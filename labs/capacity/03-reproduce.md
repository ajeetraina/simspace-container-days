# Reproduce It Anywhere

This is the payoff. A new teammate clones the repo and runs **one command** - and
gets the exact sandbox you declared.

## Reproduce from the file

```bash
sbx env run
```

`sbx env run` reads `sbxenv.yaml`, creates the sandbox if it doesn't exist
(provisioning the brokered secrets), and attaches. Compare it to the ad-hoc run
from the first section:

```text no-run-button
  before (ad-hoc)                 now (sbx env run)
  local defaults, drifts     →    declared agent + workspace, every time
  secrets vary per machine   →    anthropic brokered from ref
  policy stays on your box    →   shipped in the repo
```

## Confirm it

```bash
sbx ls
```

The `product-catalog` sandbox is running - same agent, same workspace, same
brokered secrets, for **every developer and every run**.

> [!NOTE]
> That's the full set. **Contain** gave the boundary, **Control** decided what it
> reaches, **Choice** put your tools inside it, and **Capacity** hands the whole
> thing to the team - reproducibly.

You've completed the 4 Cs. Run fast, without running wild.
