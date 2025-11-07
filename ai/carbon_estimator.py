import json, math, os

TX_PATH = "fx_data/transactions_sample.json"
CF_PATH = "fx_data/carbon_factors.json"

def load_json(p):
    with open(p, "r") as f:
        return json.load(f)

def estimate_tx_kg(tx, factors):
    method_factor = factors["method_factor_kg_per_tx"].get(tx.get("method"), 0.05)
    fx_bonus = 0.0
    if tx.get("type") == "fx_convert":
        amt = float(tx.get("amount_base", 0))
        fx_bonus = (amt / 100.0) * factors["fx_bonus_factor_kg_per_100_base"]
    return round(method_factor + fx_bonus, 3)

def label_band(kg):
    if kg < 0.05: return "Low"
    if kg < 0.15: return "Medium"
    return "High"

def main():
    txs = load_json(TX_PATH)
    factors = load_json(CF_PATH)
    print("[Green FX] Estimated carbon per transaction\n")
    for tx in txs:
        kg = estimate_tx_kg(tx, factors)
        band = label_band(kg)
        label = f"{kg} kg CO₂ ({band})"
        title = f"#{tx['id']} {tx['type']} • {tx.get('pair', tx.get('currency',''))}"
        print(f"- {title:30s} → {label}  |  [Offset]")
    print("\nTip: Show this badge next to each transaction in the UI, with an 'Offset' button (future).")

if __name__ == "__main__":
    main()
