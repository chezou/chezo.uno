---
title: WSL2にghtknを設定してgh CLIがトークンをファイル平文保存するのを防ぐ
subtitle: ''
summary: ''
date: 2026-08-09 12:27:00-07:00
lastmod: ''
categories: []
tags:
  - wsl
  - github
aliases: []
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
  - /post/2020-07-16-google colaboratory-vs code(code-server)/
  - /post/2013-01-09-autopagerize-rubynomechanizeban-wozuo-tuta/
  - /post/2026-04-24-tiktokで勝手にアカウントが作られ続けるので、claudeでカナダのprivacy法に則って通/
---

`gh auth login` はWSL2でkeyringが使えない場合、トークンを `~/.config/gh/hosts.yml` に平文保存をしてしまう。また、GitHub CLIで生成されるOAuth tokenはトークンは[明示的にrevokeするまで有効](https://github.com/cli/cli/issues/12009)である。この当たりは[先人の記事](https://zenn.dev/meijin/articles/gh-cli-auth-token-workaround)が詳しい。

これを回避するために、[ghtkn](https://github.com/suzuki-shunsuke/ghtkn)というCLIを導入した。ghtknはGitHub Appから8時間毎に更新されるUser Access Tokenを発行するCLIである。さらに、最近入った機能でバックエンドを `agent` にすることで、keyringに依存せず[ AES-256-GCM で暗号化してトークンを保存](https://github.com/suzuki-shunsuke/ghtkn/blob/main/docs/backend.md#agent-backend)できる。

今回は、作者の[suzuki-shunsukeさんの記事](https://zenn.dev/shunsuke_suzuki/articles/ghtkn-secure-github-token)を見ながらインストールをしたので、その方法をメモしておく。

### はじめに

過去に一度でも `gh auth login` をWSL2環境でしていたら、 `~/.config/gh/hosts.yml` に平文トークンが残っている。作業前にログアウトし、保存された平文トークンを無効化しておく。 

```bash
gh auth status   # 現状確認
gh auth logout
```

正常にログアウトされていれば空になる

```bash
$ cat ~/.config/gh/hosts.yml
{}
```

### インストール

今回は `mise` 経由でインストールをした。

```bash
mise install ghtkn
mise use ghtkn
```

### WSL2の環境設定準備: systemd + linger

まず、 `/etc/wsl.conf` で `systemd=true` が設定されていることを確認する。

```ini
[boot]
systemd=true
```

確認したら以下を実行する。

```bash
loginctl enable-linger "$USER"
```

その後、Windows側から一度WSL2を再起動して反映させる。

```powershell
wsl --shutdown
```

再起動後、以下が正常に出力することを確認する。

```bash
ps -p 1 -o comm=
# => systemd

loginctl show-user "$USER" --property=Linger
# => Linger=yes

ls -ld /run/user/1000
# => {username}:{username} 所有で存在する(存在しないと `mkdir /run/user/1000: permission denied` でghtkn agentが起動できない)
```

`linger`を有効にせずにagent backendで `ghtkn agent start`しようとすると、`/run/user/1000`(`XDG_RUNTIME_DIR`)がsystemd-logind経由で作られておらず、`create the socket directory: mkdir /run/user/1000: permission denied`というエラーになる。

### GitHub Appの作成

GitHub Appを作成し、client_idを取得する。これを設定ファイルに書けば良い。

今回は、作者の記事から以下のURLをベースに作成をした。
https://github.com/settings/apps/new?url=https://github.com/suzuki-shunsuke/ghtkn&device_flow_enabled=true&webhook_active=false&public=false

作成後に発行されるClient IDを次で設定する設定ファイルに書き込む。

### 設定ファイル

`ghtkn init` を実行して設定ファイルを生成し、そこにGitHub AppのClient IDと今回使うbackendの設定をする。

`~/.config/ghtkn/ghtkn.yaml`

```yaml
apps:
  - name: suzuki-shunsuke/write # 識別用のapp名。適当に書き換える
    client_id: xxx # GitHub AppのClient ID

backend:
    type: agent
```

バックエンドはデフォルトはOS keyringだが、WSL2ではハマりどころがありそうだった（[先駆者](https://tech.buty4649.net/entry/2023/01/31/182908)はいるにはいる）のでagentバックエンドを使うことにした。

agentバックエンドは以下の特徴がある。

- トークンはAES-256-GCMで暗号化して保存（keyring不要）
- refresh tokenに対応し、8時間毎のdevice flow再認証が不要になる（macOS/Linuxのみ対応。rootに用意に昇格できる環境では避けるべき）

### 初回認証

agent backendを使って初期設定するためには、先にagentを起動する必要がある。

```bash
ghtkn agent start &
ghtkn agent unlock
```

初回はパスフレーズを新規設定（2回入力）する必要がある。人間用に1Passwordにでも保存しておくと良い。

```bash
ghtkn auth
```

これを実行するとDevice Flowが開始される。[v0.2.8以降](https://github.com/suzuki-shunsuke/ghtkn/issues/453)ではheadless環境ではブラウザを開かなくなったため、WSL2では自分で表示されたURLを開いてコードを入力する。

なお、agent backendでagent未起動時にghtkn authを実行すると以下のエラーが出て失敗する。

```plain
error="create a GitHub App User Access Token: begin the device flow on the agent: begin the device flow through the backend: the ghtkn agent is not running; run 'ghtkn agent start'"
```

### systemdユーザーサービス化

WSL2でagentを常駐させるために、systemdユーザーサービスとして登録する。

まず、この設定をする前に agentを停止する。そうしないと、systemdで管理するagentと競合する。

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

以下のコマンドを実行して有効化する。

```bash
systemctl --user daemon-reload
systemctl --user enable --now ghtkn-agent.service
```

### 日常運用: agent unlock

```bash
ghtkn agent unlock --enable-refresh
```

を使うことで、refresh tokenするようになる。これを実行するとWSL2を落とさない限り自動更新する。

なお、1Password CLIの `op` 経由でパスフレーズを自動で入力できないか検討したが、ghtknの[ソースコードレベル](https://github.com/suzuki-shunsuke/ghtkn/blob/2a709a0108b35f9ccc56ddab24bb9abb60f9f9c0/pkg/agent/tty/passphrase.go#L24-L26)で明示的に禁止されている。

設計思想として手動入力を前提にしていると受け入れた。

### ghコマンドのラッパー化

`gh` コマンド事態もghtkn経由でトークンを渡すように、 `~/.zshrc` にシェル関数を設定をした。

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

`ghtkn exec` は ghtknが管理する短命トークンを環境変数として子プロセスに渡して実行する。

また、 `gh auth token` と `gh auth status --show-token` をされると平文でトークンが出るのでそれを防いでいる。

以下で動作確認ができる。

```bash
$ gh auth status
github.com
  ✓ Logged in to github.com account chezou (GITHUB_TOKEN)
  - Active account: true
  - Git operations protocol: https
  - Token: ghu_************************************
```

`ghu_...` で始まればghtkn経由のトークンを使っている。

### miseとの連携

miseでは `credential_command` を設定することで[ghtknをGItHubトークンの取得元にできる](https://mise.jdx.dev/dev-tools/github-tokens.html#using-ghtkn)。

```bash
mise settings set github.credential_command="$(mise which ghtkn) get -m 1h"
```

確認は以下のとおり。

```bash
$ mise token github
github.com: ghu_…(masked) (source: credential_command)
```

### まだ対応していないこと

[gh CLIの認証トークンの扱いが怖すぎるので、暫定的な対応手段をまとめた](https://zenn.dev/meijin/articles/gh-cli-auth-token-workaround) を読むと、まだ対応の余地がある点がいくつか残っているのに気づいた。特に、Claude Codeのセッション履歴にトークンが残る可能性は要検討。
