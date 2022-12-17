---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Wowchemyをv5.5.0からv5.7.0に上げた"
subtitle: "そしてAlgoliaを諦めた"
summary: ""
authors: [aki]
tags: [hugo]
categories: []
date: 2022-12-16T17:23:22-08:00
lastmod: 2022-12-16T17:23:22-08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

毎年アドベントカレンダーの時期にHugoのテーマであるWowchemy (旧 Academic) のバージョンを上げています。

今年は、唯一参加したアドベントカレンダーもNotionで済ませてしまったので、恩恵にはあずかれませんでしたが、それでもまあ定期アップデートは大事ですね。

Wowchemyは、スタートするときはサクッとstarter kitから作成できるのですが、変更に追従し続けるのが結構厄介で破壊的変更をガンガン入れてきます。が、ドキュメントは最新のバージョンのものしかなく、 Release noteを見てあとはソースコードを見る羽目になります。正直面倒くさい。

というわけで、今回v5.5.0からv5.6.0、v5.7.0に上げたので何をしたかを備忘録的にメモしておきます。

### v5.6.0

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/chezo.uno/pull/42" data-iframely-url="//iframely.net/owZY8PH?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>


v5.5.0からは結構大きな変更が入りました

- config.yaml (or toml) や params.yaml の構造が大幅に変わった
    - そのままだと検索、Gravaterなどが無効になるので注意
- go.modの依存するmoduleパスの変更
- Algoliaを検索に使うと壊れる

config,params.yamlの変更は、特にどこにも記載がないのでソース読みながら根性で直していきます。特に、 “features” 系は適切に設定しないと、検索が消えたりして大惨事なのでお気をつけてください

多分、rootの設定はいくつか間違っている気もしますが、もう諦めました。

しかし、tomlの構造をパースするのは僕には難しいのでyamlのほうが楽かもしれませんね。

2個目については、ローカルで試すときは例によって `hugo mod get` をすればよいです。

```bash
hugo mod get github.com/wowchemy/wowchemy-hugo-themes/modules/wowchemy/v5@v5.6.0
```

Algoliaは試してみたのですが、エラーが止まらなくて諦めました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/chezo.uno/pull/37" data-iframely-url="//iframely.net/ZR4gvfz?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

### v5.7.0

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/chezo.uno/pull/43" data-iframely-url="//iframely.net/iruvBHp?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

特に大きな影響もなくそのままいけました。過去一楽なアップグレードでした。

`hugo mod get` も6を7に変えるだけです。

```bash
hugo mod get github.com/wowchemy/wowchemy-hugo-themes/modules/wowchemy/v5@v5.7.0
```

### Algoliaを試したけど挫折した

v5.6.0にも書いたのですが、Algoliaを試して辞めました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/chezo.uno/pull/41" data-iframely-url="//iframely.net/wyFUD6u?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

検索自体はよさげなんですが

- Hugoの生成するindex.jsonを取り込むとMedium由来の `--` みたいなハイフンが複数つながるURLが `-` と一個に正規化されたperemalinkと解釈して、無限にredirectsを設定する羽目になる
- Algolia Crawlerを使うNetlify pluginがあるのですが、それを使ってinstantsearchから検索をすると検索結果が空になる

特に後者が致命的でした。なんか、便利そうだけど壊れてて使えないという体験がつらかったので諦めました。

サポートに問い合わせをすればいいのかもしれませんが、もうその気力もなく…。

また、来年Wowchemyのアップグレードをしたいと思います。
