# Attach and Authorize

Registered isn't the same as usable. Many servers need authorization - and the
credential should be held **centrally**, never written into the sandbox.

## Check authorization status

```bash
sbx mcp auth status
```

`remotedhi` shows `not authorized`. Fix that:

```bash
sbx mcp auth remotedhi
```

The hosted control plane runs OAuth and holds the credential. The sandbox never
sees it - same credential-isolation idea as Contain, now for tools.

## Attach it as a locked set

```bash
sbx run claude --static-mcp remotedhi
```

`--static-mcp` pins the kit: discovery is off, so the agent can use **only** the
servers you chose. That's the governed posture - you decide exactly which tools
go in the box.

> [!NOTE]
> Leave off `--static-mcp` for the experimentation posture: the agent can search
> the registered catalog and add servers itself.

Next: watch the agent actually use it.
