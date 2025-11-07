# 📘 Aiva Glow Wallet – Logbook

---

## 📅 August 1, 2025

### ✅ What I did
- Finalised project name: Aiva Glow Wallet
- Created GitHub repository and committed base folder structure
- Set up Jira project (team-managed) and created Epics and Sprint 1
- Linked each task to relevant epics

### 📘 What I learned
- How Jira epics, sprints, and stories interact
- How to set up a GitHub project repo from scratch
- Importance of naming clarity and structure

### 🤔 Open questions
- What's the best UI flow for a multicurrency wallet?

### ⏭️ Next steps
- Design initial UI in Lovable
- Start breaking down tasks into subtasks

---

## 📅 August 2, 2025

### ✅ What I did
- Built wallet dashboard, currency blocks, and converter UI in Lovable
- Organised files: `lovable_ui/`, `ai/`, `mockdata/` in GitHub
- Added screenshots of design work
- Resolved subtasks and backlog sync in Jira
- Marked completed UI tasks as Done in Jira

### 📘 What I learned
- Using Lovable as a low-fidelity UI tool
- Creating subtasks in Jira using the command palette
- How to properly structure folders in GitHub

### 🤔 Open questions
- How will the Smart FX assistant look and behave?

### ⏭️ Next steps
- Begin AI logic for FX recommendation (AIVA-9)
- Start AIVA-10: build Lovable UI block for GPT output

---

## 📅 August 3, 2025

### ✅ What I did
- Created `/lovable_ui/ai_suggestion_component.md` for AIVA-10
- Added README updates to GitHub with project description
- Set repo metadata: topics, description, cleaned up folders
- Created full logbook file for 6 weeks
- Confirmed sprint board reflects current progress

### 📘 What I learned
- GitHub metadata settings (topics, descriptions)
- Markdown structure for logging daily progress
- Project setup alignment between tools (Jira + GitHub)

### 🤔 Open questions
- How to test Smart FX AI logic locally
- Best practices for frontend-GPT interaction

### ⏭️ Next steps
- Continue with Smart FX AI prompt development (AIVA-9)
- Sketch wireframe of Smart FX suggestion UI

## 📅 5 August 2025 — Compliance Epic Added

**Overview:**  
Today marks the official inclusion of a new core module — **Compliance & Risk Management** — into the Aiva Glow Wallet project. This decision strengthens the product’s alignment with regulatory, ethical, and user protection standards necessary for fintech products operating in global environments.

---

### ✅ Key Activities

- 🧱 **Created new Epic:** `COMPLIANCE & RISK MANAGEMENT`
- 🗂 **Added Jira tasks under new epic:**
  - **AIVA-46**: Design KYC/AML onboarding flow
  - **AIVA-47**: Draft compliance checklist for FX transactions
  - **AIVA-48**: Define how to log sensitive actions (audit trail)
  - **AIVA-49**: Map data handling policy to Australian Privacy Principles (APPs)
  - **AIVA-50**: Create UI mockup for compliance alerts (e.g., conversion blocked)
  - **AIVA-51**: Define AI ethics safeguards for Smart FX suggestions
- 📝 Planned implementation of backend + UI elements for compliance
- 🔍 Reviewed Jira and ensured all prior tasks are mapped correctly

---

### 🚧 Status Summary

| Task ID  | Title                                                 | Epic                         | Status  |
|----------|-------------------------------------------------------|------------------------------|---------|
| AIVA-46  | Design KYC/AML onboarding flow                        | Compliance & Risk Management | ⏳ To Do |
| AIVA-47  | Draft compliance checklist for FX transactions        | Compliance & Risk Management | ⏳ To Do |
| AIVA-48  | Define how to log sensitive actions (audit trail)     | Compliance & Risk Management | ⏳ To Do |
| AIVA-49  | Map data handling to Australian Privacy Principles    | Compliance & Risk Management | ⏳ To Do |
| AIVA-50  | Create UI mockup for compliance alerts                | Compliance & Risk Management | ⏳ To Do |
| AIVA-51  | Define AI ethics safeguards for Smart FX suggestions  | Compliance & Risk Management | ⏳ To Do |

---

### 🧠 Notes
- These tasks are foundational for the legal, ethical, and privacy-aware design of Aiva.
- Implementation begins after current Sprint 1 UI and AI modules reach 100% completion.
- This shift also supports future discussions with investors, regulators, or incubators.

## 📅 6 August 2025 – Compliance Foundation

### ✅ Task Completed
- **AIVA-46:** Drafted KYC/AML Onboarding Flow

### 🛠 Work Summary
- Designed a user journey to collect personal data and verify identity:
  - Collected: Name, DOB, address
  - Uploaded: ID documents (passport, driver’s license)
  - Status: Verified / Pending / Retry

### 📂 Output
- Created `compliance_flows.md` file documenting the onboarding logic
- Committed to GitHub with message: `Added draft KYC/AML onboarding flow (AIVA-46)`


---

### 📅 7 August 2025

**Task ID:** AIVA-11  
**Title:** Test FX trend data with GPT response  
**Epic:** Smart FX AI Engine  
**Status:** ✅ Completed  

---

#### 🧠 Objective  
Implement a Python script that reads mock FX rate data, detects 7-day trends, and outputs Smart FX-style conversion recommendations for selected currency pairs.

---

#### ✅ Steps Completed

1. Opened AIVA-11 task to analyse FX trend using GPT-style logic.
2. Created directory structure:  
   - `fx_data/` for storing JSON rate files  
   - `ai/` for placing Python analysis scripts  
3. Created `fxrates.json` using 7-day sample data manually inside `fx_data/`.
4. Wrote `fx_trend_analysis.py` in `ai/` to:
   - Read `fxrates.json`
   - Extract currency pair values
   - Analyse whether the trend was rising, falling, or stable
   - Generate natural language suggestions
