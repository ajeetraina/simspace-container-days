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

## Load it into the running box

Our `demo` box already exists - it was created with the GitGuardian kit. A
sandbox's MCP set is normally fixed at creation (`sbx run claude --static-mcp
remotedhi` for a fresh, locked-down box), but you can also **hot-load** a server
into a box that's already running:

```bash
sbx mcp load remotedhi --sandbox demo
```

The agent sees the new tools immediately - a `tools/list_changed` notification, no
restart. The DHI catalog is now in the box alongside the GitGuardian kit.

> [!NOTE]
> `--static-mcp` at create time is the locked, governed posture; `sbx mcp load`
> adds a server to a live box. Either way the agent talks to one gateway, and
> authorization is held centrally.

Next: watch the agent actually use it.
