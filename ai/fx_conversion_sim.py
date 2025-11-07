#!/usr/bin/env python3
"""
FX Conversion Simulator (Sprint 3 – Compliance & Risk)
- Loads latest FX rates (fx_data/fxrates.json)
- Derives inverses and crosses via AUD when needed
- Updates/saves balances (fx_data/balances.json)
- Estimates CO2 (fx_data/carbon_factors.json)
- Runs compliance checks (thresholds, velocity, sanctions mock)
- Appends a transaction record (fx_data/transactions_log.json)
- Writes audit events (fx_data/audit_log.json)

Usage:
  python3 ai/fx_conversion_sim.py <SRC> <DST> <AMOUNT>
  e.g. python3 ai/fx_conversion_sim.py USD AUD 200
"""

import json
import sys
import uuid
from collections import OrderedDict
from pathlib import Path
from datetime import datetime, timedelta

# ---------- Paths ----------
FX_RATES_PATH         = Path("fx_data/fxrates.json")
BALANCES_PATH         = Path("fx_data/balances.json")
CARBON_FACTORS_PATH   = Path("fx_data/carbon_factors.json")
TX_LOG_PATH           = Path("fx_data/transactions_log.json")
AUDIT_LOG_PATH        = Path("fx_data/audit_log.json")

SUPPORTED = {"USD", "EUR", "AUD"}

# ---------- Compliance Config (simple, JSON-free for now) ----------
COMPLIANCE_CONFIG = {
    "amount_thresholds": {"review": 10_000.0, "blocked": 50_000.0},
    "velocity": {"window_seconds": 60, "min_count": 3, "scope": "by_src"},
    "sanctions": {"blocked_pairs": []}  # e.g. ["USD_RUS", "ANY_IRR"]
}

# ---------- Small JSON helpers ----------
def load_json_ordered(path: Path):
    """Load JSON preserving order (useful for date->rates mapping)."""
    with open(path, "r") as f:
        return json.load(f, object_pairs_hook=OrderedDict)

def load_json(path: Path, default):
    """Load JSON (or return default if file missing/empty/invalid)."""
    if not path.exists():
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return default

def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def append_tx_log(entry: dict):
    """Append one transaction dict to fx_data/transactions_log.json safely."""
    log = load_json(TX_LOG_PATH, default=[])
    log.append(entry)
    save_json(TX_LOG_PATH, log)

def append_audit(event: dict):
    """Append a structured audit event to fx_data/audit_log.json."""
    audit = load_json(AUDIT_LOG_PATH, default=[])
    audit.append(event)
    save_json(AUDIT_LOG_PATH, audit)

# ---------- Audit schema helpers (NEW) ----------
AUDIT_SCHEMA_VERSION = "1.0"

def _severity_for(status: str, rules: list[str]) -> str:
    """
    blocked -> high, review -> medium, clear -> low
    """
    s = (status or "").lower()
    if s == "blocked":
        return "high"
    if s == "review":
        return "medium"
    return "low"

def _actor_info() -> dict:
    """
    Placeholder until you add auth; swap later for real user/session IDs.
    """
    return {"user_id": "local_dev", "session_id": "cli"}

def write_audit(
    *,
    event: str,            # "conversion_attempt" | "conversion_settled"
    tx_id: str,
    pair: str,
    fx_date_used: str | None,
    rate: float | None,
    amount_src: float,
    amount_dst: float | None,
    status: str,
    reason: str,
    rules: list[str],
) -> None:
    event_doc = {
        "event_id": uuid.uuid4().hex,
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "schema": {"name": "aiva.audit", "version": AUDIT_SCHEMA_VERSION},
        "event": event,
        "tx_id": tx_id,
        "pair": pair,
        "fx_date_used": fx_date_used,
        "rate": round(rate, 6) if isinstance(rate, (float, int)) else None,
        "amount_src": round(amount_src, 2),
        "amount_dst": round(amount_dst, 2) if isinstance(amount_dst, (float, int)) else None,
        "compliance": {
            "status": status,
            "reason": reason,
            "rules_triggered": rules,
            "severity": _severity_for(status, rules),
        },
        "actor": _actor_info(),
    }
    append_audit(event_doc)

