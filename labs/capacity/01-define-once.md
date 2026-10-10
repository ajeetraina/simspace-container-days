# Define the Sandbox Once

Everything you tuned across the earlier Cs - the hardened base, the pinned MCP
tools, the network policy - can be captured into **one file**: `sbx.yaml`.

## Step 1 - Capture the sandbox

```bash
sbx template save product-catalog
```

That writes `sbx.yaml` - a single, reviewable description of the sandbox.

## Step 2 - Read what it captured

```bash
cat sbx.yaml
```

Notice how the three earlier Cs are all pinned in one place:

```text no-run-button
image:   dhi.io/node:20-hardened   # Contain  - hardened, non-root base
mcp:     [notion]                  # Choice   - the tools, pinned
network: profile balanced + allow  # Control  - what it may reach
```

The sandbox is no longer a pile of flags you remember to type. It's **data** -
and data can be versioned, reviewed, and shared.

> [!NOTE]
> This is the same move as a Dockerfile or a Compose file: the environment stops
> being tribal knowledge and becomes an artifact.

Next: share it like code.
