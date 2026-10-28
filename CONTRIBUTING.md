# Enterprise Contribution & Commit Protocol

**Repository:** IMPERIAL Core architecture and U.S. HoldCo blueprint (public, documentation-first).

## Author and authority
- Founder: Alexander Romaskevich (RomaskevicH). The current human engineering team is one founder assisted by LLM-based tools.
- Preserve original code/document attributions, external upstream licenses and third-party dependencies.
- HANTER, VELION and Universal NCA are **technical architecture**, not independently appointed corporate directors or legal officers.

## Required procedure
1. Make one scoped change, describe it with a Conventional Commit title: `docs:`, `fix:`, `test:`, `security:`, etc.
2. Run `python3 -m unittest discover -s tests -v` and `python3 tools/verify_docs.py` locally when editing public documents.
3. Open a pull request with **why, scope, changed files, verified checks, risks and rollback**.
4. Ensure the GitHub Actions documentation job passes for the current SHA (where actions are enabled).
5. Do not describe E0 architectural design as E5/E6 runtime/production evidence.
6. Require explicit owner sign-off for releasing proprietary intellectual property or publishing a patent-sensitive implementation.
7. Never force-push or rewrite historical commits solely to polish their appearance; preserve truthful provenance.

## Current legal boundary
IMPERIAL Core, Inc. is a **proposed** Delaware legal entity. The proposal for 10 million authorized shares is not proof of company formation, shares issued, or personal ownership. The Universal NCA goal of up to 1 billion agent identities is an unverified engineering objective.

**CI success here only validates documentation hygiene, not the described software itself.**
