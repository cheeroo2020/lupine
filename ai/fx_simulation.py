# fx_simulation.py

# ------------------------
# Mock balances
# ------------------------
balances = {
    "AUD": 1000.0,
    "USD": 500.0,
    "EUR": 300.0
}

# ------------------------
# FX rates
# ------------------------
fx_rates = {
    ("AUD", "USD"): 0.66,
    ("USD", "AUD"): 1.52,
    ("EUR", "USD"): 1.10,
    ("USD", "EUR"): 0.91
}

# ------------------------
# Carbon factors (kg CO₂ per 1000 units)
# ------------------------
carbon_factors = {
    ("AUD", "USD"): 0.42,
    ("USD", "AUD"): 0.45,
    ("EUR", "USD"): 0.50,
    ("USD", "EUR"): 0.40
}

# ------------------------
# Transactions log
# ------------------------
transactions = []

# ------------------------
# Compliance stub
# ------------------------
def compliance_check(amount, from_cur, to_cur):
    if amount > 10000:
        return "Review Needed"
    return "Clear"

# ------------------------
# Log a transaction
# ------------------------
def log_transaction(amount, from_cur, to_cur, converted):
    carbon_factor = carbon_factors.get((from_cur, to_cur), 0.5)
    carbon_estimate = (amount / 1000) * carbon_factor
    compliance_status = compliance_check(amount, from_cur, to_cur)

    tx = {
        "from": from_cur,
        "to": to_cur,
        "amount": amount,
        "converted": converted,
        "carbon": f"{carbon_estimate:.2f} kg CO₂",
        "compliance": compliance_status
    }
    transactions.append(tx)
    print("Logged Transaction:", tx)

# ------------------------
# Convert
# ------------------------
def convert(amount, from_cur, to_cur):
    pair = (from_cur, to_cur)

    if pair not in fx_rates:
        print(f"No rate for {from_cur}->{to_cur}")
        return

    rate = fx_rates[pair]
    converted = amount * rate

    if balances[from_cur] >= amount:
        balances[from_cur] -= amount
        balances[to_cur] += converted
        log_transaction(amount, from_cur, to_cur, converted)
        print(f"Converted {amount} {from_cur} → {converted:.2f} {to_cur}")
    else:
        print("Insufficient funds")

    print("Updated Balances:", balances)

# ------------------------
# Test
# ------------------------
print("Initial Balances:", balances)
convert(100, "AUD", "USD")
convert(200, "USD", "EUR")
print("All Transactions:", transactions)
