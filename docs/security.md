# Security model

A new device enters a pending pairing request. A computer owner must approve it before device credentials are issued. Pairing codes and claim material expire; losing access to a phone should be handled by revoking the device, not by posting or exporting its credentials.

Owner commands travel through the authenticated DSH carrier and enforce the owner principal and origin. Device transport uses separate credentials and visible conversation scope. Stable submission receipts prevent an accepted retry from producing another logical message; conflicting reuse of a request identity is refused.

The adapter uses explicit metadata projections, declared actions and the upstream known-value redaction contract. Group history is reconstructed from public room Sessions; hidden member Sessions are excluded and denied. This boundary does not grant arbitrary shell, approval, secret, memory-administration, or group-management powers.

Use HTTPS in normal operation. `devAllowInsecure` is for owned loopback fixtures only. Origin controls supplement authentication and do not replace it. Keep the dedicated Bridge home private and persistent across updates. See [configuration](configuration.md), [compatibility](../COMPATIBILITY.md), and [reporting](../SECURITY.md).