# ---------- FX rate helpers ----------
def latest_day_rates(fx):
    """
    fx is a dict like:
    {
      "2025-08-01": {"USD_AUD": 1.52, "EUR_AUD": 1.66},
      ...
    }
    """
    latest_date = max(fx.keys())
    return latest_date, fx[latest_date]

def _inv(x: float) -> float:
    return 1.0 / float(x)

def get_rate(day_rates: dict, src: str, dst: str) -> float:
    """
    Expect base pairs quoted vs AUD:
      - USD_AUD
      - EUR_AUD
    Derive:
      - inverses: AUD_USD, AUD_EUR
      - crosses via AUD: USD_EUR, EUR_USD
    Also return direct pairs if present.
    """
    if src == dst:
        return 1.0

    # 1) direct
    direct_key = f"{src}_{dst}"
    if direct_key in day_rates:
        return float(day_rates[direct_key])

    # 2) build derived table from *_AUD
    usd_aud = day_rates.get("USD_AUD")
    eur_aud = day_rates.get("EUR_AUD")

    derived = {}
    if usd_aud is not None:
        usd_aud = float(usd_aud)
        derived["USD_AUD"] = usd_aud
        derived["AUD_USD"] = _inv(usd_aud)

    if eur_aud is not None:
        eur_aud = float(eur_aud)
        derived["EUR_AUD"] = eur_aud
        derived["AUD_EUR"] = _inv(eur_aud)

    # crosses if both known
    if ("USD_AUD" in derived) and ("EUR_AUD" in derived):
        derived["USD_EUR"] = derived["USD_AUD"] / derived["EUR_AUD"]
        derived["EUR_USD"] = _inv(derived["USD_EUR"])

    if direct_key in derived:
        return derived[direct_key]

    raise ValueError(
        f"No rate available for {src}->{dst}. "
        f"Check fx_data/fxrates.json (need USD_AUD and/or EUR_AUD)."
    )

# ---------- Carbon ----------
def load_carbon_factor(pair_key: str) -> float:
    """
    Reads fx_data/carbon_factors.json expecting keys like "USD_AUD": 0.42
    Returns a default if missing.
    """
    factors = load_json(CARBON_FACTORS_PATH, default={})
    return float(factors.get(pair_key, 0.5))  # fallback default

def estimate_carbon_kg(amount_src: float, pair_key: str) -> float:
    """
    Very simple model: linear factor per 1000 units converted.
    E.g., factor=0.42 means 0.42 kg CO2 per 1000 source currency units.
    """
    factor = load_carbon_factor(pair_key)
    return (amount_src / 1000.0) * factor

def carbon_badge(kg: float) -> str:
    if kg < 0.5:
        return "Low"
    if kg < 2.0:
        return "Medium"
    return "High"

# ---------- Compliance ----------
def _now_utc() -> datetime:
    return datetime.utcnow()

def _parse_iso(ts: str) -> datetime:
    if ts.endswith("Z"):
        ts = ts[:-1]
    return datetime.fromisoformat(ts)

def recent_tx_count(window_seconds: int, scope: str, src: str, dst: str) -> int:
    """
    Count transactions in the recent window to detect velocity/structuring.
    scope:
      - "any": count all tx
      - "by_src": only same source currency
      - "by_pair": only same src->dst pair
    """
    log = load_json(TX_LOG_PATH, default=[])
    if not log:
        return 0

    cutoff = _now_utc() - timedelta(seconds=window_seconds)
    n = 0
    for t in reversed(log[-200:]):  # look at last 200 to keep it quick
        ts = t.get("timestamp")
        try:
            t_dt = _parse_iso(ts) if isinstance(ts, str) else None
        except Exception:
            t_dt = None

        if not t_dt or t_dt < cutoff:
            continue

        if scope == "any":
            n += 1
        elif scope == "by_src":
            if t.get("pair", "").startswith(f"{src}_"):
                n += 1
        elif scope == "by_pair":
            if t.get("pair") == f"{src}_{dst}":
                n += 1
    return n

