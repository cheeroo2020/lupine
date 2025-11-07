# 📑 Aiva Audit Log Schema (v1.0)

The **audit log** (`fx_data/audit_log.json`) captures all compliance-relevant events in a structured, append-only format.  
It ensures transparency, traceability, and consistency across simulation runs.

---

## 🔖 Schema Metadata
- **Schema Name:** `aiva.audit`
- **Version:** `1.0`
- **File:** `fx_data/audit_log.json`
- **Storage:** JSON array of events, append-only

---

## 🗂️ Event Structure

```json
{
  "event_id": "uuid",
  "timestamp": "2025-09-22T05:14:09Z",
  "schema": {
    "name": "aiva.audit",
    "version": "1.0"
  },
  "event": "conversion_attempt",     // or "conversion_settled"
  "tx_id": "linked transaction id",
  "pair": "USD_AUD",
  "fx_date_used": "2025-09-21",
  "rate": 1.523411,
  "amount_src": 15000.0,
  "amount_dst": 22851.17,
  "compliance": {
    "status": "review",              // "clear" | "review" | "blocked"
    "reason": "amount > 10,000",
    "rules_triggered": ["threshold_review"],
    "severity": "medium"             // low | medium | high
  },
  "actor": {
    "user_id": "local_dev",
    "session_id": "cli"
  }
}
```

---

## 🧩 Field Reference

| Field             | Type     | Description |
|-------------------|----------|-------------|
| `event_id`        | string   | Unique UUID for the audit event |
| `timestamp`       | string   | UTC timestamp (ISO 8601, Zulu) |
| `schema`          | object   | Name/version of schema |
| `event`           | string   | `"conversion_attempt"` (blocked) or `"conversion_settled"` (clear/review) |
| `tx_id`           | string   | Transaction ID linked to `transactions_log.json` |
| `pair`            | string   | Currency pair (e.g., `USD_AUD`) |
| `fx_date_used`    | string   | FX rate date (YYYY-MM-DD) |
| `rate`            | float    | Conversion rate used |
| `amount_src`      | float    | Source currency amount |
| `amount_dst`      | float    | Destination amount (0.0 if blocked) |
| `compliance`      | object   | Result of compliance checks |
| `actor`           | object   | Info about actor/session (placeholder for now) |

---

## 🔍 Compliance Object
The `compliance` sub-object captures why an event was reviewed or blocked.

- **status:**  
  - `clear` → within limits  
  - `review` → needs further checks  
  - `blocked` → prohibited  

- **reason:** Human-readable explanation (e.g. `"amount > 10,000"`, `"velocity >= 3 in 60s"`).  
- **rules_triggered:** Array of short codes (`threshold_review`, `velocity`, `sanctions_block`).  
- **severity:** Normalized risk level (`low`, `medium`, `high`).

---

## 🧑 Actor Object
For now:
```json
{
  "user_id": "local_dev",
  "session_id": "cli"
}
```
In future:
- Replace with authenticated user/session IDs.  
- Extend with IP, device, or channel information if needed.

---

## 📝 Notes
- Every transaction creates **both**:
  - A transaction entry in `transactions_log.json`
  - An audit entry in `audit_log.json`  
- **Blocked attempts** still get logged with `"conversion_attempt"`.  
- **Clear/Review settlements** are logged with `"conversion_settled"`.  

---

📌 **Versioning:** If the schema changes, bump `version` and document deltas here.
