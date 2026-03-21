---
title: 「Agents SDK+αのTipsを一人で書いていくアドカレ Advent Calendar 2025」を追走した
subtitle: ''
summary: ''
date: 2026-03-20 18:03:00-07:00
lastmod: 2026-03-20 18:41:00-07:00
categories: [AI Agent]
tags: [Agent]
draft: false
featured: false
image: null
recommendations: [/post/2014-12-31-2014nian-wozhen-rifan-tute/, /post/2014-07-05-number-juliatokyo-01de-julia100ben-notuku-wofa-biao-sitekimasita/,
  /post/2019-11-25-github actions-issue template/]
---

[@mocobeta](https://blog.mocobeta.dev/) さんが書いてくださった、OpenAIの[Agents SDKを試すアドベントカレンダー](https://adventar.org/calendars/12523)の追走をした。子供の春休みで有給取っていることもあり、春休みの宿題よろしくやってみた。

レポジトリはこちら: https://github.com/chezou/hello-agents/

（追走を）完走した感想だが、以前にLangChainとChromaをベースに社内のConfluenceを検索するRAGシステムを社内のハッカソンで作ったとき以来のフレームワークで、Agentのパターンを頭に入れたうえでどういう実装をしているのかを学ぶのにとても良かった。

Claude Opus 4.6に自習計画を立ててもらいながら、重要なところ、スキップするところをリストしてもらったが、先にこの記事を読んでおくとパターンが整理されて良かった。

[Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

なお、一番大事なのはネタバレが重要なフィクションを例として使えること。元々の記事では銀魂と終末のワルキューレ、僕の場合は、ヴィンランド・サガでいきました。

また、並行して会社の業務の一環として[tdx](https://tdx.treasuredata.com/)というCLI toolと連携するための社内skillsを作っていたのも理解を深めるのに役に立った。やったこととしては、[AI Signals](https://docs.treasuredata.com/products/customer-data-platform/machine-learning/ai-signals)というプロダクトのソリューション、RFM、NBP（推薦）といった公開済みのソリューションを中心に、 digdag のworkflowテンプレートをJinja2テンプレート化してskillにまとめるというもの。これにより、スクラッチからdigdagのワークフローを作る必要がなく、パラメターをagentが設定すれば、tdx経由でworkflow push/runをして予測結果も可視化して分析できた。

世の中の流れ的に、エージェントの制御を自前実装するよりもClaude Codeやcodexに渡したほうが速いみたいなのが来てる感じはするけれども、その裏側でどう動いているのかを考えて設計できるようになったのは何よりだった。

あとは、メモリ周りの知識がまだ欠けているのもありそこをキャッチアップしつつ、合わせて[Ralph Loop](https://ghuntley.com/loop/)なんかも学んでいきたい。