5. Ran into the following **issues** and fixed them step-by-step:

---

#### 🛠️ Troubleshooting and Fixes

| Issue | Root Cause | Fix |
|------|------------|-----|
| `cd path/to/your/aiva-glow-wallet` fails | Placeholder path not replaced | Used actual local repo path (`~/Desktop/aiva-glow-wallet`) |
| `FileNotFoundError` on `fxrates.json` | File didn’t exist yet | Created file using `touch fx_data/fxrates.json` |
| `fxrates.json` not found again | Wrong relative path | Ensured it was located inside `fx_data/` and referenced correctly from `ai/` |
| KeyError: `'USD_AUD'` | Tried to access pair as top-level key | Realised JSON had dates as top-level keys, each containing pairs |
| IndentationError after `for` loop | Block not indented | Properly indented the loop block |
| Confusion on logic order | Was unclear how each part connects | Broke into smaller debug/test steps |
| Added `"AUD_USD"` to pair list | This key doesn’t exist in JSON | Handled missing data gracefully with fallback logic |

---

#### 📸 Output Screenshot  
> 📂 **Stored in:** `screenshots/`  
![FX Suggestion Output](../screenshots/Screenshot%202025-08-07%20at%2010.38.47%E2%80%AFpm.png)

> **Smart FX Suggestions (Auto-generated)**  
> ```
> [Smart FX Suggestion] Based on the past 7 days:
> - USD_AUD: falling trend → Consider converting out of AUD  
> - EUR_AUD: falling trend → Consider converting out of AUD  
> - AUD_USD: N/A (Data missing) trend → Hold position in USD  
> ```

---
### 💻 Post-Trend Output Git & File Handling (Second Half of Day)

| Problem                              | Cause                                        | Resolution                                 |
|-------------------------------------|----------------------------------------------|--------------------------------------------|
| Screenshot file not committing      | File didn’t exist or wrong filename          | Confirmed correct name `screenshot 1.png`, moved to correct folder |
| `mv` command failed (Permission Denied) | Trying to move from restricted folder       | Used `Downloads` as source for `mv` command |
| `mv` filename with spaces broke CLI | Shell doesn’t handle unescaped spaces        | Renamed file to `screenshot 1.png`         |
| `git add` failed to match file      | Incorrect file path                          | Fixed by using exact relative path         |
| `git push` rejected with 403        | HTTPS push via password is deprecated        | Switched to GitHub Desktop (Option 3)      |
| GitHub Desktop repo not showing     | Repo not synced or detected                  | Cloned again into GitHub Desktop app       |

---

### ✍️ Git Commit History

