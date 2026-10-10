# Share It Like Code

`sbx.yaml` is just a file in your repo. So it travels exactly like your source
does - through version control, review, and history.

## Step 1 - Stage and commit it

```bash
git add sbx.yaml
```

```bash
git commit -m "Add sbx.yaml - shared team sandbox"
```

The sandbox is now **versioned**. It can be reviewed in a pull request, rolled
back if someone loosens the network policy, and audited in the history.

## Step 2 - Push it to the team

```bash
git push
```

Every teammate who pulls now has the identical sandbox definition. The governance
you set - hardened base, pinned tools, locked-down network - ships with the repo
instead of living in one person's shell history.

> [!NOTE]
> Because policy is now in code, changing the boundary becomes a **reviewable
> event**, not a silent local tweak.

Next: reproduce it as a brand-new teammate.
