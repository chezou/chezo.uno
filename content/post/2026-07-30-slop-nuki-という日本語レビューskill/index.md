---
title: slop-nuki という日本語レビューskill
subtitle: ''
summary: ''
date: 2026-07-30 23:23:00-07:00
lastmod: ''
categories:
  - tech
tags:
  - ai
  - skill
aliases: []
draft: false
featured: false
image:
  filename: pexels-göksun-barış-gökalp-35233446.jpg
  alt_text: ''
  caption: <a href="https://www.pexels.com/ja-jp/photo/35233446/">Photo by Göksun Barış Gökalp on Pexels</a>
  focal_point: Smart
  placement: null
  preview_only: true
cover:
  image: pexels-göksun-barış-gökalp-35233446.jpg
  alt_text: <a href="https://www.pexels.com/ja-jp/photo/35233446/">Photo by Göksun Barış Gökalp on Pexels</a>
  style: ''
  height: ''
  position: null
  icon: null
recommendations:
  - /post/2025-12-09-2025-12-09-principal-engineer-in-the-gene-of-ai/
  - /post/2026-08-04-ブログの推薦用軽量embedding-modelをbekkoに変えようとして、変えれなかった/
  - /post/2026-04-17-ai時代の転職活動記録/
---

英語でメールを書くときに、重ためな内容[^1] を投げるのはAIに生成してもらっている事が多く、そのときに流石にAI臭いとアレかな、と思い [stop-slop](https://github.com/hardikpandya/stop-slop) というskillを使っている。

で、日本語でメールやらSlackやらを書くときにも同じことができなかなーと思っていたら、鹿野さんが [japanese-tech-writing](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d) というskillをつくっているのを見かけたのだけど、技術文章用は別に求めていないな、と思ってアレンジしてskillにした。

[https://github.com/chezou/slop-nuki](https://github.com/chezou/slop-nuki)

slop-nukiは、シミ抜きみたいにslopを抜きたい、というダジャレである。

[cojiさんのnatural-japanease](https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint)とか、223mleさんの[clear-japanese](https://github.com/223mle/skills/tree/main/skills/clear-japanese)とか似たようなのは色々あるみたいだけど、 claude.ai で使いたいということと、ビジネスシーンで使えるようにするというのでPython依存とかはしないようにしてる。

claude.ai に入れるときは、GitHubのリリースからzipをダウンロードしてくれれば使える。Claude Codeなどでは[好きな方法で](https://github.com/chezou/slop-nuki#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)インストールしてもらえばいいんじゃないかな。

このスキルの副作用としては、なぜか混入するキリル文字やハングルをClaudeが「typoを見つけたので直しておきました！」とついでに修正してくれることである。実際、HTMLでレポートを生成するときに、これを通すと読みやすくなるから助かっている。

[^1]: 教育委員会に苦情を言うときとか