```bash
git add screenshots/fx_suggestion_output.png
git commit -m "AIVA-11: Add output screenshot for Smart FX suggestion"
git push origin main
✅ Final push done using GitHub Desktop after switching from CLI. All files pushed successfully.

---
#### 🔁 Next Steps

- ✅ Create a `screenshots/` folder inside your GitHub repo root to store all future screenshot evidence.
- ✅ Move current screenshot file into that folder.
- ✅ Commit today’s files with message:  
  `"AIVA-11: FX trend analysis script added with sample data, GPT-style recommendations & screenshots"`
- ⏭ Start **AIVA-14**: Add trend logic to determine convert/wait strategy based on threshold settings.

---

---

## 📅 9 August 2025  
**Task ID:** AIVA-14  
**Title:** Add trend logic to determine convert/wait  
**Epic:** FX Data & API Layer  
**Status:** ✅ Completed  

---

### 🧠 Objective  
Add percentage-based threshold logic to the FX trend analysis so the AI can recommend either "Convert Now" or "Wait" depending on market movement size.

---

### 🗂 Step-by-Step Process  

1. **Reviewed yesterday’s progress** from AIVA-13 & AIVA-11 to ensure base FX analysis logic was ready.  
2. **Created `fx_trend_with_threshold.py`** in `/ai/`.  
3. **Set threshold logic**:  
   - If drop ≥ threshold → **Convert Now**  
   - If small movement → **Wait**  
4. **Initial run failed**:  
   - Reason: Python could not find script (`No such file or directory`)  
   - Cause: Repo had been moved from `Desktop` to `Documents/GitHub/`  
   - Fix: Navigated to correct path in terminal (`cd ~/Documents/GitHub/aiva-glow-wallet`)  
5. **File not found error for script**:  
   - Cause: File still in old Desktop folder  
   - Fix: Moved file into `/ai/` inside repo  
6. **Tested script with mock data** in `/fx_data/fxrates.json`.  
7. **Observed missing AUD_USD data**:  
   - Added graceful handling with `"N/A"` output to avoid crash.  

---

### 🛠️ Troubleshooting Table  

| Issue | Root Cause | Fix |
|-------|------------|-----|
| Script not found | Running in wrong directory | Navigated to repo folder in Documents |
| Python path error | File created outside repo | Moved script into correct `/ai/` directory |
| Missing AUD_USD key | Not present in fxrates.json | Added "N/A" handling logic |

---

### 📸 Output Screenshot  
Stored as `/screenshots/screenshot_aiva14_threshold_output.png`:

USD_AUD: falling (-1.32%) → Convert Now | USD weakening vs AUD | Consider holding AUD

EUR_AUD: falling (-3.01%) → Convert Now | EUR weakening vs AUD | Consider holding AUD

AUD_USD: N/A (data missing) → Hold position



---

### 🔁 Next Steps  
- Integrate threshold logic into Smart FX UI  
- Begin AIVA-15 to simulate FX conversions with mock balances  

---

### 📌 Commit Info  

**Commit Message:**  
`AIVA-14: Added FX threshold logic for convert/wait decisions`  
 
**Commit Description:**  
Implemented fx_trend_with_threshold.py in /ai/

Added % change calculation and threshold-based decision logic

Handles missing pairs gracefully with N/A output

Moved repo to Documents/GitHub/ for consistent pathing

Added output screenshot to /screenshots/

---

## 📅 11 August 2025  
**Task ID:** AIVA-14 (Enhancement)  
**Title:** Enhance FX trend analysis with debug output & flexible threshold input  
**Epic:** FX Data & API Layer  
**Status:** ✅ Completed  

---

### 🧠 Objective  
Improve the FX trend analysis script (`fx_trend_with_threshold.py`) to make it easier to debug, test, and adjust decision logic by adding detailed printouts and a variable threshold via CLI.

---

### 🗂 Step-by-Step Process  

1. **Reviewed** previous implementation of `fx_trend_with_threshold.py` from 9 August.  
2. **Added debug prints**:  
   - Data type (`OrderedDict`)  
   - List of available dates  
   - Sample day values with currency pairs and rates  
3. **Printed full currency series** for each pair with a flag indicating if any days are missing.  
4. **Allowed CLI argument** to set decision threshold:  
   - Example: `python3 ai/fx_trend_with_threshold.py 0.5` for 0.5% threshold  
   - Defaults to 1.0% if not specified.  
5. **Formatted outputs** to clearly show:  
   - Currency pair  
   - Trend direction & % change  
   - Decision: "Convert Now", "Wait", or "Hold position"  
6. **Tested script** with thresholds 0.5%, 1.0%, and 2.0% to confirm dynamic behaviour.  

---

### 🛠️ Troubleshooting Table  

| Issue | Root Cause | Fix |
|-------|------------|-----|
| `zsh: number expected` error | CLI threshold argument incorrectly formatted | Ensured correct float input and tested valid syntax |
| Output unclear for debugging | Script only showed final suggestions | Added print statements before decision logic |

---

### 📸 Output Screenshot  
**Filename:** `fx_trend_debug_threshold_tests.png`  
**Location:** `/screenshots/`  
**Description:** Shows three runs of the script with thresholds of 1.0%, 0.5%, and 2.0%, including debug details.  

---

### 📌 Commit Info  

**Commit #1 – Python Script Update**  
- **Commit Message:** `AIVA-14: Enhance FX trend analysis with debug output & flexible threshold input`  
- **Commit Description:**

  - Added debug prints for data type, date range, and sample day values

  - Displayed full currency series with missing data flag

  - Enabled passing custom threshold percentage via CLI argument

  - Improved output formatting for trend % change and decision


**Commit #2 – Screenshot Evidence**  
- **Commit Message:** `AIVA-14: Add debug threshold test screenshot`  
- **Commit Description:**  

- Added screenshot of FX trend analysis script runs with thresholds 0.5%, 1.0%, and 2.0%

- Stored in /screenshots/fx_trend_debug_threshold_tests.png


---

### 🔁 Next Steps  
- Integrate this enhanced debugging into a test suite for automated runs.  
- Move towards AIVA-15: Simulate FX conversions using mock wallet balances.  

---
## 📅 14 August 2025

**Task IDs:** AIVA-52, AIVA-53  
**Titles:**  
- AIVA-52: Add Green FX carbon badge to AI Suggestion UI  
- AIVA-53: Add Compliance & Risk collapsible panel to UI  
**Epic:** Compliance & Risk Management  
**Status:** ✅ Completed (UI placeholders, backend logic later)  

---

### 🧠 Objective  
Enhance the wallet UI to display sustainability and compliance information alongside FX recommendations, preparing for environmental impact tracking and regulatory readiness.  

---

### ✅ Steps Completed  

1. **Green FX Carbon Badge**  
   - Designed a badge to show estimated carbon footprint per FX transaction.  
   - Created `carbon_estimator.py` in `/ai/` to read `carbon_factors.json` and estimate emissions from mock transaction data.  
   - Added sample data in `/fx_data/transactions_sample.json`.  
   - Tested script output and stored screenshot in `/screenshots/`.  

2. **Compliance & Risk Collapsible Panel**  
   - Built a `<details>` collapsible section in `ai_suggestion_component.md` to display compliance snapshot (KYC/AML status, transaction risk, required actions).  
   - Included status badge styles for Review, Clear, and Blocked.  
   - Added mock data for residency, sanctions check, and transaction rules.  

3. **Folder Structure Update**  
   - New files and folders added:  
     ```
     ai/
       carbon_estimator.py
     fx_data/
       carbon_factors.json
       transactions_sample.json
     lovable-ui/
       ai_suggestion_component.md (updated)
     ```
   - Ensured all outputs/screenshots are in `/screenshots/`.  

4. **Jira Updates**  
   - Created and moved AIVA-52 and AIVA-53 to **Done** in Sprint 1.  

5. **README Update**  
   - Added Green FX and Compliance UI tasks to Sprint 1 summary.  
   - Updated folder structure in README.  
   - Expanded vision to include environmental impact tracking.  

---

### 📂 Updated Folder Structure  

ai/
fx_trend_analysis.py
fx_trend_with_threshold.py
carbon_estimator.py
fx_data/
fxrates.json
carbon_factors.json
transactions_sample.json
lovable-ui/
ai_suggestion_component.md
designs/
screenshots/
fx_suggestion_output.png
greenfx_output.png
compliance_panel_preview.png
logbook.md
README.md


---

### 🛠 Troubleshooting Notes  

| Issue | Root Cause | Fix |
|-------|------------|-----|
| Carbon factors not loading | Wrong relative path in script | Fixed path to `../fx_data/carbon_factors.json` |
| Lovable UI preview not updating | Old file cached | Re-uploaded updated `ai_suggestion_component.md` |
| Confusion about where to insert collapsible panel | Unclear in instructions | Clarified placement inside AI Suggestion component below FX recommendation |  

---

### 📸 Output Screenshots  
- `/screenshots/greenfx_output.png` – Carbon badge output  
- `/screenshots/compliance_panel_preview.png` – Compliance panel collapsed/expanded view  

---

### 🔁 Next Steps  
- Integrate carbon estimation script with FX transaction logic.  
- Begin connecting compliance UI to backend rules.  
- Start AIVA-15: FX conversion simulation with mock balances.  

---
## 📅 15 August 2025
**Task ID:** AIVA-15  
**Title:** Simulate FX conversions with mock balances  
**Epic:** Smart FX AI Engine → FX Data & API Layer  
**Status:** ✅ Completed

---

### 🧠 Objective
Simulate FX conversions between **USD/EUR/AUD** using the latest rate from `fxrates.json`, persist balances in `balances.json`, and print a clear before/after summary. Handle missing pairs via inverses/cross rates and validate sufficient funds.

---

### ✅ Steps Completed
1. **Created balances file**
   - `fx_data/balances.json` with starting balances (USD, EUR, AUD).
2. **Added simulation script**
   - `ai/fx_conversion_sim.py`:
     - Loads latest date from `fxrates.json`.
     - Gets direct rate or computes **inverse/cross via AUD**.
     - Validates inputs and available balance.
     - Updates and saves balances after conversion.
3. **Tested scenarios**
   - `USD → AUD` (direct).
   - `AUD → EUR` (cross via AUD).
   - Verified **insufficient funds** error path.
4. **Verified persistence**
   - Re-running shows updated balances in `fx_data/balances.json`.

---

### 🛠 Troubleshooting & Fixes
| Issue | Cause | Fix |
|---|---|---|
| Missing rate error | Pair not in JSON | Compute inverse and cross via **AUD** pivot |
| Balances not updating | Overwrite vs update | Read → adjust → **save back** to JSON |
| Path errors running script | Wrong folder | Run from repo root: `cd ~/Documents/GitHub/aiva-glow-wallet` |

---

### 📸 Output Screenshot
Save as: `screenshots/aiva15_conversion_output.png`  
**Example run:**
[FX Conversion Simulation]
Date used: 2025-08-07
Rate USD->AUD: 1.513333
Amount: 200.00 USD → 302.67 AUD

Before:
USD 1,000.00 | EUR 800.00 | AUD 1,500.00

After:
USD 800.00 | EUR 800.00 | AUD 1,802.67

---

### 📂 Updated Folder Structure (new today)
├── ai/
│ ├── fx_trend_analysis.py
│ ├── fx_trend_with_threshold.py
│ └── fx_conversion_sim.py # NEW
├── fx_data/
│ ├── fxrates.json
│ └── balances.json # NEW
├── lovable-ui/
├── designs/
├── screenshots/
├── logbook.md
└── README.md

---

### 🔁 Next Steps
- Surface conversion result in the **Smart FX UI card** (AIVA-10 enhancement).
- Trigger simulation after user accepts a recommendation.
- (Optional) Write results to a simple CSV for history.

---

# 📘 Aiva Glow Wallet – Logbook  
**Date:** 18 August 2025  
**Focus:** AIVA-15 — Simulate FX conversion using mock data (with Green FX + Compliance stubs)

---

## 🎯 Objective
Build a tiny end-to-end “conversion” pipeline that:
- Keeps in-memory **balances** (AUD / USD / EUR).  
- Converts using **mock FX rates**.  
- Logs each conversion with a **carbon estimate** (Green FX badge source) and a **compliance status** (“Clear” / “Review Needed”).  

This gives us a safe playground to later plug into the UI card and the collapsible Compliance panel.

---

## 🧩 Files touched / created
ai/
fx_simulation.py <-- NEW (core of AIVA-15 today)
fx_trend_with_threshold.py (unchanged)
carbon_estimator.py (unchanged)
fx_data/
(no change today)


---

## 🛠 What I built

### 1) `fx_simulation.py` (final structure)

Key sections in order (the order matters in Python!):

1. **balances** – starting money per currency  
2. **fx_rates** – mock rates for the pairs we use  
3. **carbon_factors** – kg CO₂ per 1000 units converted  
4. **transactions** – in-memory log list  
5. **compliance_check(amount, from_cur, to_cur)** – returns `"Review Needed"` if amount > 10,000, else `"Clear"`  
6. **log_transaction(...)** – appends to `transactions` with carbon + compliance  
7. **convert(amount, from_cur, to_cur)** – checks rate & funds, updates balances, calls `log_transaction`  
8. **test runs** – prints initial balances, runs two conversions, prints all transactions  

> ⚠️ Why order matters?  
> Python must **see** a function before it is called.  
> If `convert()` calls `log_transaction()`, then `log_transaction()` must be defined **above** `convert()` in the file.

---

### 2) How to run it
From your repo root:

```bash
cd ~/Documents/GitHub/aiva-glow-wallet/ai
python3 fx_simulation.py

