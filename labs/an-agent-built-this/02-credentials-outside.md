# Credentials Stay Outside

The agent needs to call real APIs - but it should never **hold** the keys. In a
sandbox, secrets live on the host and the proxy injects them on the way out.

## See where the secret lives

```bash
sbx secret ls
```

Your `anthropic` key is stored on the **host**, scoped globally, and injected
**by the proxy** - "never exposed to sandbox".

## Look for it inside the box

```bash
sbx exec demo printenv ANTHROPIC_API_KEY
```

Empty. The key isn't in the sandbox's environment.

```bash
sbx exec demo cat ~/.ssh/id_rsa
```

`No such file or directory` - host home is read-only and your secret files were
never copied in.

> [!NOTE]
> The agent still makes authenticated calls - the proxy adds the key as the
> request leaves the box. Usable credentials, zero raw keys inside.

Next: try to break out.
