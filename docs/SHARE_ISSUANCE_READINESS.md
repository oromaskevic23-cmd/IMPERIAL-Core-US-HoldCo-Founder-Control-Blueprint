# IMPERIAL Core, Inc. — Shares and Founder-Control Execution Readiness

**Date:** 2026-10-24  
**Architect:** Alexander Romaskevich (RomaskevicH)  
**Status:** PROPOSED / LEGAL REVIEW REQUIRED / NO VERIFIED INCORPORATION OR ISSUANCE.  
**Public planning document only.** This is not a filed Delaware charter, share register, executed stock subscription, investor offer, patent, tax return or legal opinion.

> This GitHub project documents a possible corporate structure. It **does not establish that IMPERIAL Core, Inc. exists**, that the founder currently owns these shares, or that stock has been issued. Human corporate approvals and qualified counsel are prerequisites for legal action.

## 1. Proposed authorization

| Class | Proposed authorized shares | Ordinary votes per share | Proposed par/share |
|---|---:|---:|---:|
| Class B Founder Common | 8,000,000 | 10 | USD 0.00001 |
| Class A Common | 2,000,000 | 1 | USD 0.00001 |
| **Total** | **10,000,000** | | |

**Issuance concept (only after lawful formation):** 8m B to founder; initially zero A issued. Set aside a **planning earmark** of 1m currently unissued A for a future equity-incentive plan and 1m unissued A for possible investor transactions. Neither reserve represents an actual issue, grant, option or shareholder ownership. Options normally have no vote until valid exercise/issuance.

The proposed two-class charter **does not authorize Preferred Stock**. A preferred financing usually needs a lawyer-reviewed charter amendment, additional capitalization and negotiated stockholder rights. Ordinary voting percentages do not override statutory class voting, board fiduciary obligations, charter conversion rules or future investor rights.

## 2. Illustrative capitalization and founder control

| Scenario | Founder B issued (hypothetical) | Team A issued (hypothetical) | Investor A issued (hypothetical) | Class A still unissued | Founder economic share* | Founder ordinary voting |
|---|---:|---:|---:|---:|---:|---:|
| Present unverified legal state — no evidenced issue | 0 | 0 | 0 | 2,000,000 | N/A | N/A |
| Founder only, after legally valid issuance | 8,000,000 | 0 | 0 | 2,000,000 | 100% | 100% |
| Founder + 500k A to investors; team pool unissued | 8,000,000 | 0 | 500,000 | 1,500,000 | 94.1176% | 99.3789% |
| Founder + 1m A issued to team | 8,000,000 | 1,000,000 | 0 | 1,000,000 | 88.8889% | 98.7654% |
| Founder + 1m A team + 1m A investors | 8,000,000 | 1,000,000 | 1,000,000 | 0 | 80% | 97.5610% |

*Economic percentage presumes equal economics per Class A and Class B share, no Preferred Stock or other senior economic rights. These are planning scenarios, not current legal interests.*

**Ordinary votes** = Founder B × 10 / (all outstanding B × 10 + all outstanding A × 1). **Economics** = founder issued common / all issued common, conditional on equal class economic rights. Reserved but unissued shares are **excluded** from outstanding and voting share counts.

See the validated reproducible calculator in [equity_scenarios.py](../tools/equity_scenarios.py) and [its 12 math/denial tests](../tests/test_equity_scenarios.py). Execute:

    python3 -m unittest discover -s tests -v
    python3 tools/equity_scenarios.py --json

This script **cannot issue securities, mint tokens, create investors or execute corporate actions**.

## 3. Critical Delaware annual-cost warning