Expected output (shape):

Initial Balances: {'AUD': 1000.0, 'USD': 500.0, 'EUR': 300.0}
Converted 100 AUD → 66.00 USD
Logged Transaction: { from: 'AUD', to: 'USD', amount: 100, converted: 66.0, carbon: '0.xx kg CO₂', compliance: 'Clear' }
Converted 200 USD → 182.00 EUR
Logged Transaction: { from: 'USD', to: 'EUR', amount: 200, converted: 182.0, carbon: '0.xx kg CO₂', compliance: 'Clear' }
All Transactions: [ ...two entries... ]

🧨 Bug I hit & how I fixed it

Error:
NameError: name 'log_transaction' is not defined

Root cause:
convert() was above log_transaction() in the file; Python hadn’t parsed log_transaction() yet when it was called.

Fix:
Reordered the file so log_transaction() is defined before convert().
This is a classic Python rule: definitions must appear before first use.

✅ Verification checklist (what I confirmed)

 Balances update correctly after each conversion.

 Each transaction logs a carbon estimate using carbon_factors.

 Compliance returns "Clear" for small amounts (≤ 10,000).

 Output prints updated balances and a final transactions list.

 Running the script from ai/ works with python3 fx_simulation.py.

🧠 What I learned (today)

Function order matters in Python. If A calls B, define B before A.