def sanctions_hit(src: str, dst: str) -> bool:
    """Very simple pair blacklist check."""
    pair = f"{src}_{dst}"
    blocked = set(COMPLIANCE_CONFIG["sanctions"]["blocked_pairs"])
    return pair in blocked or f"ANY_{dst}" in blocked or f"{src}_ANY" in blocked

def compliance_check(amount_src: float, src: str, dst: str) -> dict:
    """
    Returns a full compliance object:
    {
      "status": "clear" | "review" | "blocked",
      "reason": "...",
      "rules_triggered": ["threshold_review", "velocity", ...]
    }
    Rule order: sanctions > amount thresholds > velocity
    """
    rules = []
    status = "clear"
    reason = "within limits"

    # 1) Sanctions (highest severity)
    if sanctions_hit(src, dst):
        status = "blocked"
        reason = "sanctions pair blacklist"
        rules.append("sanctions_block")
        return {"status": status, "reason": reason, "rules_triggered": rules}

    # 2) Amount thresholds
    amt_cfg = COMPLIANCE_CONFIG["amount_thresholds"]
    if amount_src > amt_cfg["blocked"]:
        status = "blocked"
        reason = f"amount>{int(amt_cfg['blocked']):,}"
        rules.append("threshold_blocked")
        return {"status": status, "reason": reason, "rules_triggered": rules}
    if amount_src > amt_cfg["review"]:
        status = "review"
        reason = f"amount>{int(amt_cfg['review']):,}"
        rules.append("threshold_review")

    # 3) Velocity (structuring)
    vel_cfg = COMPLIANCE_CONFIG["velocity"]
    count = recent_tx_count(
        window_seconds=vel_cfg["window_seconds"],
        scope=vel_cfg["scope"],
        src=src,
        dst=dst
    )
    if count >= vel_cfg["min_count"]:
        if status == "review":
            status = "blocked"
            reason = f"{reason} + velocity >= {vel_cfg['min_count']} in {vel_cfg['window_seconds']}s"
        else:
            status = "review"
            reason = f"velocity >= {vel_cfg['min_count']} in {vel_cfg['window_seconds']}s"
        rules.append("velocity")

    return {"status": status, "reason": reason, "rules_triggered": rules}

# ---------- Formatting ----------
def fmt_money(x: float) -> str:
    return f"{x:,.2f}"

def fmt_kg(x: float) -> str:
    return f"{x:.2f} kg CO₂"

