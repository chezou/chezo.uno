---
title: How to Prevent gh CLI from Leaving a Plaintext Token on WSL2
subtitle: ''
summary: ''
date: 2026-08-09 13:18:00-07:00
lastmod: ''
categories: []
tags:
  - GitHub
  - WSL
draft: false
featured: false
image:
  filename: pexels-christina-morillo-1181253.jpg
  alt_text: ''
  caption: <a href="https://www.pexels.com/ja-jp/photo/1181253/">Photo by Christina Morillo on Pexels</a>
  focal_point: ''
  placement: 3
  preview_only: false
cover: null
recommendations:
  - /blog/2019-11-26_how-to-release-python-package-from-github-actions-d5a1d8edba6e/
  - /blog/2022-01-25_hugo-content-based-recommendation/
  - /blog/2022-05-21_fastest-way-to-release-python-cli/
---

On WSL2 without a working keyring, `gh auth login` falls back to storing the token in plaintext at `~/.config/gh/hosts.yml`. Worse, the OAuth token GitHub CLI issues [never expires until you explicitly revoke it](https://github.com/cli/cli/issues/12009). [A prior article](https://zenn.dev/meijin/articles/gh-cli-auth-token-workaround) covers this problem well.

This isn't a theoretical risk. `gh auth token` shows up repeatedly as a credential-harvesting step in real npm supply chain attacks. Palo Alto Networks' Unit 42 [documented it](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/) in the Mini Shai-Hulud campaign, where a malicious payload invoked Bun to run `gh auth token` alongside other credential-harvesting commands.

To work around it, I set up [ghtkn](https://github.com/suzuki-shunsuke/ghtkn), a CLI that issues a GitHub App User Access Token and refreshes it every 8 hours. A recently added feature lets you set the backend to `agent`, which [encrypts the token with AES-256-GCM](https://github.com/suzuki-shunsuke/ghtkn/blob/main/docs/backend.md#agent-backend) instead of relying on a keyring.

Here's how I installed it, following [the ghtkn author suzuki-shunsuke's own article](https://zenn.dev/shunsuke_suzuki/articles/ghtkn-secure-github-token).

### Before you start

If you've ever run `gh auth login` on this WSL2 environment, a plaintext token is probably still sitting in `~/.config/gh/hosts.yml`. Log out and invalidate it first.

```bash
gh auth status   # check current state
gh auth logout
```

Once the logout succeeds, the file should be empty:

```bash
$ cat ~/.config/gh/hosts.yml
{}
```

### Installation

I installed it via `mise`.

```bash
mise install ghtkn
mise use ghtkn
```

### WSL2 environment prep: systemd + linger

First, confirm `systemd=true` is set in `/etc/wsl.conf`.

```ini
[boot]
systemd=true
```

Then run:

```bash
loginctl enable-linger "$USER"
```

Restart WSL2 from the Windows side for this to take effect.

```powershell
wsl --shutdown
```

After restarting, confirm all of the following:

```bash
ps -p 1 -o comm=
# => systemd

loginctl show-user "$USER" --property=Linger
# => Linger=yes

ls -ld /run/user/1000
# => owned by {username}:{username} and present (if missing, ghtkn agent can't start,
#    failing with `mkdir /run/user/1000: permission denied`)
```

If you run `ghtkn agent start` with the agent backend before linger is enabled, `/run/user/1000` (`XDG_RUNTIME_DIR`) won't exist yet, since systemd-logind never created it. You'll hit this instead:

```plain
error="create the socket directory: mkdir /run/user/1000: permission denied"
```

### Creating a GitHub App

Create a GitHub App and grab its client_id — you'll need it for the config file.

I based mine on the URL from the author's article:
https://github.com/settings/apps/new?url=https://github.com/suzuki-shunsuke/ghtkn&device_flow_enabled=true&webhook_active=false&public=false

Take the Client ID issued after creation and write it into the config file below.

### Config file

Run `ghtkn init` to generate the config file, then fill in the GitHub App's Client ID and pick a backend.

`~/.config/ghtkn/ghtkn.yaml`

```yaml
apps:
  - name: suzuki-shunsuke/write # a name to identify this app; rename freely
    client_id: xxx # GitHub App Client ID

backend:
    type: agent
```

The default backend is the OS keyring, but WSL2 has rough edges there. Some people [have made it work](https://tech.buty4649.net/entry/2023/01/31/182908), but I went with the agent backend instead.

The agent backend gives you:

- Tokens encrypted with AES-256-GCM and stored without a keyring
- Refresh token support, so you skip the device-flow re-authentication every 8 hours (macOS/Linux only — avoid enabling this in environments where malware can easily escalate to root)

### Initial authentication

To use the agent backend, start the agent first.

```bash
ghtkn agent start &
ghtkn agent unlock
```

On first run, it asks you to set a new passphrase (entered twice). Stash it in 1Password or similar so you don't lose it.

```bash
ghtkn auth
```

This kicks off the device flow. [As of v0.2.8](https://github.com/suzuki-shunsuke/ghtkn/issues/453), it no longer tries to open a browser in headless environments — on WSL2, you open the displayed URL yourself and enter the code.

If you run `ghtkn auth` with the agent backend before the agent is running, it fails with:

```plain
error="create a GitHub App User Access Token: begin the device flow on the agent: begin the device flow through the backend: the ghtkn agent is not running; run 'ghtkn agent start'"
```

### Setting up as a systemd user service

To keep the agent running long-term on WSL2, register it as a systemd user service.

First, stop the manually-started agent, or it'll conflict with the one systemd manages.

```bash
ghtkn agent stop
```

`~/.config/systemd/user/ghtkn-agent.service`

```ini
[Unit]
Description=ghtkn agent

[Service]
ExecStart=/home/aki/.local/share/mise/installs/ghtkn/latest/ghtkn agent start
Restart=on-failure

[Install]
WantedBy=default.target
```

Enable it:

```bash
systemctl --user daemon-reload
systemctl --user enable --now ghtkn-agent.service
```

### Day-to-day operation: unlocking the agent

```bash
ghtkn agent unlock --enable-refresh
```

This turns on refresh tokens. Once enabled, the token renews automatically as long as WSL2 stays up.

I looked into feeding the passphrase in automatically via 1Password CLI's `op`, but ghtkn blocks this [at the source-code level](https://github.com/suzuki-shunsuke/ghtkn/blob/2a709a0108b35f9ccc56ddab24bb9abb60f9f9c0/pkg/agent/tty/passphrase.go#L24-L26). I'm treating that as intentional design and typing the passphrase by hand.

### Wrapping the `gh` command

I added a shell function to `~/.zshrc` so `gh` itself routes its token through ghtkn.

```bash
gh() {
    if [ "$1" = "auth" ]; then
      case "$2" in
        token)
          echo "[blocked] 'gh auth token' is disabled" >&2
          return 1
          ;;
        status)
          for arg in "$@"; do
            case "$arg" in
              --show-token|-t)
                echo "[blocked] 'gh auth status --show-token' is disabled" >&2
                return 1
                ;;
            esac
          done
          ;;
      esac
    fi
    ghtkn exec -- gh "$@"
}
```

`ghtkn exec` passes ghtkn's short-lived token to the child process as an environment variable.

The function also blocks `gh auth token` and `gh auth status --show-token`, since both print the token in plaintext.

Check that it's working:

```bash
$ gh auth status
github.com
  ✓ Logged in to github.com account chezou (GITHUB_TOKEN)
  - Active account: true
  - Git operations protocol: https
  - Token: ghu_************************************
```

A token starting with `ghu_...` confirms ghtkn issued it.

### Integrating with mise

mise lets you set `credential_command` so [ghtkn becomes the source for GitHub tokens](https://mise.jdx.dev/dev-tools/github-tokens.html#using-ghtkn).

```bash
mise settings set github.credential_command="$(mise which ghtkn) get -m 1h"
```

Confirm it:

```bash
$ mise token github
github.com: ghu_…(masked) (source: credential_command)
```

### What's still unhandled

[This Japanese article on gh CLI's token handling](https://zenn.dev/meijin/articles/gh-cli-auth-token-workaround) pointed me to more gaps. I still need to check whether [Claude Code's session history retains the token](https://github.com/TeXmeijin/claude-code-history-audit).
