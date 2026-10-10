# Read the Policy Log

Control isn't just rules - it's **visibility**. Every connection the agent tried,
allowed or blocked, is recorded with the rule that decided it.

## Read the log

```bash
sbx policy log
```

```text no-run-button
  HOST                       RULE                       DECISION
  api.anthropic.com          allow default (llm)        allowed
  registry.npmjs.org         allow default (dev)        allowed
  inventory.internal:8080    deny default               blocked   ← before your rule
  inventory.internal:8080    allow inventory.internal   allowed   ← after your rule
  telemetry.vendor.example   deny telemetry.vendor      blocked
```

You can see the agent trip over the default, your allow rule take effect, and the
deny rule stop exfiltration - all without trusting the agent to report it.

> [!NOTE]
> **Control** done. You decided what the agent may reach and proved it, rule by
> rule. Next pillar: **Choice** - giving the boxed agent the tools it needs.

You've completed Control.
