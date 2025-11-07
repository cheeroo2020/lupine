# 📘 Technical Documentation: Multi-Currency Wallet Project

This document serves as an extensive, systematic, and educational backend reference for the Aiva Glow Wallet project.  
It combines code-level explanations, backend best practices, architecture notes, and learning checkpoints.

---

## 📂 Repository Structure

```
├── ai/                      # Smart FX engine & simulations
│   ├── fx_trend_analysis.py
│   ├── fx_trend_with_threshold.py
│   ├── fx_conversion_sim.py   # mock balance FX simulation with carbon & compliance
│   └── carbon_estimator.py
│
├── fx_data/                 # Mock FX, balances, transaction, and carbon data
│   ├── fxrates.json
│   ├── balances.json
│   ├── transactions_sample.json
│   └── carbon_factors.json
│
├── lovable_ui/              # UI exported from Lovable (Markdown + assets)
│   ├── ai_suggestion_component.md
│   ├── compliance_collapsible_panel.md
│   └── Smart Fx.png
│
├── designs/                 # UI concepts
├── screenshots/             # Output snapshots for tracking
├── logbook.md               # Daily build journal
└── README.md                # Project overview
```

---

## 🔑 Key Python Files & Functions

### 1. `ai/fx_trend_analysis.py`
- Detects rising/falling/stable FX trends over mock 7-day data.
- Core function: compares first vs last rate to label as *rising*, *falling*, or *stable*.

**Learning notes:**
- Demonstrates simple iteration and conditional logic.
- Relates to wallet: drives Smart FX recommendation engine.

---

### 2. `ai/fx_trend_with_threshold.py`
- Extends trend detection by introducing % thresholds.
- Suggests **Convert Now** vs **Wait** based on move size.

**Learning notes:**
- Introduces percentage math and threshold-based decision logic.
- Python: reinforces rounding, formatting, and safe numeric operations.

---

### 3. `ai/fx_conversion_sim.py`
- Simulates wallet balances and FX conversions.
- Features:
  - Reads balances from `fx_data/balances.json`
  - Ensures sufficiency before conversion
  - Updates balances post conversion
  - Logs each transaction into `transactions_sample.json`
  - Attaches compliance decision + carbon estimate

**Learning notes:**
- Core backend simulation of wallet operations.
- Teaches JSON persistence, error handling, and audit logging.

---

### 4. `ai/carbon_estimator.py`
- Estimates carbon footprint of each transaction.
- Uses method factor + FX bonus factor to compute CO₂.
- Labels each transaction as Low / Medium / High.

**Learning notes:**
- Shows config-driven computation (factors externalized in JSON).
- Prepares for UI integration (badges next to transactions).

---

## 🛠 Backend Learning Notes & Best Practices

- **JSON vs Database**: Mock JSONs mimic tables. Later, migrate to PostgreSQL with SQLAlchemy ORM models.
- **Functions**: Each function is *pure* (predictable output from inputs) where possible → easy to test.
- **Error Handling**: Use `.get()` with defaults, but production code should validate inputs with `pydantic`.
- **Logging vs Print**: For production, prefer `logging` library.
- **Precision**: Use `decimal.Decimal` for financial values instead of `float`.

---

## 🏗 Backend Architecture (Conceptual)

### Core Components
- **API Layer (FastAPI planned):** Endpoints for wallet creation, FX conversion, compliance check.
- **Data Layer:** PostgreSQL tables → Users, Wallets, Balances, Transactions, Compliance Logs.
- **Logic Layer:** FX rate retrieval, conversion simulation, compliance rules, carbon estimation.
- **UI Layer:** Lovable mockups, React prototype later.

### Typical Workflow: FX Conversion
1. User initiates conversion (UI → API).  
2. Backend checks balances, compliance, and rates.  
3. Conversion applied → new balances saved.  
4. Transaction appended with carbon + compliance info.  
5. Response returned to UI.

---

## 🧩 Example Database Schema (PostgreSQL)

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE wallets (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE balances (
    id SERIAL PRIMARY KEY,
    wallet_id INT REFERENCES wallets(id),
    currency_code CHAR(3),
    amount NUMERIC
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    wallet_id INT REFERENCES wallets(id),
    type TEXT,
    src_currency CHAR(3),
    dst_currency CHAR(3),
    amount NUMERIC,
    rate NUMERIC,
    carbon_kg NUMERIC,
    compliance_status TEXT,
    created_at TIMESTAMP DEFAULT now()
);
```

---

## 📚 Learning Checkpoints

1. **Functions:** Explain the difference between `return` and `print` in Python.  
2. **JSON I/O:** Create a script that appends a new mock transaction into `transactions_sample.json`.  
3. **Compliance:** Extend `fx_conversion_sim.py` to reject transactions above a set threshold.  
4. **Carbon:** Modify `carbon_estimator.py` to save enriched transactions into a new JSON file.  
5. **Database:** Sketch how you would translate `balances.json` into a SQL table.

---

## 📈 Industry Best Practices vs Current Project

- ✅ **Good:** Modular design, JSON-driven configs, clear sprint logbook.  
- ⚠️ **Needs Work:** Replace prints with logging, enforce type safety, migrate from JSON to DB, secure API layer.  
- 🚀 **Next Step:** Deploy small FastAPI app with `/convert`, `/balances`, `/transactions` endpoints.

---

## 🧭 Final Notes

This documentation is designed both as a **teaching tool** and a **handover guide**.  
A new developer should be able to read this, run the project, and extend it with real APIs and databases.