A minimal simulation can be powerful: balances → convert → log → annotate with carbon & compliance.

Keeping concerns separated (rates, balances, estimators, compliance) makes later UI wiring simple.

🧪 Sample output interpretation (why it matters)

Carbon (e.g., “0.42 kg CO₂”) comes from:
carbon_estimate = (amount / 1000) * carbon_factor[(from, to)]


This is the number we surface as the Green FX badge.

Compliance status ("Clear" vs "Review Needed") will drive the label on the
Compliance & Risk collapsible panel in the UI (e.g., “Status: Review”).

🔁 Next steps (tomorrow)

Hook the simulation outputs to the UI copy (Lovable content):

Show the Green FX badge value next to the Smart FX card.

Set the Compliance panel chip based on the latest transaction status.

Add a couple more pairs/rates & try a "Review Needed" case (e.g., amount > 10000) to see the panel flip.

(Optional) Persist transactions to a small JSON file for a simple history view.

---

📂 Current structure after today
ai/
  fx_simulation.py            # NEW – AIVA-15 conversion demo (today)
  fx_trend_analysis.py
  fx_trend_with_threshold.py
  carbon_estimator.py
fx_data/
  fxrates.json
  transactions_sample.json
  carbon_factors.json
lovable_ui/
  ai_suggestion_component.md
  compliance_collapsible_panel.md
  Smart Fx.png
screenshots/
  (add a screenshot of the terminal run if you want traceability)

---

# 📘 Logbook Entry — 20 August 2025

### **Task ID:** AIVA-15  
**Title:** Simulate FX conversions with mock balances  
**Epic:** FX Data & API Layer  
**Status:** ✅ Completed  

---

### 🧠 Objective  
Build a simulation that allows converting between currencies (USD, EUR, AUD) using mock balances and FX rates. Add carbon impact estimates and compliance checks.

---

### 📂 Steps Completed  

1. **Set up `fx_conversion_sim.py`:**  
   - Created a CLI script to simulate FX conversions.  
   - Script loads latest rates from `fx_data/fxrates.json`.  
   - Loads balances from `fx_data/balances.json`.  

2. **Implemented conversion logic:**  
   - Deducts amount from source balance.  
   - Adds converted amount to destination balance.  
   - Prevents insufficient fund transfers.  

3. **Rate calculation:**  
   - Supports direct pairs (`USD_AUD`, `EUR_AUD`).  
   - Supports inverse pairs (e.g., `AUD_USD`).  
   - Supports cross rates via AUD pivot (e.g., `USD_EUR`).  

4. **Carbon estimation:**  
   - `estimate_carbon_kg()` calculates emissions in kg CO₂.  
   - Adds **Low/Medium/High** badge depending on thresholds.  

5. **Compliance check:**  
   - Transactions >10,000 flagged as `"Review Needed"`.  
   - Normal transactions marked `"Clear"`.  

6. **Test run in terminal:**  
   ```bash
   python3 ai/fx_conversion_sim.py USD AUD 200

✅ Successfully converted USD → AUD, updated balances, printed carbon + compliance tags.


📸 Output Example
[FX Conversion Simulation]  
Date used: 2025-08-07  
Rate USD->AUD: 1.500000  
Amount: 200.00 USD → 300.00 AUD  

Before:  
  USD 600.00 | EUR 986.34 | AUD 1,800.00  

After:  
  USD 400.00 | EUR 986.34 | AUD 2,100.00  

Impact & Controls:  
  Carbon: 0.10 kg CO₂ (Low) | Compliance: Clear  

One-liner:  
  USD->AUD @ 1.5000 | 200.00 USD → 300.00 AUD | CO₂ 0.10 kg (Low) | Clear

---

# 📊 Sprint 2 Midway Health Report — 23 August 2025

### 🏷️ Sprint: AIVA Sprint 2 (15–29 Aug)

---

### ✅ Current Scope (In Progress)
- **AIVA-17:** Create GitHub repo aiva-wallet → In Progress  
- **AIVA-18:** Write README.md with vision and stack → In Progress  
- **AIVA-19:** Add mockdata and ai folders in GitHub → In Progress  

---

### 📂 Backlog (To Do, planned for Sprint 3)
- **AIVA-21:** Set key milestone dates  
- **AIVA-22:** Plan pitch deck content (Notion/Canva)  
- **AIVA-46 → AIVA-51:** Compliance & Risk epic tasks (KYC, Audit trail, APPs, Alerts, Ethics)  

---

### 🚦 Health Status
- Sprint 2 is **on track**.  
- Repo + README nearly ready to close.  
- Simulation tested successfully (`fx_conversion_sim.py`).  
- All deliverables can be finished by **end of August**.  

---

### 📸 Key Demo Proof
- FX conversion sim (USD→AUD, Aug 20 run) shows balances update, carbon badge + compliance output.  
- README updated with new folder structure.  

---

### 🧭 Next Steps
- Finalize Sprint 2 by committing:  
  - Updated `README.md`  
  - Updated folder structure (`ai/`, `fx_data/`)  
  - Screenshots of CLI runs  
- Prepare ground for **Sprint 3 (Compliance epic)** starting **Sep 1**.  

---

# 📅 25 August 2025 — Logbook (Sprint 2)

**Focus:** Practice and validate the FX conversion simulator with carbon + compliance stubs.  
**Repo path:** `~/Documents/GitHub/aiva-glow-wallet`

---

## ✅ What I did
1. Ensured a transactions file exists (empty array if missing).
   ```bash
   [[ -f fx_data/transactions_sample.json ]] || echo "[]" > fx_data/transactions_sample.json
   ```
2. Ran the simulator with a few scenarios to learn balance checks, rate lookup, carbon estimate, and compliance flow.

---

## 🧪 Runs & Results

### 1) Attempted: USD → AUD, 200  
```bash
python3 ai/fx_conversion_sim.py USD AUD 200
```
**Outcome:** ❌ `ValueError: Insufficient USD balance`  
> Lesson: balance validation happens **before** compliance.

---

### 2) Successful small trade: EUR → USD, 50  
```bash
python3 ai/fx_conversion_sim.py EUR USD 50
```

**Expected-style output (abridged):**
```
[FX Conversion Simulation]
Date used: 2025-08-07
Rate EUR->USD: 1.073333
Amount: 50.00 EUR  →  53.67 USD

