---
authors: [aki]
date: 2022-01-14 21:35:00-08:00
lastmod: 2022-01-15 09:29:00-08:00
summary: HugoやJekyllの記事にレコメンドを足すためにprelimsを使った
tags: [NLP, Python, Recommendation]
title: prelimsを使ってHugoの記事にレコメンドを追加する
keywords: [hugo, 生成, prelims, wowchemy, レコメンド, キーワード, jekyll, ビルド, 名前, 記事]
recommendations: [/post/2022-01-25-hugo-content-based-recommendation/, /post/2025-08-24-pages-cms/,
  /post/2017-01-22-shu-shi-ru-rinomarkdownwosphinxwoshi-tutehtml-slash-pdfnisuru/]
---


![](https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

シンプルだけど、アイデアは賢いなーと思ったHugoやJekyllの記事にレコメンドを足す、prelimsを使ってみた。

[https://github.com/takuti/prelims](https://github.com/takuti/prelims)

prelimsはなんてことない、TD・IDFでキーワード生成したり、そのコサイン類似度で記事の類似度を出してコンテンツベースのレコメンドを生成してくれるもの。

takutiさんは、gulpでやっているようだっただけど、僕が使ってるHugoのWowchemyに対してやってみた。

実際のcommitを見てもらうのが早い気もするが、JekyllやHugoにあるFrontmatterというメタデータに `recommendations` というキーワードを追加して生成してくれるというもの。Hugoのビルド自体はそんなに遅くならない、はず（というのは、サイトの相対URLを生成して名前解決はビルド時に行うので、記事数が多くなると重くなりうる）。

[https://github.com/chezou/chezo.uno/commit/0e4dabe4555b165fc9043deda108b6c783cd9487](https://github.com/chezou/chezo.uno/commit/0e4dabe4555b165fc9043deda108b6c783cd9487)

ちょっとハードルあるかなというのが、自分で下記のようなPython scriptを書かないといけないところ。まあtokenizerとかstop wordsとかどうすんねん問題があるので致し方なし。

[https://github.com/chezou/chezo.uno/commit/c908c6ad5fd4c1ccc57bd82d74a62bb12f602890](https://github.com/chezou/chezo.uno/commit/c908c6ad5fd4c1ccc57bd82d74a62bb12f602890)

あとは、Hugoの Wowchemyというテーマを使っているけど、 `layouts/partials/page_related.html` という名前でこういうものをつくる必要があるのです。

```html
{{ if isset .Params "recommendations" }}
<div class="article-widget content-widget-hr">
  <h3>{{ i18n "related" }}</h3>
  <ul>
    {{ $candidates := where .Site.RegularPages "Type" "in" site.Params.mainSections }}
    {{ $rec := apply .Params.recommendations "lower" "." }}
    {{ $filtered := where $candidates "RelPermalink" "in" $rec }}
    {{ range $filtered }}
    <li><a href="{{ .Permalink }}">{{ .Title }}</a></li>
    {{ end }}
  </ul>
</div>
{{ end }}
```

`config.toml` には `params.mainSections` を指定することで、指定したSectionのタイプに対して表示されるようにできます。

```html
[params]
  mainSections = ['post', 'blog']
```

ゆくゆくはclickかなにかでCLI作ってwrapしてしまうかなぁ。

---

[Buy me a 🍵](https://www.buymeacoffee.com/chezou)

[Back to home](https://memo.chezo.uno/)