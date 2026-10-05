# What Harm Can It Do?

The agent just built your image. It ran on your host, with your rights, and nothing scoped
it. The horror stories from the talk were all exactly this situation - a helpful agent, full
access, one ordinary request. Let's reproduce two of them.

> [!WARNING]
> These are **simulated** in the lab terminal - nothing on your real machine is touched. On
> an unsandboxed host, the commands below would do precisely what the output shows.

## 1. What can it reach?

First ask the agent what it can see from where it's running:

```bash terminal-id=main
claude -p "What files and credentials can you read on this machine?"
```

Read the list. The agent isn't doing anything clever or malicious - it's just enumerating
what's *there*. Your Docker socket. Your AWS credentials. Your unencrypted SSH key. Your
GitHub token. A production `.env` with a database password. It runs as you, so it reads what
you can read.

This is the **secrets-leakage** horror story (the poisoned Nx package). The attacker never
needed to steal your keys directly - they just needed your agent, which already had them in
reach, and a reason to look.

## 2. Ask it to do a chore

Now a completely normal request - the kind you'd actually type. Clean up the project:

```bash terminal-id=main
claude -p "Clean up my project folder - remove caches, build output and temp files"
```

Watch what happens. The agent builds an `rm -rf` to do the cleanup, the trailing `~/`
expands to your **entire home directory**, the Trash is bypassed, and `~/.aws`, `~/.ssh` and
years of files are gone - unrecoverably.

This is the **filesystem** horror story. You approved *"clean up."* You did not approve this.
Nothing between the agent and your disk said no, because there was nothing there at all.

## The common thread

| Horror story | What the agent had | What one request became |
|--------------|--------------------|-----------------------|
| Secrets leaked | read access to your whole home dir | an inventory of every credential you own |
| Filesystem wiped | your user's delete rights, no scope | `rm -rf ~/` from *"clean up my project"* |

Both failures have the **same cause** and therefore the **same fix**. It isn't a smarter
prompt, a longer allowlist, or a human clicking *approve* faster. It's a **boundary** - so
that "what it can reach" is a short list you chose, not "everything you can reach."

That boundary is the next section.

Continue to **Put the Agent in a Box**.