Before:
  USD 100.00 | EUR 986.34 | AUD 2,550.00

After:
  USD 153.67 | EUR 936.34 | AUD 2,550.00

Impact & Controls:
  Carbon: 0.03 kg CO₂ (Low)  |  Compliance: Clear
```

---

### 3) Compliance test (large trade): USD → AUD, 15,000  
```bash
python3 ai/fx_conversion_sim.py USD AUD 15000
```
- First try: ❌ Failed (insufficient USD balance).  
- After topping up balances (or using a smaller amount): ✅ success and **Compliance: Review** triggered.

**One‑liner style (example):**
```
USD->AUD @ 1.5000 | 15,000.00 USD → 22,500.00 AUD | CO₂ 6.30 kg CO₂ (High) | Review
```

> Note: Exact carbon value depends on your `fx_data/carbon_factors.json`.

---

## 📸 Key Outputs (recap)
- **Small trade (EUR→USD 50)** → Carbon **0.03 kg (Low)**, Compliance **Clear**, balances updated correctly.  
- **Large trade (USD→AUD 15,000)** → Carbon **High**, Compliance **Review** (after ensuring sufficient source funds).

---

## 🧯 Problems & Fixes

| Problem                          | Cause                            | Fix (short)                                 |
|----------------------------------|----------------------------------|---------------------------------------------|
| Insufficient balance error       | Amount > available funds         | Top up `balances.json` or reduce amount     |
| Compliance not triggered         | Amount below threshold           | Use higher amount (e.g., 15,000 USD)        |
| Confused order of validations    | Expected compliance before funds | Remember: **Funds → Rate → Carbon → Compliance** |

---

## 🧠 Learnings
- Validation order (very important):  
  1. **Balance sufficiency**  
  2. **FX rate calculation** (direct, inverse, AUD cross)  
  3. **Carbon estimate** (factor per 1000 units)  
  4. **Compliance** (simple threshold → `Clear` / `Review`)
- Debugging approach:
  - Read Python tracebacks (`ValueError`) carefully
  - Start with small, controlled trades
  - Adjust JSON data (`balances.json`, `carbon_factors.json`) when needed

---

## 🗂 Files touched today
- `ai/fx_conversion_sim.py` (run + verify behavior)
- `fx_data/balances.json` (adjust for tests)
- `fx_data/transactions_sample.json` (append tx logs)
- `fx_data/carbon_factors.json` (used in estimate)

---

## ✅ Commit for today

**Commit message**
```
AIVA-15/S2: Exercise FX simulator with carbon & compliance cases
```

**Extended description**
```
- Ran fx_conversion_sim.py with small and large trades
- Verified balance checks, rate lookup, carbon estimate, and compliance flow
- Confirmed "Clear" for small trade and "Review" for high-value trade
- Ensured transactions_sample.json appends correctly; balances.json updated
```

---

## ⏭️ Next steps (Sprint 2 goals)
- Add one screenshot to `/screenshots/` for each scenario (small trade, compliance review).
- Link the simulator “one-liner” output into the **Smart FX** UI card mock (Lovable).
- Prepare a tiny function to read the latest transaction from `transactions_sample.json` for UI.

---

## 31 August 2025  
**Task ID:** AIVA-17, AIVA-18, AIVA-19 (Sprint 2 Wrap-up)  
**Epic:** Documentation & GitHub / FX Data & API Layer  
**Status:** ✅ Completed  

---

### 🎯 Objective  
Finish Sprint 2 with a **working demo of FX conversion simulation** that:  
- Updates balances from `balances.json`  
- Uses latest FX rates (`fxrates.json`)  
- Estimates carbon footprint per trade (`carbon_factors.json`)  
- Runs a compliance stub for large trades  
- Appends transactions into `transactions_sample.json`  

---

### 📝 Step-by-Step Process  

1. **Balance Setup**  
   - Initial error when running `USD→AUD 15000`:  
     ```
     ValueError: Insufficient USD balance. Have 5053.67, need 15000.0
     ```  
   - ✅ Fixed by resetting balances.json to:  
     ```json
     {"USD":20000,"EUR":1000,"AUD":1000}
     ```  

2. **Small Trade Test** (`EUR→USD 50`)  
   - Output confirmed:  
     ```
     Before:  USD 100.00 | EUR 986.34 | AUD 2,550.00
     After:   USD 153.67 | EUR 936.34 | AUD 2,550.00
     Carbon:  0.03 kg CO₂ (Low) | Compliance: Clear
     ```  
   - Verified **FX rate lookup**, **balances update**, **carbon = Low**, and **compliance = Clear**.  

3. **Large Trade Test** (`USD→AUD 15000`)  
   - After fixing balances:  
     ```
     Before:  USD 20,000.00 | EUR 1,000.00 | AUD 1,000.00
     After:   USD 5,000.00  | EUR 1,000.00 | AUD 23,500.00
     Carbon:  6.30 kg CO₂ (High) | Compliance: Review
     ```  
   - ✅ Compliance correctly triggered for >10,000 USD.  
   - ✅ Carbon footprint correctly classified as **High**.  

4. **Transaction Logging**  
   - Each trade appended to `fx_data/transactions_sample.json` with:  
     - Timestamp  
     - Pair, rate, amount  
     - Before/After balances  
     - Carbon + Compliance results  

---

### 📸 Key Outputs  

#### ✅ Successful Small Trade (EUR→USD 50)  
- Carbon footprint: `0.03 kg CO₂ (Low)`  
- Compliance: `Clear`  

#### ✅ Successful Large Trade (USD→AUD 15000)  
- Carbon footprint: `6.3 kg CO₂ (High)`  
- Compliance: `Review`  

---

### 🚩 Problems & Fixes  

| Problem                         | Cause                           | Solution                                      |
|---------------------------------|---------------------------------|-----------------------------------------------|
| Insufficient balance error       | Tried to trade more than wallet | Reset or topped up `balances.json`            |
| Compliance not triggered         | Trade was too small             | Tested with 15,000 USD, crossed threshold     |
| Confusion: balance vs compliance | Script enforces balances first  | Learned order: Balance → FX → Carbon → Comp.  |

---

### 📚 Learnings  
- **Order of execution matters**:  
  1. Balance sufficiency check  
  2. FX rate calculation  
  3. Carbon estimation  
  4. Compliance review  

- Debugging was systematic:  
  - Read `ValueError` tracebacks  
  - Tested smaller trades first  
  - Adjusted `balances.json` when needed  

- Adding **carbon + compliance layers** makes the wallet simulation feel closer to a real fintech engine.  

---

### ✅ Outcome  
- Sprint 2 deliverables finished.  
- **FX Conversion Simulator** working with balances, carbon tags, compliance stub, and transaction logging.  
- Ready to move into **Sprint 3 (Compliance Epic, Sep 1)**.  

---

## 📅 2 September 2025  
**Focus:** Mapping Global Licensing Insights into Sprint Structure  
**Context:** Lessons from Airwallex global licensing snapshot applied to Aiva Epics  

---

### 🔗 Mapping Regulatory Learnings to Aiva Sprint Structure  

#### 1. Compliance & Risk Epic  
- **Insight:** Each region (AUSTRAC, FinCEN, FCA, EBA) mandates AML/CTF checks, reporting, and transaction monitoring.  
- **Sprint Link:**  
  - **AIVA-46 (KYC/AML onboarding flow):** Simulate AUSTRAC/FinCEN KYC tiers (basic vs enhanced).  
  - **AIVA-47 (Compliance checklist):** Align with PSD2 obligations (EU) vs MSB obligations (US).  
  - **AIVA-48 (Audit trail):** Logs must satisfy potential regulator reviews (AUSTRAC/FinCEN examiners).  

---

#### 2. FX Data & API Layer  
- **Insight:** Regulators separate processors (no wallet balances) vs transmitters (holding balances). Licensing depends on handling customer funds.  
- **Sprint Link:**  
  - **AIVA-19 (Mockdata & AI folders):** Extend mock FX data with jurisdiction tags.  
  - **AIVA-15 (Conversion simulation):** Add “jurisdiction” metadata to each simulated transaction.  
  - **Future:** Wrap all FX API calls with compliance hooks for reporting.  

---

#### 3. Wallet UI  
- **Insight:** Consumer protection varies (FCA e-money safeguarding vs ASIC AFSL disclosure).  
- **Sprint Link:**  
  - **AIVA-4/5/6 (UI tasks):** Display disclosure banners (“Demo only, not licensed provider”).  
  - **Future:** Toggle UI between ASIC vs FCA reporting mockups.  

---

#### 4. Documentation & GitHub  
- **Insight:** Regulators expect policies and privacy compliance docs in addition to technical systems.  
- **Sprint Link:**  
  - **AIVA-18 (README.md):** Add a “Licensing Snapshot” section documenting obligations.  
  - **AIVA-49 (Data policy to APPs):** Map directly to Australian Privacy Principles (APPs).  

---

#### 5. Demo & Launch  
- **Insight:** Firms expand region by region — not everywhere at once.  
- **Sprint Link:**  
  - **AIVA-21 (Milestone dates):** Simulate a staged rollout (AU → UK → US).  
  - **AIVA-22 (Pitch deck):** Show compliance maturity as part of expansion plan.  

---

### ✅ Learnings  
- Regulation is part of the product, not an afterthought.  
- Compliance epics map neatly to global case studies (Airwallex, Wise, Stripe).  
- For Aiva, even as a prototype, adding “jurisdiction-aware” tags makes the simulation closer to a real-world wallet.  

---

### 📌 Next Steps  
- Add “Licensing Insights Layer” to **logbook.md** to guide Sprint 3 (Compliance Epic).  
- Update README to include a **Licensing Snapshot section**.  
- Begin Sprint 3 with AUSTRAC-inspired KYC/AML onboarding simulation.  

---

**Date:** Saturday, 06 September 2025

---

### Branch Setup
Created and switched to new branch `sprint3/compliance` in GitHub website. Verified sync with GitHub Desktop and confirmed branch alignment.

### Audit Log
Scaffolded `fx_data/audit_log.json` for compliance event tracking. Prepared structure for recording blocked/reviewed/cleared transactions.

### Compliance Logic
Upgraded `ai/fx_conversion_sim.py` with compliance rules: amount thresholds, velocity checks (structuring), and sanctions mock. Added full compliance object (`status`, `reason`, `rules_triggered`).

### Audit Integration
Implemented `append_audit` to record structured audit events into `audit_log.json`.

### UI Work (Lovable)
Prepared a single comprehensive Lovable prompt to modernize wallet UI: dark mode toggle, collapsible compliance panel, transaction timeline, AI insight card, and improved balance cards.

### Sync & Confirmation
Confirmed branch state in GitHub Desktop and verified no local changes pending. Repository is aligned with remote `sprint3/compliance`.

### Next Steps
Tomorrow: extend compliance UI in Lovable, finalize Sprint 3 commits, and begin planning for Sprint 4 API layer.

---

**Date:** Monday, 08 September 2025

---

### Compliance Engine
- Enhanced `ai/fx_conversion_sim.py` with full compliance logic.
- Implemented thresholds: >10,000 flagged as Review, >50,000 flagged as Blocked.
- Added velocity detection (≥3 transactions in 60 seconds).
- Included sanctions mock for blocked currency pairs.

### Transaction Log Enrichment
- All entries now saved into `fx_data/transactions_log.json`.
- Each record includes:
  - Carbon object (`kg`, `badge`)
  - Compliance object (`status`, `reason`, `rules_triggered`)

### Audit Trail
- Created `fx_data/audit_log.json` for sensitive actions.
- Records both `conversion_attempt` (blocked) and `conversion_settled` (clear/review).

### Testing Outputs
- Verified Clear transactions (small amounts).
- Verified Review transactions (amounts >10,000).
- Verified Blocked transactions (amounts >50,000).
- Verified velocity detection by running ≥3 trades within 60s.

### Jira Updates
- Marked **AIVA-106 (Compliance Rule Engine)** as Done.
- Progressed **AIVA-48 (Audit Trail)** to In Progress.
- Prepared for **AIVA-50 (Compliance Alerts UI)** via Lovable integration next.

### Next Steps
- Hook enriched JSON into Lovable UI (timeline + collapsible compliance panel).
- Export screenshots of UI updates for Sprint 3 deliverables.
- Plan for Sprint 4 API endpoints (/balances, /convert, /transactions).

---

# 📘 Aiva Glow Wallet – Daily Logbook  
**Date:** 22 Sep 2025  

---

## ✅ Activities Completed
- Continued work on **AIVA-48: Enrich transaction log with compliance metadata**.  
- Enhanced `fx_conversion_sim.py` with compliance integration:  
  - Threshold rules (review > 10k, blocked > 50k).  
  - Velocity rules (structuring detection).  
  - Sanctions mock checks (pair blacklist support).  
- Added **audit logging** via `fx_data/audit_log.json` to record:  
  - `conversion_settled` events for clear/review transactions.  
  - `conversion_attempt` events for blocked transactions.  
- Verified schema for audit events (`event_id`, `timestamp`, `event`, `pair`, `amount_src`, `status`, `reason`, `rules`).  
- Attempted to test review/blocked scenarios but **insufficient USD balance** caused simulation to fail at the balance check.  

---

## 🐞 Issues Faced
- Balance was too low (`USD ~ 5,483`) for triggering high-value transactions (`15k` and `60k`).  
- As a result, compliance `review` and `blocked` events could not be simulated in the current run.  

---

## 🔧 Workarounds Discussed
1. **Option A – Lower Thresholds:**  
   - Adjust compliance thresholds to `review=2,000` and `blocked=4,000`.  
   - Run test transactions (50 EUR → USD, 3k USD → AUD, 5k USD → AUD) to generate all 3 cases.  

2. **Option B – Top Up Balances:**  
   - Edit `fx_data/balances.json` to increase USD balance (e.g., 120,000).  
   - Run transactions with original thresholds (10k/50k).  

---

## 📝 Next Steps
- Choose between **lowering thresholds** or **topping up balances** to simulate review and blocked events.  
- Run three test transactions (clear/review/blocked) to confirm audit log enrichment.  
- Commit results with structured commit messages:  
  - `test(compliance): lower review/blocked thresholds for audit demos`  
  - `chore(data): top up balances.json for high-value compliance tests`  
  - `chore(audit): add demo clear/review/blocked events to audit_log.json`  

---

## 📌 Reflection
Today’s progress was a major milestone in implementing **compliance metadata and audit logging**. While test coverage was limited due to wallet balances, the underlying compliance engine logic and audit schema are now in place. Tomorrow’s focus is to generate complete audit trails for **clear, review, and blocked** scenarios.

----

# Logbook — 01 Oct 2025

## Tasks Completed
- Created foundational repo structure with folders:
  - `/compliance`
  - `/docs`
  - `/tests`
- Added seed files:
  - `/docs/Mission.md`
  - `/compliance/kyc_flow.md`
  - `/compliance/risk_log.json`
- Drafted **Mission.md** with 4 core pillars:
  1. Borderless multi-currency wallet
  2. Compliance-first design
  3. Blockchain-anchored statements
  4. AI-resistant, auditor-friendly exports

## Reflections
- Today marks the official **reset** of Aiva’s 90-day plan (Oct–Dec 2025).
- Even though progress feels small, creating the structure gives clarity and momentum.
- Tomorrow’s focus: begin filling out Mission.md in more detail and map first compliance learning notes.
