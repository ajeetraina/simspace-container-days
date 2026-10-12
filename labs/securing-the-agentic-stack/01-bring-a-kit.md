# Bring a Mixin Kit: GitGuardian

A **mixin kit** stacks a capability into the box: a tool, its credentials, and its
network rules, as one signed artifact. We'll add **GitGuardian** - it installs
`ggshield` and wires it in as the agent's **AI hook**, so the agent's own actions
are scanned for hardcoded secrets automatically.

## Inspect the kit first

```bash
sbx kit inspect "oci://docker.io/ajeetraina777/gitguardian-kit@sha256:8a3ad30666e6e651e4fff3c56a16e715bff4ac5356512c7dcbaa47f97988e8c4"
```

```text no-run-button
  Name:           gitguardian
  Kind:           mixin
  Schema:         v2
  Display:        GitGuardian (ggshield) — Claude Code
  Policies:
    Network:      4 allow, 0 deny      (github.com, …, api.gitguardian.com)
    Credentials:  1 sources            (GitGuardian API key - held on the host)
    Environment:  1 variables
    Commands:     2 install, 0 startup
```

A mixin declares exactly what it adds - a network allowlist, one credential, and
its install commands. Nothing hidden.

## Attach it to the agent

```bash
sbx run claude --name demo --kit "oci://docker.io/ajeetraina777/gitguardian-kit@sha256:8a3ad30666e6e651e4fff3c56a16e715bff4ac5356512c7dcbaa47f97988e8c4" .
```

sbx pins kits **by digest** (it rejects plain `:tags` at consume time) - so you
run exactly the artifact you just inspected. Inside the box, `ggshield` is
installed and `GITGUARDIAN_API_KEY` is a **proxy-managed placeholder**: the real
key stays on the host and is injected by the proxy only on calls to
`api.gitguardian.com`.

> [!NOTE]
> Same credential-isolation idea as **Contain** - now for a tool's key. The
> scanner runs inside the box; its key never does.

Next: watch the kit catch a secret in the act.
