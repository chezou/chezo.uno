---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "3ファイル追加してGitHub ActionsでHugoにレコメンド記事を表示する"
subtitle: "prelimsを使ってコンテンツベースのレコメンドをしてみよう"
summary: "prelimsとGitHub Actionsを使うことで、Hugoの自分の記事にレコメンド記事を表示できるようになります"
authors: [aki]
tags:
  - recommendation
  - hugo
  - github actions
categories: [tech, ML]
date: 2022-01-25T18:41:33-08:00
lastmod: 2022-01-25T18:41:33-08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "https://chezo.uno/post/2021-04-24-ml-at-work-2nd-edition/ へのレコメンドの例"
  focal_point: "Smart"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

こんにちは、早いものでもう40の大台が迫ってくる誕生日を迎えました。前日にブースターショットを打ったので、一日中ほとんど寝込んでいました。必要な人のために、[例のリスト](https://www.amazon.jp/hz/wishlist/ls/FH3MHL6LTE02?ref_=wl_share)を置いておきます。

さて、Hugoにはキーワードベースの関連記事の表示をする機能があります。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://gohugo.io/content-management/related/" data-iframely-url="//iframely.net/q1grvUY?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

しかし、キーワードベースの関連記事も悪くはないのですが、折角なので自分で関連記事のレコメンドをしてみたくないですか？
そう思っていたら、 [takuti](https://twitter.com/takuti) さんの Prelims というオープンソースを見つけました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/takuti/prelims" data-iframely-url="//iframely.net/omDBVa8?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

Prelimsは、Hugo（やJekyll）のFront matterと呼ばれるメタデータの部分にキーワードやレコメンド記事を足してくれるものになります。

レコメンドの方式自体は、今実装されているのは古典的なTF-IDFを用いたコンテンツベースの類似文書を出してくる方式ですが、Front matterを後から処理してレコメンド記事を追加するというシンプルだけどスマートな方法に感銘を受けました。

ただし、Prelimsはflexibilityを重視しているため、例えば日本語のtokenizerやstop wordsなどは自分で設定をする必要があります。

このあたり、ちょっと慣れていないと難しいかなとも思ったので、[prelims-cli](https://github.com/chezou/prelims-cli)というCLIツールを作り、config用のYAMLファイルを用意すればGitHub Actionsでrecommendできるようにしました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/prelims-cli" data-iframely-url="//iframely.net/m9C9uKt?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

用意するものは以下の3つです。

1. prelims-cli用の scripts/config/myconfig.yaml
2. 関連ページを表示する layouts/partials/page_related.html
3. prelims-cliを実行する GitHub Actions

実際の例をgistに貼りました。

{{< gist chezou a9cb0ab2a086b3ce9ce9bf1abbc5b347 >}}

myconfig.yaml については、 `content/blog` が英語の `content/post` が日本語の記事をおいている想定です。
この3つのファイルを追加すればHugoであれば関連記事が、冒頭の画像のように出てくるはずです。

内部的には日本語のtokenizerはSuachiPyのfull辞書を使い、最も長いCモードで形態素単位を設定しています。
ただし、prelimsが生成する `keywords` は少しノイジーだなと思ったので、自分のサイトでは `recommendations` のみを利用しています。

僕はものぐさなので、タグやカテゴリを豆にメンテナンスできないのですが、レコメンドのおかげで過去の関連記事のリンクも出せるので便利だと感じています。
また、自分の記事は自分の持ち物なので、それに対してレコメンドしてML的なsandboxとして遊ぶのは楽しいなと感じています。

この環境を使うことで、Netlify CMSでの執筆等Python環境を用意することができないところでも執筆して、レコメンド記事を作成することができます。
もしよければ、 prelims を使ったレコメンドを試してみてください。
