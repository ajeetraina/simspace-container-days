# Declare the Sandbox Once

Everything you tuned across the earlier Cs can be captured in **one file**:
`sbxenv.yaml`. It declares the sandbox so `sbx env run` can recreate it anywhere.

## Read the declaration

```bash
cat sbxenv.yaml
```

```text no-run-button
schemaVersion: "1"
name: product-catalog
agent: claude            # which agent runs
workspace: .             # what it can see
kits:                    # the GitGuardian scanner from Choice, pinned by digest
  - oci://docker.io/ajeetraina777/gitguardian-kit@sha256:8a3ad30…
secrets:
  gitguardian:
    ref: "op://Engineering/GitGuardian/api-key"   # a SOURCE, not a value
    snapshot: true
```

The sandbox is no longer a pile of flags you remember to type. It's **data** -
the agent, its workspace mount, its mixin `kits:`, all pinned.

Notice the `secrets:` block carefully: it never contains a **value**. It declares
a **source** - here a 1Password `ref:` - that each developer's `sbx env` resolves
**on their own host**. The repo carries *how to get* the secret, never the secret
itself.

> [!NOTE]
> This is the same move as a Dockerfile or a Compose file: the environment stops
> being tribal knowledge and becomes a reviewable artifact.

Next: share it like code.
