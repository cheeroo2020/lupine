import json

# Load data from fxrates.json
with open('fx_data/fxrates.json', 'r') as f:
    data = json.load(f)

trend_summary = {}

def detect_trend(rates):
    if rates[-1] > rates[0]:
        return "rising"
    elif rates[-1] < rates[0]:
        return "falling"
    else:
        return "stable"

# Analyze each currency pair
for pair in ['USD_AUD', 'EUR_AUD', 'AUD_USD']:
    # Collect that pair's values from each date
    try:
        pair_values = [entry[pair] for entry in data.values()]
        trend = detect_trend(pair_values)
    except KeyError:
        trend = "N/A (Data missing)"
    
    trend_summary[pair] = trend

# Prepare recommendation string
suggestion = "[Smart FX Suggestion] Based on the past 7 days:\n"
for pair, trend in trend_summary.items():
    if trend == "rising":
        action = "Consider converting into"
    elif trend == "falling":
        action = "Consider converting out of"
    else:
        action = "Hold position in"
    
    suggestion += f"- {pair}: {trend} trend → {action} {pair.split('_')[1]}\n"

print(suggestion)
