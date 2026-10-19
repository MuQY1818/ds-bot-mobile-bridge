# Development

Use Node.js 24, npm, Python 3, Git, `tar`, and `patch`. No App checkout, phone, simulator, real model key, or user profile is needed.

```sh
npm ci --ignore-scripts
npm run test:prepare
npm run check
npm run test:integration
npm run audit
```

`test:prepare` installs the lockfile-pinned public DSH `0.2.1-rc.2` into ignored `fixture/deps`, verifies the published `ds-bot@0.1.7` archive integrity, and creates pristine and patched copies under `fixture/`. The reviewed group-contract patch is applied only to the downloaded fixture. It never patches DSH or an installed user package.

`npm test` checks adapters, authentication, groups, projections, and action boundaries. `npm run test:sdk` checks the portable client used by the fixture. `npm run lint` checks the Bridge and fixture JavaScript; `npm run check:source` verifies unchanged extracted runtime bytes. The SDK, mock, reviewed patch, and public harness lock are all included under `test-support/`, so the test suite has no sibling-repository dependency.

```sh
# Commit the reviewed change before creating an exact source-linked archive.
npm run pack
npm run test:delivery -- artifacts/ds-bot-mobile-bridge-0.0.6.tgz
npm run audit
```

The pack script enforces the explicit `package.json` file list and a clean source commit. It excludes tests, fixtures, SDK, mock, patches, CI, runtime state, and development dependencies from the plugin archive. Delivery creates a new isolated public DSH profile, installs the exact archive, and exercises the official manager, configuration, pairing, restart, revocation, disabling, and removal. Its model and WebSocket traffic are synthetic and its own child services are cleaned up.

An optional manual fixture can be started with `npm run fixture -- --keep`. Use only the ignored readiness file for its synthetic addresses. End that owned process to stop its services; do not use a live DSH profile for validation.
