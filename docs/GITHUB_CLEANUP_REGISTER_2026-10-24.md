# IMPERIAL Core — GitHub cleanup register and safe consolidation

**Inspection date:** 2026-10-24  
**Account:** `oromaskevic23-cmd`  
**Owner:** Alexander Romaskevich / RomaskevicH  
**Purpose:** Reduce portfolio clutter **without deleting important IP, code, Git history or private material**.  
**Evidence basis:** Repository listing and default-branch root directory inventories from the connected GitHub account, plus verified workflow evidence for CONSTRUCTOR AI. This is not a full content-duplication or secret audit.

## Verified inventory

- **23 repositories** accessible in the connected GitHub installation.
- **16 docs-only** repositories: root contains `README.md`, `ENTERPRISE_COMMIT_STANDARD.md`, and `ENTERPRISE_READINESS.md`, but no standalone runnable source tree checked at the root in this inventory.
- **7 structured/source repositories:** CYBER HAK, VELION public, AGY public, two third-party source forks, CONSTRUCTOR AI and this central public hub.
- **0 completely empty default branches.** Docs-only does not mean valueless or safe to delete. Several README files are hundreds of kilobytes.
- **0 repositories deleted in this maintenance pass.** The connected GitHub app has no delete/rename/archive repository action. A phone's authenticated GitHub browser session is not transferred to a separate automation browser.

### Current repository registry

