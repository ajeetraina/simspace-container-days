# Reproduce It Anywhere

This is the payoff. A new teammate clones the repo and runs **one command** - and
gets the exact sandbox you secured, down to the image digest.

## Step 1 - See the shared template

```bash
sbx template list
```

`product-catalog` is there, marked **shared** - available to anyone on the team.

## Step 2 - Reproduce the sandbox

```bash
sbx run --from sbx.yaml
```

Compare this to the ad-hoc run from the first section:

```text no-run-button
  before (ad-hoc)                 now (from sbx.yaml)
  local defaults, drifts     →    dhi.io/node:20-hardened, every time
  tools vary per machine     →    mcp: notion, pinned
  policy stays on your box    →    network: balanced, shared
```

Same image, same tools, same policy - **every developer, every run**. A new hire
is productive and governed in one command, with nothing to remember.

> [!NOTE]
> That's the full set. **Contain** gave the boundary, **Control** decided what it
> reaches, **Choice** put your tools inside it, and **Capacity** hands the whole
> thing to the team - reproducibly.

You've completed the 4 Cs. Run fast, without running wild.
