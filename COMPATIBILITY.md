# Compatibility

Bridge **0.0.6** targets public DSH **0.2.1-rc.2** with the narrow reviewed DS Bot Bridge contract. It requires `bridge.describe`, stable `bridge.submit`, and `bridge.redact`. Pristine npm DS Bot `0.1.7` lacks the complete contract and is intentionally rejected for unsupported operations.

A separately identified compatible DS Bot package is available through [Mobile App releases](https://github.com/MuQY1818/ds-bot-mobile-app/releases). Existing installations already exposing the required contract do not need another replacement. Updates must preserve the original team and be performed through the ordinary owner-controlled plugin process.

Supported transport includes Bot/group text history, full-message events, stable receipts, and explicitly declared model, usage, own-memory, schedule, queue and cancel capabilities. Token-level streaming, native approval/secret submission, media/voice, system push and group administration are not provided by this Bridge release.

The independent source extraction changes repository infrastructure and documentation only. It does not imply App Store, production, or physical-device acceptance. See [validation](docs/validation.md) and [provenance](docs/provenance.md).
