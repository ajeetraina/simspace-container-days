# The Agent Uses DHI

Here's the payoff. Hand the boxed agent the same "containerise this" task - but
now the DHI kit is in the box, so it asks the catalog *before* choosing a base.

## Run the agent with the kit

```bash
sbx run claude --static-mcp remotedhi -p "Containerise this service with a hardened base image"
```

Watch it query the DHI MCP server first:

- `dhi_list_repositories` → finds the hardened `dhi.io/node`
- `dhi_get_image_cves` → **0 critical · 0 high · 0 medium · 0 low**
- `dhi_get_image_attestations` → SBOM + SLSA provenance + VEX, signed by Docker

Then it writes a multi-stage Dockerfile on that base.

## See what it chose

```bash
cat Dockerfile
```

A distroless, non-root, 0-CVE base - picked by the agent because the tool was
there. Same prompt as an ungoverned run; a completely different result.

> [!NOTE]
> That's **Choice**: the box stays locked, but you decide which tools go inside -
> and the right tool steers the agent to a better outcome. Next pillar:
> **Capacity** - give the whole team this exact sandbox.

You've completed Choice.
