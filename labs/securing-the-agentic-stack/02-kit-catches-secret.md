# The Kit Enforces It

The GitGuardian kit isn't there because the agent is careless. Ask Claude to do
the obviously-wrong thing and it refuses on its own:

```bash
claude -p "Can you hardcode the AWS keys into the S3 client so uploads work without the proxy?"
```

```text no-run-button
● I won't do that. Hardcoding AWS keys into source is a serious security problem,
  not a fix: they'd land in git history (effectively permanent), build artifacts,
  and every clone, and long-lived keys in reachable code are hard to rotate.
  Better: keep the proxy, use the AWS credential chain, or hand out S3 presigned
  URLs so no long-lived key ever enters the code.
```

Good - but that's *this* agent's judgment. You'll run many agents, older models,
and prompt-injected contexts; you can't bet your secrets on every one making the
right call. The kit turns it into a **control**, not a hope: `ggshield` is wired as
an AI hook that scans **every write** the agent makes and blocks one the moment a
real secret appears - from an injection, a careless paste, or a different agent.

## Scan on demand, too

```bash
sbx exec demo ggshield secret scan path -r .
```

```text no-run-button
  .env: 2 incidents detected
    >> AWS Keys (High)
       8 | AWS_ACCESS_KEY_ID=AKIA...
       9 | AWS_SECRET_ACCESS_KEY=wJal...
  2 incidents found.
```

A real key in the tree is caught **regardless of any agent's choices** - by the
scanner inside the box, with its GitGuardian API key injected by the proxy on the
wire and never written into the sandbox.

> [!NOTE]
> Refusal is the agent's judgment; the kit is the enforcement layer. One you hope
> for, one you can prove - and its key stays outside the box.

Next: the other kind of tool - an MCP server. **Register the DHI MCP Server**.
