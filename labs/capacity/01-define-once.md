# Declare the Sandbox Once

Everything you tuned across the earlier Cs can be captured in **one file**:
`sbxenv.yaml`. It declares the sandbox so `sbx env run` can recreate it anywhere.

## Read the declaration

```bash
cat sbxenv.yaml
```

```text no-run-button
name: product-catalog
agent: claude            # which agent runs
workspaces: [ . ]        # what it can see
secrets:
  anthropic:
    ref: anthropic       # brokered by the proxy, never written into the box
```

The sandbox is no longer a pile of flags you remember to type. It's **data** -
the agent, its workspace mounts, and its brokered secrets, all pinned. (The file
can also carry mixin `kits:` and declared `args:`.)

> [!NOTE]
> This is the same move as a Dockerfile or a Compose file: the environment stops
> being tribal knowledge and becomes a reviewable artifact.

Next: share it like code.
