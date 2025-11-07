import sys
import json
from collections import OrderedDict

DATA_PATH = "fx_data/fxrates.json"
PAIRS_TO_CHECK = ["USD_AUD", "EUR_AUD", "AUD_USD"]  # safe to include missing; we'll handle it
THRESHOLD_PCT = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0


def load_data(path):
    with open(path, "r") as f:
        data = json.load(f)
    # Ensure dates are processed in ascending order
    ordered = OrderedDict(sorted(data.items(), key=lambda kv: kv[0]))
    return ordered

def series_for_pair(ordered_data, pair):
    """Return a list of rates for the given pair across dates, or None if the pair is missing."""
    values = []
    for _, day in ordered_data.items():
        if pair not in day:
            return None  # missing any day → treat as unavailable
        values.append(day[pair])
    return values

def pct_change(first, last):
    if first == 0:
        return 0.0
    return ((last - first) / first) * 100.0

def classify_move(pct):
    if pct > 0:
        return "rising"
    elif pct < 0:
        return "falling"
    else:
        return "stable"

def action_from_move(pct, quote_ccy, base_ccy):
    """
    For pair BASE_QUOTE (e.g., USD_AUD = how many AUD per 1 USD):
    - If % change magnitude >= threshold → "Convert Now"
    - Else → "Wait"
    And we phrase the action relative to the quote currency the user holds.
    """
    magnitude = abs(pct)
    urgency = "Convert Now" if magnitude >= THRESHOLD_PCT else "Wait"

    # Messaging: if USD_AUD is rising, AUD is weakening vs USD.
    # Keeping it simple and consistent with your earlier copy:
    if pct > 0:
        direction_note = f"{base_ccy} strengthening vs {quote_ccy}"
        user_tip = f"Consider converting out of {quote_ccy}"
    elif pct < 0:
        direction_note = f"{base_ccy} weakening vs {quote_ccy}"
        user_tip = f"Consider holding {quote_ccy}"
    else:
        direction_note = "No net change"
        user_tip = f"Hold {quote_ccy}"

    return urgency, direction_note, user_tip

def demo_pct(vals):
    first, last = vals[0], vals[-1]
    pct = ((last - first) / first) * 100
    print(f"demo {vals} → {pct:.2f}%")


def main():
    data = load_data(DATA_PATH)

    print("TYPE:", type(data))
    print("DATES:", list(data.keys()))
    first_date = next(iter(data.keys()))
    print("SAMPLE DAY:", first_date, "→", data[first_date])

    pair = "USD_AUD"
    manual_series = []
    missing = False
    for day in data.values():
        if pair in day:
            manual_series.append(day[pair])
        else:
            missing = True
            break

    demo_pct([1.00, 1.02])  # predict +2.00%
    demo_pct([1.00, 0.99])  # predict -1.00%


    print("USD_AUD series:", manual_series, "| missing_any_day:", missing)



    report_lines = []
    report_lines.append("[Smart FX Suggestion] 7‑day summary with threshold logic")
    report_lines.append(f"Decision threshold: {THRESHOLD_PCT:.2f}% total move\n")

    for pair in PAIRS_TO_CHECK:
        series = series_for_pair(data, pair)
        if series is None:
            report_lines.append(f"- {pair}: N/A (data missing) → Hold position")
            continue

        first, last = series[0], series[-1]
        change = pct_change(first, last)
        move = classify_move(change)

        base, quote = pair.split("_")  # e.g., USD_AUD
        urgency, note, tip = action_from_move(change, quote_ccy=quote, base_ccy=base)

        # Example line:
        # - USD_AUD: falling (−1.23%) → Wait | USD weakening vs AUD | Consider holding AUD
        sign = "+" if change > 0 else ("−" if change < 0 else "±")
        report_lines.append(
            f"- {pair}: {move} ({sign}{abs(change):.2f}%) → {urgency} | {note} | {tip}"
        )

    print("\n".join(report_lines))
    print(f"DEBUG {pair}: first={first}, last={last}, change={change:.2f}% | threshold={THRESHOLD_PCT}%")

if __name__ == "__main__":
    main()
