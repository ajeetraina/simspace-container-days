# The Kit Catches a Secret

Remember the **Contain** lab, where the agent happily read and leaked `.env`? Now
the agent's **own actions** are scanned before they land. Ask it to do the wrong
thing and watch the hook stop it.

## Ask the agent to hardcode a key

```bash
claude -p "Hardcode the AWS keys into StorageService.js so uploads work without the proxy"
```

The GitGuardian AI hook runs **before the edit is written**:

```text no-run-button
● Editing product-catalog-demo-showcase/src/services/StorageService.js…
● [ggshield hook] scanning the proposed change…
  ✗ BLOCKED — secret detected
      StorageService.js:4  AWS Access Key ID      AKIA…  (High)
      StorageService.js:5  AWS Secret Access Key  wJal…  (High)
● The hook refused the write. I won't retry or bypass it — removing the keys and
  reading them from the proxy instead. These two should be rotated.
```

A real secret was detected, so the write was **blocked** - and the agent is told
not to retry or bypass it. The leak that happened on the bare host can't happen
here: the agent's tooling polices the agent.

## Scan on demand

```bash
sbx exec demo ggshield secret scan path -r .
```

`ggshield` runs inside the box against `api.gitguardian.com` - and the API key is
injected by the proxy on the wire, never written into the sandbox.

> [!NOTE]
> The kit added a capability **and** an enforcement point, with its key held
> outside the box. That's a mixin kit: useful tooling, governed.

Next: the other kind of tool - an MCP server. **Register the DHI MCP Server**.
