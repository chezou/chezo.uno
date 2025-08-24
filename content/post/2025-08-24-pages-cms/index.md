---

title: Pages CMSの設定をした
date: 2025-08-24 12:09:00+00:00
lastmod: 2025-08-24 14:38:00+00:00
draft: false
featured: false
image:
  preview_only: false
  filename: media/pages-cms.png
keywords:
  - hugo
  - 画像
  - wowchemy
  - cloudflare
  - 検索
  - 移行
  - 設定
  - 模索
  - 変わり
  - ワークアラウンド
recommendations:
  - /post/2022-12-16-bump-wowchemy-v570/
  - /post/2022-01-14-prelims-recommend-hugo/
  - /post/2022-01-25-hugo-content-based-recommendation/
---

以前からiPadなどのモバイル端末でHugoの記事を書く方法を模索していたのだけど、そんななかでmehoriさんのこの記事を知ったのでPages CMSを試してみた。

[Pages CMS：設定ファイル一つですぐに使える、静的サイト向けのお手軽CMS](https://mehori.com/blog/2025/pages-cms/)

結論から言うと、Hugoのフォルダ構造 (/articlename/index.md) はまじめにサポートしていないのと、それにより[画像周りのアップロードが微妙](https://github.com/pages-cms/pages-cms/issues/129)なこと、そもそも、iPhoneから[画像をアップロードしようとすると413エラーが出てアップロードできない](https://github.com/pages-cms/pages-cms/issues/284)ことなどあるが、まあとりあえずiPadから日本語で文字だけの記事は設定できたのでよし。

途中、めちゃくちゃマイナーなYAML frontmatterのパースエラーが出たけど、ワークアラウンドも見つけることができた。 [https://github.com/pages-cms/pages-cms/issues/308](https://github.com/pages-cms/pages-cms/issues/308)

コードを読めば何とかなるレベルなのだけど、必要最低限のものはあるのでいいかな。

現状、こんな設定です [https://github.com/chezou/chezo.uno/blob/438a1b6895cc0dc25386e926922382bba5ed38f4/.pages.yml](https://github.com/chezou/chezo.uno/blob/438a1b6895cc0dc25386e926922382bba5ed38f4/.pages.yml)

併せて、wowchemyからhugo-bloxに移行をしたけど、そっちもまあまあ大変だった。詳しくは PRを見てもらえれば。しかし、Hugo Academic -> Wowchemy -> Hugo Bloxと名前変わりすぎだろ...。

*   [https://github.com/chezou/chezo.uno/pull/50](https://github.com/chezou/chezo.uno/pull/50)
    
*   Amazonアフィリエイトの画像が出なくなっていた問題も画像出さないように修正した [https://github.com/chezou/chezo.uno/commit/95aad549ee3554bacb560d39dfb51d1499207aa8](https://github.com/chezou/chezo.uno/commit/95aad549ee3554bacb560d39dfb51d1499207aa8) [https://github.com/chezou/chezo.uno/commit/861182ece0c398787306c242b7f3c558508b8d43](https://github.com/chezou/chezo.uno/commit/861182ece0c398787306c242b7f3c558508b8d43)
    

移行した後に検索が動かないことに気づいたんだけど、

*   pagefindのインデックス作る設定をCloudflare上でbuild commandに追加 -> `&& npx pagefind --source 'public'`
    
*   CloudflareのRocket Loader周りの試行錯誤をしたけど[ダメだったので無効](https://github.com/chezou/chezo.uno/pull/52#issuecomment-3218275752)にした
    

というので何とか動き始めた。けど、日本語はまともに検索できなさそう。仕方ない。