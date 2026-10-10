# Allow and Deny

Two rule types sit on top of the profile: **allow** opens a host, **deny** closes
one - and deny always wins.

## Allow the internal service

```bash
sbx policy allow network inventory.internal
```

Rule added, globally. Re-check and watch the decision flip:

```bash
sbx policy check network inventory.internal:8080
```

`ALLOW` now - the agent can reach exactly what you decided, and nothing else new.

## Block a known-bad host

```bash
sbx policy deny network telemetry.vendor.example
```

Deny takes precedence over any allow, so even a broad allow rule can't re-open it -
a simple way to stop a known exfiltration target.

> [!NOTE]
> Rules are global by default; add `--sandbox demo` to scope a rule to one
> sandbox instead of all of them.

Next: see every decision in the log.
