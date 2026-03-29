---
title: ワークフローテンプレートをskillに埋め込んで、LLMの役割を"生成"から"レンダリング"に変えた話
subtitle: Claude Code skillにJinja2テンプレートを埋め込んでML workflowを生成する
summary: ''
date: 2026-03-28 18:03:00-07:00
lastmod: ''
categories: [agent, LLM]
tags: [Development]
draft: false
featured: false
image: null
recommendations: [/post/2025-09-19-review-fatigue/, /post/2013-08-25-llmaturinican-jia-simasita/,
  /post/2019-11-16-tdworkflow/]
---

## MLワークフローのLLMによる自動生成の夢

会社の[AI Signals](https://docs.treasuredata.com/products/customer-data-platform/machine-learning/ai-signals)というML機能では、(MLではないが)RFMや推薦、Contextual Banditといった処理を行う機能がある。特にMLの予測処理をスケーラブルに実行するために、ML用APIをcallすると裏側でAWS Batchが起動して並列でworkerを立ち上げるという仕組みを取っている。この並列実行をするためには、入力テーブルをprofile（マーケティングキャンペーンの対象となるエンドユーザー）ごとに集約するという割り切りを入れることで、スケーラビリティを確保している。これらの処理は、digdagのworkflow（.digファイル。実際にはTreasure Workflow と呼ばれる hosted digdagで実行される）と、workflow内に記述されるSQL（Hive または Trino）とで管理されるワークフローからML APIがdigdagの `http>` operatorで呼び出される。

元々のプロジェクト開始時の座組としては、こうした前処理的・後処理的なワークフローはProfessional Serviceと呼ばれる有償のポストセールスエンジニアのMLEが自分たちで作成したテンプレートを元に、PSを購入した顧客にそのワークフローを展開していたのだが、この枠組みを超えて多くの顧客へ展開したいということで、LLMによるワークフロー・SQL生成が期待されていた。だが、モデルが日々良くなってるとはいえLLMによるワークフロー・SQL生成を安定して行うことは難しく（例えば、TD固有のUDFはぱっと出てこない）、何度か挑戦していたが諦めていた。

## Claude Codeの進化とエージェント用CLI

そんな中、会社でAI Native企業になるというCEOの号令のもとClaude Codeの全社導入が進んだ。ソフトウェアエンジニアだけではなく、PdMやSolution Architect、営業にまでClaude Codeの利用が拡大された。特に重要な取り組みとしては、TDの各種マイクロサービスのAPIを叩ける統一的なエージェント用CLIの[tdx](https://tdx.treasuredata.com/)と、tdxを内包したデスクトップアプリケーションである[Treasure Studio](https://tdx.treasuredata.com/studio/)の貢献が大きい。Claude Codeとtdxが連携することで、エージェントがマーケティングのジャーニーを作成したりTDにあるテーブルの分析結果を可視化したりできるようになったのである。CEO自ら社員向けにオンボーディングチャレンジタスクを作ったりして利用加速を進めた結果、自社内及び顧客環境でも様々な自動化が進んでいる。

この流れで、[顧客向け](https://github.com/treasure-data/td-skills)・社内向けのSkills marketplaceが誕生した。これらを利用することで、作業の再現性が高まり、複雑な処理の自動化が加速しているのである。

## ワークフロー生成におけるエージェント用CLIの功績

tdxの一番大きな功績は、Treasure WorkflowのエンドポイントをCLIから叩けるようにしたことで、Claude Codeがワークフローを作成、push、実行、結果を見て改善というフローが自律的に回せるようになったことである。ワークフローというものは実行するのに少なくとも数分、長ければ1時間以上かかるものもあるため、[自動テストを行うのも難しい分野であり長年苦しんでいた](https://docs.google.com/presentation/d/1hvF29KsE3WmIfoC98EONJjZKovqUFYlHNIKOSZIX_GU/edit)。

それを、Claude Code + tdxのおかげで、生成したワークフローを実行し、バックグラウンドに積んで実行結果を検証というサイクルが実現可能になったのである。これは革命的である。

APIとのやり取りを含めて一気通貫できるエージェント向けCLIは、もはやなくてはならない存在であろう。

## MLワークフローテンプレートのskill化

とはいえ、冒頭でも書いたようにClaude Codeのモデルがいかに賢くなったとはいえ、事前知識がない顧客など、誰が実行しても安定的に納得の行くワークフローをLLMに生成させるのは困難である。

そこで、問題の見方を変えてみた。ワークフロー・SQLをスクラッチで生成するのが難しければ、設定ファイルのパラメータを元にワークフローとSQLを生成するテンプレートを作ればよいのである。つまり、テンプレートをskillに埋め込むことで、LLMの責任範囲は「ワークフローとSQLをスクラッチから生成する」ことから「データや問題に適したパラメータを選ぶ」ことへと狭まる。つまり、欲しいワークフローはあらかじめテンプレート化することでそこは確定的な処理として扱うのである。「[確定的処理はスクリプトに追い出す](https://nyosegawa.com/posts/skill-creator-and-orchestration-skill/#2.-%E7%A2%BA%E5%AE%9A%E7%9A%84%E5%87%A6%E7%90%86%E3%81%AF%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%81%AB%E8%BF%BD%E3%81%84%E5%87%BA%E3%81%99)」の応用といったところか。

この発想は、cdp-apiがDBの値をもとに動的にdigdagのworkflowを生成するというところから着想を得た。

<script defer class="speakerdeck-embed" data-slide="29" data-id="dcef99361823438cb3b542784fa07b56" data-ratio="1.7772511848341233" src="//speakerdeck.com/assets/embed.js"></script>

[https://speakerdeck.com/aamine/treasure-data-techtalk-2022-td-cdp-in-30-minutes?slide=29](https://speakerdeck.com/aamine/treasure-data-techtalk-2022-td-cdp-in-30-minutes?slide=29)

## digdagワークフローのJinja2テンプレート

実際にskillとして行ったのは、Jinja2でdigファイルをテンプレート化し、LLMは config.yml をsingle source of truthとしてすべての変更可能なパラメータを置き、設定値を決定することにフォーカスをさせた。 .dig.j2 というあまり世の中で見ない拡張子を見たときは、ちょっとドキドキした。

内部ではレンダー時に決定するパラメータ `{{ }}` と、digdagの変数として記述できるランタイム時のパラメータ `${ }` を使い分けている。前者は、例えばSQLのエンジンがHiveかTrinoかによって分岐させたり、使うアルゴリズムやハイパーパラメータの候補が事前に決定できる場合に使われる。後者は、例えばハイパラチューンをした結果をテーブルに格納し、その結果をSQLで取得した際に動的に学習タスクに割り当てる、みたいなときに使う。

## OpenAPI = agentとの契約書

テンプレート化をする際に厄介なのが、ML APIに渡せるパラメータが複雑であり、それをどのようにagentに教えるかということである。幸いにも、自分たちのプロジェクトでは、ML用エンドポイントのパラメータはOpenAPIで管理されており、そのspecで網羅的に渡すことが出来た。

元々、MLソリューション実行時にはOpenAPIから [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) で生成されたmodel.pyでパラメータのバリデーションを行っていたのだが、機械可読な仕様である openapi.yml をエージェントに渡すことで、それを翻訳したmarkdownにskill化していた。標準フォーマット万歳である。

## skill作成 agent VS skill使用 agent

skill作成中に作ったskillのテストどうするのがいいの？とClaudeに聞いたら、別プロセスでagent立ち上げて試行錯誤をするのが良いと教えてもらったので、それを実践した。これは非常に良い体験だった。

具体的には、skill使用agentを使うときは、OpenAPIやskillのドキュメントを自分で読むわけではないので、「このアルゴリズムとこのパラメータの組み合わせを実行したい」みたいな欲求が湧いてくるのである。通常、手動でやる sanity check だと頭に仕様が乗っており、面倒で複雑なパラメータの組み合わせはサボりがちなのだが、agentに任せれば簡単にできるという欲が湧いてくる。

しかし、skill使用agentから帰ってきた言葉は「skillを見たけどまだその組み合わせはOpenAPI的には実装されていない」という答えだった。一応、QAのend to endのテストもあると思っていたのに、危ないところであった。実際にはOpenAPIを手動で管理していたため、Pythonコード内部では実装されていたが、リクエストから受け付けるパラメータの漏れがあるのが見つかった。

このバグを早急に修正して、development環境にdeployし、skillもupdateしたところ、新しい組み合わせのパラメータをさも今までもあったかのようにClaudeは使いこなしていた。流石である。

開発しながらskillも作ることで、実行環境を用意することがかなり恩恵があるということを学んだ瞬間である。

## まとめ

こうして得られたskillを社内skills marketplaceに共有することで、今まで有償PSが作っていたworkflow作成ステップを簡略化し、さらには有償PSを買っていない顧客でも利用可能となった。

また、Treasure Studioの恩恵として、MLで予測した結果を可視化できるようになり、簡単に分析・モデル改善のサイクルが回せるようになった。これらの分析のパターンもskill化していくと良さそうだが今回はスコープ外とした。

この記事を書くときにClaudeと壁打ちをしていたのだが、「LLMの強みは問題の構造を理解することとパラメータ推論」とClaudeは主張している。それを支援するための一気通貫したCLIを用意することで、生成→実行→修正のループを自律的に回せるようになる。そこでループの複雑なタスクをテンプレート化することで、ドメイン知識のある人間と、（知識がない人が使う）agentの役割分担ができるのだと学んだ。
