# Security

Bridge provides scoped device credentials to an existing computer-side DS Bot team. Its transport is intended for a trusted HTTPS endpoint or an owner-managed private network. It does not provision TLS, tunnels, accounts, or firewall rules.

Do not post credentials, pairing material, private messages, state archives, or exploitable vulnerability details in public issues. Use GitHub's private vulnerability reporting when available in the repository Security tab. If private reporting is unavailable, open a minimal issue requesting a private contact without disclosing the vulnerability.

Keep Bridge state in its own long-lived absolute directory. Restrict filesystem access to that directory, use the same state directory when upgrading, and revoke lost devices through the authenticated computer owner interface. Stop an old Bridge instance before starting another against the same directory or port.

Only declared capabilities are available to devices. Owner pairing and revocation use the authenticated DSH carrier, while device endpoints use separate scoped credentials. The compatibility and rejection tests exercise these boundaries; they are not a full security audit. See [the security model](docs/security.md).
