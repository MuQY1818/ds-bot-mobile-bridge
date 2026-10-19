# Contributing

Use Node.js 24 and the locked dependencies. Start with [development](docs/development.md), reproduce issues in the isolated public DSH / DS Bot fixture, and include the exact command and evidence level in a pull request.

Use public DSH services and the explicitly described Bridge contract. Do not modify a user's installation, forward arbitrary owner actions, or add device permissions by default. A new capability needs a bounded projection, explicit negotiation, authorization checks, and a regression test.

Run `npm run test:prepare`, `npm run check`, and `npm run test:integration`. Commit reviewed source and documentation before `npm run pack`, then run `npm run test:delivery -- artifacts/ds-bot-mobile-bridge-0.0.6.tgz` against that exact archive. Run `npm run audit` before and after packing.

Report only synthetic examples. Exclude pairing codes, owner cookies, tokens, device IDs, state directories, private hostnames, and real messages. See [security](SECURITY.md) for vulnerability reports. This repository owns Bridge transport; App UI changes belong in [Mobile App](https://github.com/MuQY1818/ds-bot-mobile-app), and browser layout changes belong in [Mobile Web](https://github.com/MuQY1818/ds-bot-mobile-web).