# ---------- Core simulation ----------
def simulate(src: str, dst: str, amount: float):
    # Load FX + latest date
    fx_all = load_json_ordered(FX_RATES_PATH)
    latest_date, day_rates = latest_day_rates(fx_all)

    # Load balances
    balances = load_json(BALANCES_PATH, default={"USD": 1000.0, "EUR": 1000.0, "AUD": 1000.0})

    # Basic checks
    src = src.upper().strip()
    dst = dst.upper().strip()

    if src not in SUPPORTED or dst not in SUPPORTED:
        raise ValueError(f"Only {sorted(SUPPORTED)} supported right now.")
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if balances.get(src, 0.0) < amount:
        raise ValueError(f"Insufficient {src} balance. Have {balances.get(src,0.0)}, need {amount}.")

    # Rate lookup
    rate = get_rate(day_rates, src, dst)
    received = round(amount * rate, 2)

    # Snapshot before
    before = balances.copy()

    # Carbon + Compliance (pre-apply so we can also audit)
    pair_key = f"{src}_{dst}"
    co2_kg = estimate_carbon_kg(amount, pair_key)
    badge = carbon_badge(co2_kg)
    comp = compliance_check(amount, src, dst)

    # If blocked, don't mutate balances – still log attempt + audit
    if comp["status"] == "blocked":
        tx_entry = {
            "tx_id": uuid.uuid4().hex,
            "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "fx_date_used": latest_date,
            "pair": pair_key,
            "rate": round(rate, 6),
            "amount_src": round(amount, 2),
            "amount_dst": 0.0,
            "balances_before": before,
            "balances_after": before,   # unchanged
            "carbon": {"kg": round(co2_kg, 2), "badge": badge},
            "compliance": comp
        }
        append_tx_log(tx_entry)

        # NEW standardized audit writer
        write_audit(
            event="conversion_attempt",
            tx_id=tx_entry["tx_id"],
            pair=pair_key,
            fx_date_used=latest_date,
            rate=rate,
            amount_src=amount,
            amount_dst=0.0,
            status=comp["status"],
            reason=comp["reason"],
            rules=comp["rules_triggered"],
        )

        # Output summary
        print("[FX Conversion Simulation]")
        print(f"Date used: {latest_date}")
        print(f"Rate {src}->{dst}: {rate:.6f}")
        print(f"Amount: {fmt_money(amount)} {src}  →  {fmt_money(0)} {dst} (BLOCKED)\n")
        print("Impact & Controls:")
        print(f"  Carbon: {fmt_kg(co2_kg)} ({badge}) | Compliance: BLOCKED ({', '.join(comp['rules_triggered'])})")
        return

    # Apply conversion (clear or review both settle; review is a soft control here)
    balances[src] = round(balances[src] - amount, 2)
    balances[dst] = round(balances.get(dst, 0.0) + received, 2)

    # Build transaction entry
    tx_entry = {
        "tx_id": uuid.uuid4().hex,
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "fx_date_used": latest_date,
        "pair": pair_key,
        "rate": round(rate, 6),
        "amount_src": round(amount, 2),
        "amount_dst": received,
        "balances_before": {
            "USD": before.get("USD", 0.0),
            "EUR": before.get("EUR", 0.0),
            "AUD": before.get("AUD", 0.0),
        },
        "balances_after": {
            "USD": balances.get("USD", 0.0),
            "EUR": balances.get("EUR", 0.0),
            "AUD": balances.get("AUD", 0.0),
        },
        "carbon": {"kg": round(co2_kg, 2), "badge": badge},
        "compliance": comp
    }

    # Persist changes
    save_json(BALANCES_PATH, balances)
    append_tx_log(tx_entry)

    # NEW standardized audit writer
    write_audit(
        event="conversion_settled",
        tx_id=tx_entry["tx_id"],
        pair=pair_key,
        fx_date_used=latest_date,
        rate=rate,
        amount_src=amount,
        amount_dst=received,
        status=comp["status"],
        reason=comp["reason"],
        rules=comp["rules_triggered"],
    )

    # ---- Output ----
    print("[FX Conversion Simulation]")
    print(f"Date used: {latest_date}")
    print(f"Rate {src}->{dst}: {rate:.6f}")
    print(f"Amount: {fmt_money(amount)} {src}  →  {fmt_money(received)} {dst}\n")

    print("Before:")
    print(f"  USD {fmt_money(before.get('USD',0))} | "
          f"EUR {fmt_money(before.get('EUR',0))} | "
          f"AUD {fmt_money(before.get('AUD',0))}")

    print("\nAfter:")
    print(f"  USD {fmt_money(balances.get('USD',0))} | "
          f"EUR {fmt_money(balances.get('EUR',0))} | "
          f"AUD {fmt_money(balances.get('AUD',0))}")

    print("\nImpact & Controls:")
    print(f"  Carbon: {fmt_kg(co2_kg)}  ({badge})  |  Compliance: {comp['status'].upper()} ({comp['reason']})")
    if comp["rules_triggered"]:
        print(f"  Rules: {comma_join(comp['rules_triggered']) if 'comma_join' in globals() else ', '.join(comp['rules_triggered'])}")

    print("\nOne-liner:")
    print(f"  {src}->{dst} @ {rate:.4f} | {fmt_money(amount)} {src} → {fmt_money(received)} {dst} "
          f"| CO₂ {fmt_kg(co2_kg)} ({badge}) | {comp['status'].upper()} ({comp['reason']})")

# ---------- CLI ----------
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 ai/fx_conversion_sim.py <SRC> <DST> <AMOUNT>")
        print("Example: python3 ai/fx_conversion_sim.py USD AUD 200")
        sys.exit(1)

    src, dst, amount_str = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        amount = float(amount_str)
    except ValueError:
        print("AMOUNT must be a number, e.g., 200 or 150.50")
        sys.exit(1)

    simulate(src, dst, amount)

if __name__ == "__main__":
    main()