| # | Repository | Visibility | Observed structure | Preservation / decision |
|---:|---|---|---|---|
| 1 | [`IMPERIAL-Core-`](https://github.com/oromaskevic23-cmd/IMPERIAL-Core-) | PRIVATE | DOCS_ONLY | Source-of-truth private architecture; KEEP |
| 2 | [`Repository-name-IMPERIAL-Core`](https://github.com/oromaskevic23-cmd/Repository-name-IMPERIAL-Core) | PRIVATE | DOCS_ONLY | Potential overlapping architecture; COMPARE before consolidation |
| 3 | [`HANTER`](https://github.com/oromaskevic23-cmd/HANTER) | PUBLIC | DOCS_ONLY | Possible overlap with HANTER-Public; KEEP until contents compared |
| 4 | [`Nano-Core-Agents`](https://github.com/oromaskevic23-cmd/Nano-Core-Agents) | PRIVATE | DOCS_ONLY | Private Universal NCA architecture; KEEP private |
| 5 | [`Enterprise-IMPERIAL-Skills`](https://github.com/oromaskevic23-cmd/Enterprise-IMPERIAL-Skills) | PRIVATE | DOCS_ONLY | Tiny 496-byte README; documents snapshotted privately, full Git history backup required before deletion |
| 6 | [`Codex-Enterprise-IMPERIAL-Skills`](https://github.com/oromaskevic23-cmd/Codex-Enterprise-IMPERIAL-Skills) | PUBLIC | DOCS_ONLY | Large public documentation; KEEP pending content deduplication |
| 7 | [`IMPERIAL-Core-Public`](https://github.com/oromaskevic23-cmd/IMPERIAL-Core-Public) | PUBLIC | DOCS_ONLY | Public umbrella brand documentation; KEEP as public guide |
| 8 | [`IMPERIAL-Engineering-Intelligence-`](https://github.com/oromaskevic23-cmd/IMPERIAL-Engineering-Intelligence-) | PRIVATE | DOCS_ONLY | Large private design content; KEEP |
| 9 | [`HANTER-Public`](https://github.com/oromaskevic23-cmd/HANTER-Public) | PUBLIC | DOCS_ONLY | Large public HANTER specification; compare with HANTER |
| 10 | [`Nano-Core-Agents-Public`](https://github.com/oromaskevic23-cmd/Nano-Core-Agents-Public) | PUBLIC | DOCS_ONLY | Public NCA specification; keep private/public boundary |
| 11 | [`Codex--PRIVATE-`](https://github.com/oromaskevic23-cmd/Codex--PRIVATE-) | PRIVATE | DOCS_ONLY | Private architecture; KEEP private |
| 12 | [`Legion-Public`](https://github.com/oromaskevic23-cmd/Legion-Public) | PUBLIC | DOCS_ONLY | LEGION concept docs; KEEP until product implementation |
| 13 | [`CRYPTO-IMPERIAL-Ecosystem-Public`](https://github.com/oromaskevic23-cmd/CRYPTO-IMPERIAL-Ecosystem-Public) | PUBLIC | DOCS_ONLY | Public blockchain/token architecture; KEEP, no live liquidity claims |
| 14 | [`ORION-Public`](https://github.com/oromaskevic23-cmd/ORION-Public) | PUBLIC | DOCS_ONLY | ORION architecture; KEEP |
| 15 | [`IMPERIAL-AGI`](https://github.com/oromaskevic23-cmd/IMPERIAL-AGI) | PUBLIC | DOCS_ONLY | AGI research/vision documentation; KEEP |
| 16 | [`CYBER-HAK-Public`](https://github.com/oromaskevic23-cmd/CYBER-HAK-Public) | PUBLIC | STRUCTURED_DOCS | Security architecture/agents/docs; NOT EMPTY |
| 17 | [`VELION-LLM-Public`](https://github.com/oromaskevic23-cmd/VELION-LLM-Public) | PUBLIC | STRUCTURED_DOCS | Legacy repo slug; public VELION architecture; KEEP links |
| 18 | [`AGY---PUBLIC-`](https://github.com/oromaskevic23-cmd/AGY---PUBLIC-) | PUBLIC | STRUCTURED_DOCS | Blockchain architecture and specification; KEEP |
| 19 | [`mirofish`](https://github.com/oromaskevic23-cmd/mirofish) | PUBLIC | UPSTREAM_SOURCE_FORK | Third-party fork with code and AGPL license; preserve attribution |
| 20 | [`lingbot-vla-v2`](https://github.com/oromaskevic23-cmd/lingbot-vla-v2) | PUBLIC | UPSTREAM_SOURCE_FORK | Third-party fork with code and Apache license; preserve attribution |
| 21 | [`CONSTRUCTOR-AI`](https://github.com/oromaskevic23-cmd/CONSTRUCTOR-AI) | PUBLIC | CODE_AND_CI | Own Task Manager + planning/quarantine code; 63/63 tests passed on 31122d4 |
| 22 | [`SHPAIZMAN-ORCHESTRATOR`](https://github.com/oromaskevic23-cmd/SHPAIZMAN-ORCHESTRATOR) | PUBLIC | DOCS_ONLY | Gift project specification; no installable product tree yet |
| 23 | [`IMPERIAL-Core-US-HoldCo-Founder-Control-Blueprint`](https://github.com/oromaskevic23-cmd/IMPERIAL-Core-US-HoldCo-Founder-Control-Blueprint) | PUBLIC | STRUCTURED_DOCS_CI | Canonical public founder/hub docs and validation workflow; KEEP |

## Practical consolidation priorities

**A — Preserve first (done for one limited source):** `Enterprise-IMPERIAL-Skills` is the smallest documentation-only private repository, with a 496-byte README. All three default-branch documents were copied **within the private GitHub boundary** to [private IMPERIAL Core preservation folder](https://github.com/oromaskevic23-cmd/IMPERIAL-Core-/tree/main/docs/consolidation/Enterprise-IMPERIAL-Skills). That private snapshot records the source HEAD and Git blob SHA for each file. **It is not a full mirror of history, issues, branches or settings, and therefore is not yet sufficient authorization to permanently delete the original.**

**B — Compare pairs without assuming duplicates:** `HANTER` vs `HANTER-Public`; `Nano-Core-Agents` vs `Nano-Core-Agents-Public`; `IMPERIAL-Core-` vs `Repository-name-IMPERIAL-Core`; `Enterprise-IMPERIAL-Skills` vs `Codex-Enterprise-IMPERIAL-Skills`. Similar names are only a review signal, not identical content; some pairs intentionally separate private and public information.

**C — Protect valuable work:** keep `CONSTRUCTOR-AI`, `CYBER-HAK-Public`, `VELION-LLM-Public` (canonical product name **VELION**), `AGY---PUBLIC-`, the founder hub, and both appropriately attributed third-party source forks. `SHPAIZMAN-ORCHESTRATOR` is a separate beneficiary project; do not mix permissions or ownership.

## Updated CONSTRUCTOR AI evidence

The earlier [Enterprise portfolio audit](ENTERPRISE_PORTFOLIO_AUDIT.md) recorded CONSTRUCTOR AI as README-only **before** the later implementation commits. That observation was a historical snapshot, **not its current state**. On 2026-10-24, the repository acquired Task Manager reference source, a gated model planning adapter, non-executing quarantine and automated tests. Exact commit `31122d4f0fed5149daa193c1005cee7a513f292c` completed [GitHub Actions run 40121553650](https://github.com/oromaskevic23-cmd/CONSTRUCTOR-AI/actions/runs/40121553650) with **63 tests passed, 0 failed**.

This means **E2 source and E3 offline automated verification for the current reference scopes**. It does **not** mean real Groq inference, arbitrary AI code sandbox, browser E2E or production-level compliance has been verified.

## Controlled deletion checklist

1. Export a complete `git clone --mirror` or `git bundle --all` to an independently held, access-controlled backup; verify references/branches/tags and restore path. Copying README files alone is **not a history backup**.
2. Examine issues, pull requests, releases, actions, deployment webhooks, package links and private/public exposure before deletion.
3. Compare nontrivial README and architecture material to its proposed canonical destination; migrate relevant content, preserving attribution, licenses and original timestamps/source commit references.
4. Search links and dependencies pointing to the old repo; where reasonable leave a redirect/archival README rather than delete outright.
5. If a repository is truly redundant and owner confirms, GitHub UI: **Settings → General → Danger Zone → Delete this repository**. This requires the owner's authenticated browser; connector access alone cannot perform it in this chat.
6. Update the registry after the actual deletion and verify the new total. Do not claim a deletion based only on a planned or prepared cleanup.

**Security principle:** Never transfer private repository content to a public consolidation destination. No secrets, proprietary code or nonpublic plans belong in public cleanup reports.

**Baseline before any deletion: 23 total / 16 docs-only / 7 structured or source / 0 truly empty.**
