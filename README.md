# 🌐 Lupine Systems — Aiva (Intelligence) · Lupine (Rail) · Cloked Compliance (Trust)

Lupine Systems is a compliance-first, cross-border value movement stack:

- **Aiva** — *The Intelligence Layer*: routing, FX timing, corridor scoring, risk-aware decisions.
- **Lupine** — *The Payment Execution Rail*: fast, transparent AU↔SG↔MY sandbox payments.
- **Cloked Compliance** — *The Silent Regulatory Shield*: AI-resistant exports, audit-ready, blockchain-anchored trust.

Together: **move value with certainty**, **decide how it moves**, **prove it’s safe to move**.

---

## 🧭 Master Overview (Nov 2025)

- Target domain: research & health-science orgs moving funds across AU · SG · MY.
- Problem: funds delayed by compliance friction and poor routing.
- Approach: **Aiva decides**, **Lupine executes**, **Cloked proves** — with zero extra effort for users.

---

## ⚙️ Architecture

```
AIVA (ai/)  →  LUPINE (rail/)  →  CLOKED COMPLIANCE (compliance/)
```

- **Aiva (ai/):** FX & route simulation, thresholds, velocity, sanctions mock, carbon estimator, audit logging.
- **Lupine (rail/):** FastAPI stubs for `/quote`, `/pay`, `/status`, corridor adapters (AU↔SG↔MY).
- **Cloked Compliance (compliance/):** KYC flow, risk log, statement export → hash/anchor (testnet) → verify → uncloak.

---

## 🧭 Next Steps (Nov → Dec 2025)

**Week 1** — anchoring CLI + verifier;  
**Week 2** — Rail API + corridor adapters;  
**Week 3** — end-to-end glue;  
**Week 4** — demo: Export → Hash → Anchor → Verify → Uncloak + /quote→/pay happy path.

---

## ⬇️ Original README (preserved below)

# 🌐 Aiva Glow Wallet
A next-gen multi-currency wallet with AI-powered smart FX recommendations, live trend analysis, environmental impact tracking, and DeFi-friendly architecture — designed and built by a solo founder to explore the future of money, cross-border finance, and digital wallets.

---

## 🚀 Project Vision
Aiva is a build + learn journey to explore how the future of money is being shaped by:

- Smart FX engines
- Real-time trend data
- AI UX logic
- Environmental impact tracking (Green FX)
- Multicurrency interoperability
- Blockchain + DeFi infrastructure
- Compliance & risk intelligence

---

## 🧱 Folder Structure (Reset on 1 October 2025)
```
├── ai/                       # Smart FX engine & simulations
│   ├── fx_trend_analysis.py
│   ├── fx_trend_with_threshold.py
│   ├── fx_conversion_sim.py   # FX simulation with compliance + audit logging
│   └── carbon_estimator.py
│
├── fx_data/                  # Mock FX, balances, transaction, and carbon data
│   ├── fxrates.json
│   ├── balances.json
│   ├── transactions_sample.json
│   ├── transactions_log.json  # enriched with compliance + carbon
│   ├── audit_log.json         # structured audit log
│   └── carbon_factors.json
│
├── lovable_ui/               # UI exported from Lovable (Markdown + assets)
│   ├── ai_suggestion_component.md
│   ├── compliance_collapsible_panel.md
│   └── Smart Fx.png
│
├── compliance/               # NEW: compliance-first reset
│   ├── kyc_flow.md           # KYC/AML notes and flows
│   ├── risk_log.json         # Risk factors log
│
├── designs/                  # UI concepts
├── screenshots/              # Output snapshots for tracking
├── docs/
│   ├── Mission.md            # Reset vision pillars
│   ├── audit_log_schema.md   # Schema for audit events
│   ├── privacy_compliance.md # Privacy + compliance scaffolding
│   ├── governance.md         # Governance and regulator engagement notes
│   └── ai_ethics.md          # AI safety & ethics documentation
│
├── tests/                    # OCR, compliance, and anchoring test results
│   ├── ocr_results.md
│
├── logbook.md                # Daily build journal
└── README.md                 # Project overview
```

---

## 🧑‍💻 Sprint 1 Summary (1 Aug – 18 Aug)
| Task ID | Title | Status |
|---------|-------|--------|
| AIVA-4  | Design wallet dashboard in Lovable | ✅ Done |
| AIVA-5  | Add 3 currency balance blocks      | ✅ Done |
| AIVA-6  | Create FX converter UI             | ✅ Done |
| AIVA-7  | Display static transaction log     | ✅ Done |
| AIVA-9  | Draft Smart FX GPT prompt logic    | ✅ Done |
| AIVA-10 | Create Lovable UI element for AI suggestion | ✅ Done |
| AIVA-11 | Test FX trend data with GPT-style response | ✅ Done |
| AIVA-14 | Add FX threshold logic for convert/wait | ✅ Done |
| AIVA-15 | Simulate FX conversions with mock balances | ✅ Done |
| AIVA-52 | Add Green FX carbon badge to Smart FX UI  | ✅ Done |
| AIVA-53 | Add Compliance & Risk collapsible panel to UI | ✅ Done |

