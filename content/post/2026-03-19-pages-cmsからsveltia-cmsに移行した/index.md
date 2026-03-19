---
title: Pages CMSからSveltia CMSに移行した
subtitle: ''
summary: ''
date: 2026-03-19 11:06:00-07:00
lastmod: ''
categories:
  - blog
tags:
  - blog
draft: true
featured: false
image: null
---

去年の夏に[Pages CMSを導入した](https://chezo.uno/post/2025-08-24-pages-cms/)のだけど、色々と気になる点が出てきたのでSveltia CMSに移行した。

### モチベーション

[このコメント](https://github.com/chezou/chezo.uno/pull/96#issuecomment-4078902665)にも書いたけど、Pages CMSの以下の問題が起因だった。

- タイムゾーンの扱いが雑（とにかく+00:00に落とす）だったのと、[丁寧にユースケースまで提供した](https://github.com/pages-cms/pages-cms/issues/247#issuecomment-4071771738)けど修正する気があまりなさそうだったこと

- Hugobloxが推奨するコンテンツ(index.md)と画像が同じフォルダに置かれる構成を実現するのがかなり面倒くさい。結局手で画像をuploadしていた

### やったこと

- 認証のためにCloudflare WorkersにSveltia CMS Authをデプロイした

- Pages CMSの .pages.yml を static/admin/config.yml にClaudeが移植した

- static/admin/index.html をドキュメントからコピペした

- Pages CMSがdropしたタイムゾーンの問題をClaudeで復旧した

一番の難所は、Sveltia CMS Authのデプロイだけど、元々、Cloudflare Pagesを使っていたのでやることは https://github.com/sveltia/sveltia-cms-auth のREADMEにあるデプロイボタンを押して手順に従うだけだった。簡単。Herokuを思い出す。

詳しくは以下のPRを見てください。

- https://github.com/chezou/chezo.uno/pull/96

- https://github.com/chezou/chezo.uno/pull/99

### 感想

Pages CMSの小さい不満点が色々と解消されているのがとても良い。例えば、400以上のpostがあるときにPages CMSだと10秒以上開くのにかかるのだが、Sveltia CMSは2秒くらいで終わる。速い。

また、M↓ボタンがあるので、これのおかげで最悪md形式で手動で直せるのがとても良い。今まではGitHubに行って手で修正していた。これは、mobileからの操作を考えたときに最悪の体験だったので、かなり助かる。

後はきめ細やかさが色々と伝わってくる。この記事を書いているときに、GitHubの障害が発生していたのだが、それのwarningが出ている。Client sideで動いてるのにこれは感動。

![warning notification of GitHub issue on Sveltia CMS](pasted-image-1773944380663.png)

というわけで、しばらくは楽しく試してみようと思う。
