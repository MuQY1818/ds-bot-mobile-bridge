# Validation scope

The independent repository retains the Bridge 0.0.6 runtime and existing test assertions. Verification is reported at the boundary exercised:

| Check | What it establishes |
| --- | --- |
| Source manifest | Runtime bytes match the recorded App source commit |
| Unit and SDK tests | Projection, authorization, receipts, client and action logic |
| Isolated integration | Real public DSH services with a reviewed DS Bot fixture and scripted model |
| Exact packed delivery | Install, enable, pairing, restart, revoke, disable and remove the exact archive |
| Production/device behavior | Requires separate evidence; not implied by tests above |

The pristine npm DS Bot 0.1.7 rejection is intentional. The reviewed fixture patch is installed only in the ignored test tree and is not bundled in Bridge. Tests do not contact a real model or use a user's profile. Local extraction verification on 2026-10-19 used Node.js 24.13.0:

- Clean `npm ci --ignore-scripts` and the independent `test:prepare` succeeded. Repeated preparation replaces only its owned downloaded source copies and is safe after a previous run.
- All **30 Bridge unit tests** and **30 SDK tests** passed; `oxlint --deny-warnings` passed.
- All **10 extracted runtime files** match the recorded source commit.
- The public DSH / reviewed DS Bot / scripted-model fixture passed **17 integration assertions**, including group attribution, hidden-session refusal, stable receipts, redaction, reconnection and scoped operations. Its two child services stopped cleanly.
- Local documentation links resolve, and the source allowlist/privacy audit reports no findings.

Exact package delivery is recorded separately after the committed archive is tested. The CI badge reports the configured GitHub workflow; no remote CI run or production installation is claimed by these local results.