---

## 📊 Sprint 2 Summary (15–31 Aug 2025)
| Task ID | Title | Status |
|---------|-------|--------|
| AIVA-17 | Create GitHub repo aiva-wallet     | ✅ Done |
| AIVA-18 | Write README.md with vision and stack | ✅ Done |
| AIVA-19 | Add mockdata and ai folders in GitHub | ✅ Done |

**Health:** Sprint 2 completed successfully.

- Repo + README finalized.  
- `fx_conversion_sim.py` enhanced with: carbon footprint estimation, compliance stub, and transaction logging.  
- CLI runs tested with both small and large trades.  
- All deliverables closed on **31 Aug 2025**.  

---

## 📊 Sprint 3 Progress (2–22 Sep 2025)
**Status as of 22 September 2025: Compliance enrichment nearing completion**

| Task ID  | Title                                               | Status        |
|----------|-----------------------------------------------------|---------------|
| AIVA-46  | Compliance Rule Engine (thresholds)                 | ✅ Done       |
| AIVA-47  | Velocity & Pattern Checks (structuring)             | ✅ Done       |
| AIVA-48  | Enrich transaction log with compliance metadata     | ⏳ In Progress|
| AIVA-49  | Audit Logging framework                             | ✅ Done       |
| AIVA-50  | Privacy & Data Mapping (APP)                        | ⏳ In Progress|
| AIVA-51  | AI Ethics Safeguards                                | ⏳ In Progress|
| AIVA-52  | Collapsible Compliance Panel UI                     | ⏳ In Progress|
| AIVA-53  | Compliance Alerts UI                                | ⏳ In Progress|
| AIVA-106 | Implement compliance rule engine (thresholds, velocity, sanctions) | ✅ Done |

**Highlights Today (22 September 2025):**
- Refined **`ai/fx_conversion_sim.py`** with full compliance logic: threshold checks, velocity detection, and sanctions mock.  
- Integrated **audit logging** to `fx_data/audit_log.json` using a standardized writer (`write_audit`) and documented schema (`docs/audit_log_schema.md`).  
- CLI test runs: clear (small), review (>10k USD), blocked (>50k USD), and velocity (≥3 trades in 60s).  
- During large tests, insufficient balances triggered overdraft prevention as expected — captured in logbook.  
- Logbook updated for **22 Sep 2025**.  

---

## 🔄 Reset (1 Oct 2025)
- **New 90-day plan launched (Oct–Dec 2025).**
- Repo restructured with compliance-first focus:
  - `/compliance`, `/docs`, `/tests` created.  
  - Drafted **Mission.md** with 4 core pillars:  
    1. Borderless multi-currency wallet  
    2. Compliance-first design  
    3. Blockchain-anchored statements  
    4. AI-resistant, auditor-friendly exports  
- Logbook updated to mark reset milestone.  

---

## 🧠 Module Progress
1. **Wallet UI (/lovable_ui)**  
   - ✅ Dashboard, balances, FX converter, static log.  
   - ✅ Smart FX Recommendation with Green FX badge.  
   - ✅ Collapsible compliance panel.  
   - ⏳ Pending: compliance alerts, timeline transaction view, dark mode toggle.  

2. **Smart FX AI Engine (/ai)**  
   - Fully enriched `fx_conversion_sim.py` with compliance + audit logging.  
   - Thresholds, velocity, sanctions checks, and carbon estimation integrated.  

3. **FX Data Store (/fx_data)**  
   - `transactions_log.json` → enriched with compliance & carbon.  
   - `audit_log.json` → standardized audit events (`conversion_attempt`, `conversion_settled`).  

4. **Compliance (/compliance)**  
   - Reset structure added.  
   - `kyc_flow.md` scaffolded.  
   - `risk_log.json` scaffolded.  

5. **Docs (/docs)**  
   - `Mission.md` reset pillars defined.  
   - Privacy, governance, and AI ethics files scaffolded.  

6. **Tests (/tests)**  
   - OCR and compliance test logs to be added (Nov 2025).  

---

## 🧭 What’s Next
- Complete reset tasks: fill Mission.md, draft KYC flow, add first risk log.  
- Resume Sprint 3 compliance enrichment.  
- Begin Sprint 4 in October: FastAPI endpoints (`/convert`, `/balances`, `/transactions`).  
- Prototype Cloked Compliance: statement hashing + blockchain anchoring + cloaked exports.  

---

## 👤 Built By
**Chirantan (Chris) Gogoi**  
📍 Based in Australia  
🔭 Exploring the future of money, wallets, AI, and cross-border solutions  
💼 Solo founder in learning & prototyping phase
