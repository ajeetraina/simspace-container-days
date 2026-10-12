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
  Description:    Installs the GitGuardian CLI (ggshield) with proxy-injected API-key auth for api.gitguardian.com and wires it as a Claude Code AI hook, so the agent's own actions are scanned for hardcoded secrets automatically - the real key never enters the sandbox.

  Policies:
    Network:      4 allow, 0 deny
    Credentials:  1 sources
    Environment:  1 variables, 0 proxy-managed
    Commands:     2 install, 0 startup, 0 init files
```

A mixin declares exactly what it adds - a network allowlist, one credential, and
its install commands. Nothing hidden.

## Attach it to the agent

```bash
sbx run claude --name demo --kit "oci://docker.io/ajeetraina777/gitguardian-kit@sha256:8a3ad30666e6e651e4fff3c56a16e715bff4ac5356512c7dcbaa47f97988e8c4" .
```

sbx pins kits **by digest** (it rejects plain `:tags` at consume time) - so you
run exactly the artifact you just inspected. `--kit` only applies when **creating**
a sandbox; if a `demo` already exists, remove it first with `sbx rm demo` (or pick
a new `--name`). Inside the box, `ggshield` is installed and `GITGUARDIAN_API_KEY`
is a **proxy-managed placeholder**: the real key stays on the host and is injected
by the proxy only on calls to `api.gitguardian.com`.

> [!NOTE]
> Same credential-isolation idea as **Contain** - now for a tool's key. The
> scanner runs inside the box; its key never does.

Next: see the kit enforce it.