The [Delaware franchise-tax schedule](https://corp.delaware.gov/frtax/) and [8 Del. C. §503](https://delcode.delaware.gov/title8/c005/) provide an **Authorized Shares Method** and an **Assumed Par Value Capital Method**.

- With 10m authorized shares, a simple Authorized Shares Method illustration under the published bracket formula is **$250 + 999 × $85 = $85,165/year** in franchise tax, plus a separately stated **$50 annual report fee**. This is not a tax bill or final professional quote.
- The Assumed Par Value Capital Method may yield much less (published **minimum $400**) and depends on actual gross assets, issued shares and capital structure. One cannot responsibly promise the minimum in advance.
- Delaware corporations generally must file the annual report and franchise-tax payment by **March 1**, for the preceding period. Formation, registered-agent, bookkeeping, federal tax, legal and cross-border compliance expenses are **additional**. Neither par value nor a claimed $0 startup budget eliminates these obligations.

**Mandatory gate:** obtain an exact Delaware filing quote and accountant-modeled franchise tax under both methods **before** submitting any 10m-share dual-class incorporation.

## 4. Corporate action sequence — not yet completed

| Step | Missing legally operative evidence | Current status |
|---|---|---|
| Company name and agent | Delaware legal-name clearance, registered-agent agreement | NOT VERIFIED |
| Incorporation | Accepted/stamped Certificate of Incorporation and Delaware entity number | NOT VERIFIED |
| Class rights | Charter defines class counts, voting, economic rights, permitted transfers, conversion, any sunset | COUNSEL REVIEW REQUIRED |
| Organizational governance | Incorporator action, bylaws, lawful initial board appointment, board resolutions | NOT VERIFIED |
| Founder shares | Valid board approval, founder stock purchase/subscription agreement, lawful consideration, securities exemption | NOT VERIFIED |
| Share ownership | Official company stock ledger with valid issue date and share class | NOT VERIFIED |
| Founder tax decision | Restricted vs unrestricted shares, cross-border tax review; §83(b) election if applicable | NOT VERIFIED |
| Team pool | Equity plan authorization, Rule 701 review, grants, foreign employment and tax review | NOT VERIFIED |
| Investor round | Approved terms and correct Preferred/SAFE mechanics; necessary charter amendments | NOT VERIFIED |
| IP transfer | Chain of title and approved, signed assignments/licenses for specifically listed assets | NOT VERIFIED |
| Operational tax | EIN, Form 1120, any Form 5472, Ukrainian CFC duties where applicable | NOT VERIFIED |

The IRS generally requires a relevant [§83(b) election / Form 15620](https://www.irs.gov/pub/irs-pdf/f15620.pdf) within **30 days of a transfer of restricted property**, not 30 days after incorporation; an unrestricted founder issuance may not require it. U.S.–Ukraine tax residency and reporting must be evaluated individually before an issuance or assignment.

## 5. Counsel decision register

1. **Charter:** Is 8m B / 2m A, 10:1 high-vote, equal economic rights the right **legal and investor-compatible** structure? Should high-vote rights convert on transfer, death, ownership thresholds, or time-based sunset?
2. **Founder consideration:** How should historical code and other work be valued, retained, licensed or transferred, and are founder shares restricted/reverse-vested? Do not assume $80 aggregate par value is enterprise valuation or the correct taxable price.
3. **Fundraising:** Will the planned investor allocation require Preferred Stock, additional shares, board seats, special votes or a SAFE conversion reserve? Do not promise that 1m Common A shares suffice for an institutional round.
4. **Staff equity:** Does a 1m A incentive pool make sense before hiring, and what rights/conditions and cross-border tax rules apply?
5. **Governance:** Who lawfully appoints the initial board/officers and who can approve shares, changes to voting rights, subsidiary formation and IP moves? Technical owner permissions do not override directors' duties or shareholder rights.
6. **Regulatory and geographic status:** Confirm corporate availability, SEC/state exemption, Ukrainian residency and CFC notification, Delaware/federal recurring expenses before taking any action.

## 6. Hard separation from crypto and AI agents

NDB, IMPERIUM, MONARCH, NZT, LISA, SALMAN and wallet balances are **not Class A or B corporate shares**. No automated transfer of tokens, treasury or private IP is authorized. Universal NCA, HANTER, VELION, CONSTRUCTOR AI and CYBER HAK are technical/project components, not stockholders by default.

**Deny by Default:** No AI agent may create issued shares, corporate ownership records, investor promises, signed approvals, securities sales, tax elections or Delaware filings merely because a GitHub planning file exists. Keep real corporate minutes, identities, tax identifiers, contracts and shareholder ledgers in a controlled legal repository, **not public GitHub**.

### Source of legal structure

- [Original fuller US HoldCo equity model](US_HOLDCO_EQUITY.md)
- [Corporate structure](CORPORATE_STRUCTURE.md)
- [Delaware DGCL §151 stock classes](https://delcode.delaware.gov/title8/c001/sc005/)
- [Delaware DGCL §212 voting rights](https://delcode.delaware.gov/title8/c001/sc007/)
- [Delaware franchise tax](https://corp.delaware.gov/frtax/)
- [IRS Form 15620 instructions](https://www.irs.gov/pub/irs-pdf/f15620.pdf)

**Completion rule:** the *engineering math/checklist* may pass automated tests, but the *shares* are **not complete** until proper corporate formation, approvals, consideration, securities compliance and executed stock ledger are independently evidenced.
