# A Locked Box Needs Tools

**Contain** gave the agent a boundary. **Control** decided what it can reach. But
a sandbox that's safe and can't do anything is useless - the boxed agent still
needs **your tools**. sbx has two distinct ways to put them in the box:

- **Mixin kits** - package tooling *into* the sandbox: a CLI, its credentials, and
  its network rules, as one signed artifact you pull from Docker Hub. Here, the
  **GitGuardian** kit, so the agent's own actions are scanned for secrets.
- **MCP servers** - external tool *servers* the agent calls through one governed
  gateway. Here, the **Docker Hardened Images (DHI)** server, so the agent picks a
  0-CVE base *before* it writes a single `FROM` line.

Two problems from Contain, two tools: the **kit** catches the secrets the agent
tried to leak; the **MCP server** fixes the CVEs it shipped. Different mechanisms,
same idea - give the boxed agent what it needs, with the credentials held outside.

> [!NOTE]
> This is **Choice**, the third C: you bring your own agent, tools, and endpoints -
> safely, inside the box.

Next: bring a mixin kit.
