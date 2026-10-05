# Conclusion

## One agent, two blast radii

You opened this workshop with a row of horror stories - an agent that wiped a home
directory, one that erased years of photos, one weaponised to steal credentials, one that
ran a command nobody approved. Then you reproduced the shape of them yourself: a helpful
agent, running on your host with your rights, turning one ordinary request into real damage.

Then you changed one thing. Not the agent, not the prompt - the **environment around it**.
Inside an `sbx` microVM the same agent, given the same words, had nothing to leak and nothing
to destroy, because your host simply wasn't reachable from inside the box.

| | What the agent could reach | Outcome |
|---|---------------------------|---------|
| On your host | daemon, home dir, `~/.aws`, `~/.ssh`, tokens | secrets inventoried, home directory wiped |
| In the `sbx` sandbox | its own microVM only; host read-only | nothing to leak, nothing lost |

> [!IMPORTANT]
> You did not slow the agent down, take away its autonomy, or add a human back into the
> loop. You made the fast path and the safe path the same path.
>
> **The agent was never the problem. The absence of a boundary was.**

## The takeaway

Give coding agents a **boundary by default** - a sandbox with its own daemon and network, a
read-only view of the host, and no credentials it doesn't explicitly need. Least privilege at
authoring time, the same discipline you already apply to what runs in production.

## The rest of the story

This session was the short path - watch the harm, then box it. The full workshop goes
further with the same application: measuring an image with an SBOM, VEX and provenance,
migrating to a hardened base, signing it, and putting a CI gate at the dev-to-prod border -
plus wiring the sandboxed agent to a governed MCP server so it can only reach signed,
read-only tools.

Full hands-on version: <https://github.com/ajeetraina/simspace-agentic-security>

## Resources

| | |
|---|---|
| Docker Sandboxes (`sbx`) | <https://docs.docker.com/ai/sandboxes/> |
| Coding Agent Horror Stories (blog series) | <https://www.docker.com/blog/ai-coding-agent-horror-stories-security-risks/> |
| Docker Hardened Images | <https://docs.docker.com/dhi/> |
| Docker Scout | <https://docs.docker.com/scout/> |
| MCP Catalog | <https://hub.docker.com/mcp> |
| Product Catalog sample | <https://github.com/dockersamples/catalog-service-node> |
