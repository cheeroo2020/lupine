# 🌍 Lupine Systems  
### *Aiva × Lupine × Cloked — Building Compliant Financial Infrastructure for the AI Era*

Lupine Systems is a compliance-first, cross-border value movement stack that integrates **AI intelligence, execution rails, and cloaked compliance** for global research, health, and innovation ecosystems.

---

## 🧭 Overview (as of Nov 2025)

**Aiva** — *The Intelligence Layer*  
> Determines how and when value should move (routing, FX timing, corridor scoring, risk-aware decisions).

**Lupine** — *The Payment Execution Rail*  
> Moves funds securely and transparently across corridors (AU ↔ SG ↔ MY).

**Cloked Compliance** — *The Silent Regulatory Shield*  
> Ensures AI-resistant, audit-ready exports and blockchain-anchored trust.

Together, they enable you to:  
**Move value with certainty. Decide how it moves. Prove it’s safe to move.**

---

## 🧩 System Architecture

```
AIVA → LUPINE → CLOKED COMPLIANCE
```

- **Aiva (ai/):** FX and route simulation, thresholds, sanctions mock, velocity checks, carbon estimator, audit logging.  
- **Lupine (rail/):** FastAPI service with `/quote`, `/pay`, and `/status` endpoints, supporting AU↔SG↔MY corridors.  
- **Cloked Compliance (compliance/):** KYC flows, risk logs, statement hashing → anchor (testnet) → verify → uncloak.

---

## ⚙️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Backend** | Python · FastAPI · Pydantic |
| **Compliance** | Blockchain Anchoring · KYC Flow · Risk Logging |
| **AI Layer** | FX Trend Analysis · Smart Routing · Compliance Scoring |
| **Frontend (future)** | Vite · Tailwind · ShadCN · Lovable.dev |
| **Infrastructure** | Docker · GitHub Actions CI/CD (planned) |

---

## 📁 Repository Overview

```
ai/              → Aiva intelligence engine
rail/            → Lupine payment rail (FastAPI)
compliance/      → Cloaked Compliance trust layer
fx_data/         → Mock FX, balances, audit, and carbon data
docs/            → Vision, Mission, Governance, Ethics
tests/           → Compliance and routing verification
logbook.md       → Daily build journal
```

---

## 🧠 Vision

To build **AI-safe, compliance-first financial infrastructure**  
that connects innovation ecosystems across the Indo-Pacific —  
where speed, transparency, and trust move together.

---

## 🎯 Mission

- Reduce cross-border payment friction for regulated sectors  
- Make compliance auditable yet invisible (“Cloked”)  
- Embed ethical AI decisioning in every transaction  
- Prove that trust can scale as infrastructure

---

## 🪜 Roadmap

**Q4 2025**  
- Integrate Aiva routing engine with Lupine rail sandbox  
- Anchor compliance exports to Polygon testnet  
- Demo: Export → Hash → Anchor → Verify → Uncloak  

**2026**  
- Pilot corridor AU ↔ SG ↔ MY  
- Implement carbon-aware FX optimization  

**2027–2030**  
- Expand corridors (Japan, India, Indonesia)  
- Obtain EMI / AFSL licensing  
- Launch Cloaked Compliance as a Service (CaaS)

---

## 👤 Founder

**Chirantan (Chris) Gogoi**  
📍 Based in Australia  
Fintech strategist and compliance innovator building AI-resilient payment infrastructure for the Indo-Pacific.  

🔗 [LinkedIn](https://linkedin.com/in/chirantangogoi)  
📧 cheeroo2020 [at] gmail.com  

---

## 🪶 Philosophy

> Transparency without exposure.  
> Compliance without delay.  
> Trust without friction.

---

# 🧱 Technical Documentation and Development History

## 🌐 Aiva Glow Wallet
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
├── compliance/               # compliance-first reset
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

---

## 📊 Sprint 3 Progress (2–22 Sep 2025)
| Task ID  | Title | Status |
|----------|-------|--------|
| AIVA-46  | Compliance Rule Engine (thresholds) | ✅ Done |
| AIVA-47  | Velocity & Pattern Checks | ✅ Done |
| AIVA-48  | Enrich transaction log with compliance metadata | ⏳ In Progress|
| AIVA-49  | Audit Logging framework | ✅ Done |
| AIVA-50  | Privacy & Data Mapping (APP) | ⏳ In Progress|
| AIVA-51  | AI Ethics Safeguards | ⏳ In Progress|

---

## 🔄 Reset (1 Oct 2025)
- Compliance-first structure introduced: `/compliance`, `/docs`, `/tests`
- Defined new pillars in `Mission.md`
- Created KYC and risk log scaffolds
- Documented 4 compliance pillars

---

## 🧠 Module Progress
1. **Wallet UI (/lovable_ui)** — Complete core dashboard & FX UI  
2. **Smart FX AI Engine (/ai)** — Enhanced simulation & audit logic  
3. **FX Data Store (/fx_data)** — Carbon and compliance enrichment  
4. **Compliance (/compliance)** — Rule framework + KYC logs  
5. **Docs (/docs)** — Governance + Ethics scaffolds  
6. **Tests (/tests)** — OCR & Anchoring validations  

---

## 🧭 Next
- Complete reset deliverables  
- Begin Lupine FastAPI endpoints integration  
- Prototype Cloked Compliance exports  
- Prepare end-to-end demo flow

---

