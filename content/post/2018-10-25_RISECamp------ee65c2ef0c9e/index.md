---
title: RISECampに参加した
description: >-
  10/11–12にUC
  BerkeleyのRISELabが主催していたbootcampに参加しました。kawasaki.rbでも少し話しましたが、参加報告です。
date: '2018-10-25T08:01:02+09:00'
categories: []
keywords: [conference]
authors: [aki]
---

10/11–12にUC Berkeleyの[RISELab](https://rise.cs.berkeley.edu/)が主催していたbootcampに参加しました。kawasaki.rbでも少し話しましたが、参加報告です。雰囲気は[公式FBの写真](https://www.facebook.com/media/set/?set=ms.c.eJw9U1mSxUAIutGUtvv9Lzb1RPJJEVGg4~_2TEtYZz~%3BP9~_WIrnY5W4BjwkcSui8vJO3i9~_ZjffI0cVl0968NTYTrSQb388SN2fK2~_O~%3BRTXVZP5vi3~_v0~_~%3BQf9Ouzz01ez06~%3Bd94T7Avfnp7~%3B~_rOhvZnnN08vVr6b~_C~_znvMXON~_95CZ5~_5EHvsIqvnsfhB3~_P~%3BgzzyvsTuKk3jvwuT9Xl6~%3BM7sv6HftLWv1K~%3BsL~_YRwXyob~%3BC~%3BPWfqujT5L7vgv43jz7q~%3BGvW5uG8L9~%3Be~_~%3BXljX74fjzQP~%3BOM3S~%3B27Qf~_~_kmHH76nXn0V6lsjP2XegXn6a~_SV7MMf~_idGXvLlNcBN3Mh~%3BuD8N7yN5v~_J~_~%3Bg~%3BS2z~%3BzXbYjh98b3peSN8F7Yr6N~_cf7Be9X~%3BR8UQsUf.bps.a.484959355319247&type=1&__xts__[0]=68.ARC6fIHVyfA7Xo3m9MzK2UMK_5zPf7En9IKyoKfHS5TQdrIuAzVUbJoUgpHWUZKeqdawRdSIrPnRNmbTg3T-ctW0exs9E36ZRfaKxMXZzrKNfSKL6EOL86ibYKlGnCixYo3CJ79fiz8o6sJaGW6WRAHtrKr9zWeRhjQgHa0c7Vh6dlvEPe4ZaVqhJ4wYl-UdU0gH5W11AA&__tn__=HH-R)がわかりやすいです。

[**RISE Camp - RISE Camp**  
_RISE Camp ​is ​a bootcamp ​organized ​by ​the ​UC ​Berkeley ​RISELab ​where ​you ​can get exposure to research and…_risecamp.berkeley.edu](https://risecamp.berkeley.edu/ "https://risecamp.berkeley.edu/")[](https://risecamp.berkeley.edu/)

\[2018/11/29追記\]  
動画とTutorial用のバイナリが公開されました

[**ucbrise/risecamp**  
_RISECamp Tutorials. Contribute to ucbrise/risecamp development by creating an account on GitHub._github.com](https://github.com/ucbrise/risecamp/releases/tag/rc18diy-v1 "https://github.com/ucbrise/risecamp/releases/tag/rc18diy-v1")[](https://github.com/ucbrise/risecamp/releases/tag/rc18diy-v1)

\[/追記終わり\]

RISELabはSparkで有名なAMPLabの後継となる研究室で、彼らが作るML関連のライブラリ・フレームワークのハンズオンをするというのが会の趣旨です。

![](/img/1__NZTxwssCMLDZDv2Km1M1Hg.jpeg)
![RISELabのStack](/img/1__X7a1O3wc38JN97nSzJph7Q.jpeg)
RISELabのStack

上の図のオレンジと緑の部分が彼らが作っているフレームワークになるのですが、その中でも以下のものについての紹介がありました。

*   RAY, RLlib, Tune: Pythonの分散処理フレームワークRAYと、それを使った強化学習ライブラリRLlib、パラメータチューニング用のライブラリTune
*   Flor: MLのモデル作成のための実験をtrackingするためのライブラリ
*   Clipper: MLモデルのServing用のAPIサーバを立てたり管理するためのライブラリ
*   PyWren: AWS Lambdaを使った並列処理のためのライブラリ
*   Opaque: Apache Sparkを使った暗号化したDataFrameを処理するライブラリ
*   WAVE: Decentralised authorization for IoT

### tl;drという名の感想

*   機械学習エンジニアリングは複雑で、モデルのデプロイ・サービング、実験の再現性やトレーサビリティはプロダクションへの重要なパートになる気がする。[MLFlow](https://mlflow.org/)や[Kubeflow](https://github.com/kubeflow/kubeflow)もそういったMLOpsの部分を狙っている
*   機械学習のワークロードはすべてPythonでやるぞという意気込みを強く感じた。会場からはSparkとどう連携するの？みたいな話もよく出たが、PySparkで一応…みたいな答えが多かった。特に [cloudpickle](https://github.com/cloudpipe/cloudpickle) を使ってオブジェクトばらまいて並列分散処理をすればいいじゃんという発想は単純ながら力強い。そして、Apache Arrowでノードのworker間のshared memory作るというのは今どきだなと。PythonはDSLとして便利なポジションになってるのかなぁ

たまたま、帰りの飛行機で聞いたTWML AI podcastでもこんな話が出ていました。

以下、ざっとハンズオンを行った順に紹介をしていきます。

### RAY, RLlib, Tune

[**ray-project/ray**  
_A system for parallel and distributed Python that unifies the ML ecosystem. - ray-project/ray_github.com](https://github.com/ray-project/ray "https://github.com/ray-project/ray")[](https://github.com/ray-project/ray)

RAYはこのRISELabのセットの中での基礎となるフレームワークです。READMEにもある通り、以下のようなdecoratorを書くだけでPythonの処理を並列・分散処理できるというコンセプトのものになります。

![](/img/1__FfKig9pDJRJZv4rtEBYyaA.png)

MLの処理をDSLとして抽象化します。特徴としては、

*   FunctionをTasksとして
*   ClassをActorsとして

として、Actorモデルを使って並列処理を行います。 `@ray.remote` というデコレータを書くと、その関数はRAYのWorkerで実行されるという仕組みです。

![](/img/1__ZRoARnXmvmlN__SBwDGXhsg.jpeg)

ポイントとしては、Pythonのobjectをcloudpickleというpackageを使ってserializeしてWorkerに投げてしまうということです。裏側にはノードごとのshared memoryとしてApache Arrowもいるため、Workerの共用メモリとしてオブジェクトを格納します。データの並列化どうするんだろうなと思ったら、ModinというPandas on Rayというライブラリも開発しているようです。”Modin is a DataFrame for datasets from 1KB to 1TB+”と言っているので、皆が困っているサイズ感のDataFrameを扱えるようになるかもしれません。

[**modin-project/modin**  
_Modin: Speed up your Pandas workflows by changing a single line of code - modin-project/modin_github.com](https://github.com/modin-project/modin "https://github.com/modin-project/modin")[](https://github.com/modin-project/modin)

![](/img/1__wNA1IPu9X2ICC9GzIOvzqA.jpeg)

チュートリアルは、こちらのrepoと同じものを実際にJupyterLabでハンズ・オンしました。

[**ray-project/tutorial**  
_Contribute to ray-project/tutorial development by creating an account on GitHub._github.com](https://github.com/ray-project/tutorial "https://github.com/ray-project/tutorial")[](https://github.com/ray-project/tutorial)

RAY自体はなるほど、と思って生々しいコードを書いていたのですが、それをベースにした[RLlib](https://github.com/ray-project/ray/tree/master/python/ray/rllib)という強化学習のライブラリと[Tune](https://github.com/ray-project/ray/tree/master/python/ray/tune)というパラメータチューニング用のライブラリを使ってみて、隠蔽されたアプリケーションとして使うとML用の並列処理を行うのには良いなと感じました。

![](/img/1__Va8PIW3Bx__G5FJas3kDatA.jpeg)

なお、WorkerのPythonのdependencyはあらかじめ解決した上で走らせてねということなので、複数プロジェクト走らせたりするのにはまだまだ自前で頑張る部分がありそうです。

### Clipper

Clipperは、MLの予測のためのAPIサーバを簡単にデプロイできるようにするためのライブラリです。

[**ucbrise/clipper**  
_A low-latency prediction-serving system. Contribute to ucbrise/clipper development by creating an account on GitHub._github.com](https://github.com/ucbrise/clipper "https://github.com/ucbrise/clipper")[](https://github.com/ucbrise/clipper)

コンセプトとしてはData scientistにパフォーマンスが気になる本番のAPI部分のコードを書かせることなく、スケーラブルなAPIサーバをコンテナベースでデプロイできるようにするということです。基本的には対応しているPythonのMLライブラリであれば、Dockerfileも書かないで予測の処理のコードを書いて、それをPythonからデプロイするという流れになります。

また、内部ではPrometheusのコンテナも立ち上げて、特定のmetricsをトラッキングできるようになっています。

### Flor

Florは機械学習の実験のトレーサビリティを上げ、再現性を高めるためのライブラリになります。

[**ucbrise/flor**  
_Build, configure, run, and reproduce experiments with Flor. - ucbrise/flor_github.com](https://github.com/ucbrise/flor "https://github.com/ucbrise/flor")[](https://github.com/ucbrise/flor)

機械学習では、feature engineeringなどのデータの加工をしたり、パラメータの探索をしたりしながらパイプラインを作っていきます。そこで、よくあるのが過去のパイプラインを再現したいのに、既にobjectが上書きされていて戻せないといったことがあります。Florでは、それを再現可能にするために色々と補助をしてくれます。

![](/img/1__NQsxJzTYwsHcRRdCy9SCdQ.jpeg)

少しFlor流の書き方をしないといけないのですが、それをすることで実験同士の処理のdiffを見たり、処理のパイプラインを可視化したり、他の人から引き継いだ実験の中間データを後から再度取得したりすることができます。

![](/img/1__esjnYs5wLhZ9VicWXgiivg.jpeg)

MLでは実験のreproducibilityをどう作るのかという話がよく話題にあがるため、その一つのアプローチとして良いのではないでしょうか。ただ、大きいデータになったときの中間データを効率的に保存できるかは少し気になりました。

### PyWren

[http://pywren.io/](http://pywren.io/)

PyWrenは、AWS Lambdaのようなサーバレスアーキテクチャを使って並行処理を行うためのフレームワークです。（まだ、GCPやAzureでは動かないっぽい）

以下はパラメータチューニングのノートブックですが、mapとfilterで処理を並列にばらまくことで分割しています。

また、これだけではなくNumPyWrenというNumpyの処理を同様に並列化するというプロジェクトも進んでいるようです。

PyWrenに関してはLambdaのアップロードできるイメージ？のサイズの制限があるため、shared objectを外部サーバに出したりと充実したPython Package周りを入れるために工夫をしているようです。

### Opaque

[**ucbrise/opaque**  
_A data analytics platform with strong security. Contribute to ucbrise/opaque development by creating an account on…_github.com](https://github.com/ucbrise/opaque "https://github.com/ucbrise/opaque")[](https://github.com/ucbrise/opaque)

OpaqueはSparkSQLをHardware Enclaves (Intel SGX, AMD SEV etc)の上で走らせて、セキュアな分析を可能にするものとのことです。チュートリアルでは、病気に関するデータセットを使ってSpark DataFrameを処理しましたが、まだScalaでしか動かないようです。

![](/img/1__Oo2duV6e19Vu66svgpU9ZQ.jpeg)

### WAVE

IoTのための中央集権型ではない認可のための仕組みです。

[**WAVE - RISE Lab**  
_WAVE is a global-scale fully-decentralized authorization system that operates with no central authorities yet permits…_rise.cs.berkeley.edu](https://rise.cs.berkeley.edu/projects/wave/ "https://rise.cs.berkeley.edu/projects/wave/")[](https://rise.cs.berkeley.edu/projects/wave/)

RISECamp 2017の動画

チュートリアルでは、二人の人がペアになって、それぞれのスマートホームを模したライトや温度センサーに対して変更や読み取りの権限を与えて操作をするということを行いました。

これだけだと、なんでこの流れでこれが紹介されるの？と思いましたが、最後に行ったRay, Clipper, Flor, WAVEの統合ハンズオンでは、RayとRLlibでpongの強化学習を行うための予測モデルを作り、Clipperでモデルをデプロイし、更にそのモデルの予測のための権限をWAVEで管理するという形でした。予測モデルの権限管理をするという発想があまりなかったので興味深かったです。

スライドやVideoはまだ出ていませんが、当日YouTube Liveでも中継していたので、そのうち[公式チャンネル](https://www.youtube.com/channel/UCP2-wiA964pif0secCpPbfw)に上がると思います。

あと、JupyterLab/Jupyter Notebookでのハンズオンを二日間フルでやりましたが、FIXMEを残しておいて修正したらassertでうまくいったかチェックをするというスタイルは、自分でも進捗を確認しやすいので良かったなと思います。