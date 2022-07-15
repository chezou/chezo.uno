---
title: 機械学習工学研究会夏合宿2022でMLインフラ運用WGを終了しました
subtitle: ''
summary: MLSE の本番適用のためのインフラと運用WGの活動を終了しました。
authors: [aki]
tags: []
categories: [conference]
date: 2022-07-15 15:16:04-07:00
lastmod: 2022-07-15 15:16:04-07:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [課題, 基盤, 夏合宿, 作り, チーム, 運用, 難しさ, 変化, mlops, 議論]
recommendations: [/post/2020-11-10-mlse-conference/, /post/2020-07-11-mlse-summer-workshop/,
  /post/2020-12-31-2020-review/]
---

2019年から土橋さん ([@masaru_dobashi](https://twitter.com/masaru_dobashi)) と共同幹事をしていた、機械学習工学研究会 (MLSE) の「本番適用のためのインフラと運用WG」を、今月頭の夏合宿で終了しました。

## 2022年MLSE夏合宿での議論

今回の夏合宿では、過去開催してきた討論会やカンファレンスで上がっていた、本番適用をするための課題をリストアップし、現在も課題となっている部分を中心に議論をしました。

議論に使ったMuralはGitHubにexportしてあります。

https://github.com/mlse-jssst/InfraOpWGProceedings/blob/master/20220702_SummerCamp/MLSE_InfraOPWG_SummerCamp_Output.pdf

黄色以外の色のものは当日追加したトピック、左下の赤で囲まれた部分はさらにそのまとめになります。

活動をまとめていて気づいてきたのは、多くのMLOpsツールを提供するベンチャーやクラウドベンダーによって、自動化をするためのOSSやマネージドサービスはそろってきているものの、組織やプロジェクトのフェーズごとに必要なものが違ってくるということでした。

フェーズによるML基盤の変遷としては、Karteの基盤の変遷の話を思い出しました。

<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/d2b7118ec5eb461fbe8c79bb6343f6b8" title="History of the ML system in KARTE" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 560px; height: 315px;" data-ratio="1.7777777777777777"></iframe>

少人数でのML基盤としてはCADDiのマネージドな環境を駆使した基盤も参考になると思います。

<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/c572de6c163a4b6fb9b268d2a9c1417a" title="CADDi AI LabにおけるマネージドなMLOps" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 560px; height: 314px;" data-ratio="1.78343949044586"></iframe>

また、組織やチーム作り自体が大きな障壁になりうる話も頻繁に聞いており、これは研究者的なモデル開発をする人と運用をするdeveloperをチームとしてどう構成すればいいのか、どうやってナレッジや成果物を共有すればいいのか（研究開発部門が子会社など）、チーム作りの課題が浮き彫りになりました。

あとは、機械学習やデータを活用したプロダクトづくりの文化の醸成も、銀の弾丸がない中で各社試行錯誤していることがうかがえました。これは、プロジェクトのKPI設計をビジネスサイドに理解してもらう難しさや、作り切りでOKだった従来型のソフトウェア製品とは違った変化に対応し続ける必要がある機械学習システムの「運用」の理解を得る難しさが課題に挙げられました。

## 振り返ってみて

企業の事業部門に在籍しながら3年というスパンで学会仕事をするのは、なかなか大変だったなというのを改めて実感しました。COVID-19による社会情勢の変化、海外移住など個人の状況の変化、会社のチームの異動（上司が変わるたびに説得をする必要がある）と、長期的に継続する社外活動というのは思うようには進まないものだなという当たり前のことを感じました。

もう一回程度、事例共有カンファレンスがしたかったですが、最近では[MLOps勉強会](https://mlops.connpass.com/)でそういった話が日本語でも展開されているので、そちらにも期待です。

## 今後について

今後は、（我々も事前にすり合わせたわけではないのですが）ちょうど[杉山さん](https://twitter.com/K_Ryuichirou)をはじめとする皆さんがこの夏合宿から開始した、[機械学習オペレーションWG](https://mlxse.connpass.com/event/251751/)に引き継がれていきます。今後の活動が楽しみです。

## 過去の活動の様子

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2018-05-17_mlse-kickoff/" data-iframely-url="//iframely.net/eSKNDTE"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2020-07-11-mlse-summer-workshop/" data-iframely-url="//iframely.net/roy2DFa"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2020-11-10-mlse-conference/" data-iframely-url="//iframely.net/tRnxnhX"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>
