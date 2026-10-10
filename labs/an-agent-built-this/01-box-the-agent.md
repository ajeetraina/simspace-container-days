# Box the Agent

One command puts the agent inside a **microVM** - its own kernel, filesystem, and
Docker daemon. The host is on the other side of the wall.

## Run the agent in a sandbox

```bash
sbx run claude --name demo
```

Read what it mounted - and what it didn't:

- **Workspace:** your project, mounted read-write at `/workspace`.
- **Host home:** mounted **read-only** at `/host` - your secrets are not copied in.
- **Credentials:** brokered by a proxy, never handed to the agent.
- **User:** `agent`, non-root.

## Confirm it's running and isolated

```bash
sbx ls
```

The `demo` sandbox is `running`, on the `claude` agent, scoped to your project
workspace.

> [!NOTE]
> A container shares the host kernel; a **microVM** brings its own. That's what
> lets the agent have a real Docker daemon inside without touching yours.

Next: prove the credentials never come inside.
