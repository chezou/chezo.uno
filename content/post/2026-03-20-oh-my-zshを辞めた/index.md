---
title: Oh-my-zshを辞めた
subtitle: ''
summary: ''
date: 2026-03-19 18:56:00-07:00
lastmod: ''
categories: []
tags: []
draft: false
featured: false
image: null
---

OMZは特に何も考えなくても楽に設定できたので使い続けていたが、GH Copilotなどでshell起動が重いと怒られるようになっていたところ、joker1007さんのこんな投稿を見かけた。

https://bsky.app/profile/joker1007.bsky.social/post/3mfqjogaqsh2g

ので、脱OMZをした。

- [Starship](https://starship.rs/): ターミナルの見た目をカスタマイズ用

- [Carapace](https://carapace-sh.github.io/carapace-bin/carapace-bin.html): 主にgitの補完

今のところ、WSL2の環境で動かしているけど悪くはない。Starship用にNerd Fontを入れないといけないのだが、JetBrains MonoのNerd Fontを https://www.nerdfonts.com/ からダウンロードして使っている。

starship.tomlもこんな感じにしている。

https://gist.github.com/chezou/cf444515c282e825d298e38a57365f32
