# Source provenance

This independent repository is extracted from [DS Bot Mobile App](https://github.com/MuQY1818/ds-bot-mobile-app) commit `92d9b452b49e8e52211015d11a3b1a93a38d4dfa`, directory `bridge/`, Git tree `2abbd0ef92cc6c08012ca8568c6a862c5269e5c7`.

All Bridge runtime files (`index.mjs` and `src/*`) are unchanged. [source-manifest.json](source-manifest.json) records their exact extraction hashes, enforced by `npm run check:source`. Package metadata points to the new repository; README files, test paths, independent fixture preparation, CI and packaging are repository maintenance changes. No user runtime state or local history is imported. The App repository retains its `bridge/` synchronization snapshot.

The included SDK is copied from the same commit's `packages/mobile-sdk/`; the reviewed fixture patch comes from `group-bridge/patches/ds-bot-0.1.7-groups.patch`; the scripted mock comes from `ds-bot/dev/mock-llm.mjs`. They remain development-only and are excluded from the release package. The lockfile in `test-support/harness/` pins only public npm dependencies for the isolated harness.

The original Bridge [NOTICE](../NOTICE) and Apache-2.0 [LICENSE](../LICENSE) remain. The ancestry includes QingJ01/DS-Bot-App commit `253407cf76062b2aa60bc5d039415aaa1c9867c4` and Fei2411's DS Bot `0.1.7`, with upstream source commit `939a6635830cb5b246e7dd19c67b0e1352ad1c07`. This community project is independent of DeepSeek.

Future synchronization must record its source commit and update the manifest deliberately. Do not treat the App snapshot as a separate device state or run both copies against the same Bridge home.
