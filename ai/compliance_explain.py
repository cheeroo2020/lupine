import json

RULES_PATH = "fx_data/compliance_rules.json"
CASES_PATH = "fx_data/compliance_examples.json"

def load_json(p):
    with open(p, "r") as f:
        return json.load(f)

def evaluate(tx, rules):
    if tx.get("dest_country") in rules["blocked_countries"]:
        code = "COUNTRY_BLOCKED"
    elif tx.get("amount", 0) >= rules["kyc_required_above"] and not tx.get("kyc_verified", False):
        code = "KYC_REQUIRED"
    else:
        code = "OK"
    return {
        "id": tx["id"],
        "status": code,
        "explanation": rules["explanations"][code],
        "next_step": rules["next_steps"][code]
    }

def main():
    rules = load_json(RULES_PATH)
    cases = load_json(CASES_PATH)
    print("[Compliance] Why is this blocked? (human readable)\n")
    for tx in cases:
        res = evaluate(tx, rules)
        print(f"- #{res['id']} → {res['status']}")
        print(f"  Why: {res['explanation']}")
        print(f"  Next: {res['next_step']}\n")
    print("Tip: Show this panel inline when a transaction is blocked, instead of a generic error.")

if __name__ == "__main__":
    main()
