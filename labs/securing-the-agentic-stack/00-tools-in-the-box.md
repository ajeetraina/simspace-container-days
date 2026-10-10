# A Locked Box Needs Tools

**Contain** gave the agent a boundary. **Control** decided what it can reach. But
a sandbox that's safe and can't do anything is useless - the boxed agent still
needs **your tools**. In sbx, those tools arrive as **MCP servers** (kits).

In this lab the tool is the **Docker Hardened Images (DHI) MCP server**: a catalog
the agent can query to pick a minimal, signed, 0-CVE base image - *before* it
writes a single `FROM` line.

```text no-run-button
  agent in a box          DHI MCP kit
  "containerise this"  →  dhi_list_repositories
                          dhi_get_image_cves      → 0 critical / 0 high
                          dhi_get_image_attestations → SBOM + SLSA, signed
                       ←  "use dhi.io/node:24-debian13"
```

The agent talks to **one gateway**, the gateway talks to the servers, and that
chokepoint is where authorization and policy apply.

> [!NOTE]
> This is **Choice**, the third C: you bring your own agent, tools, and endpoints -
> safely, inside the box.

Next: register the DHI MCP server.
