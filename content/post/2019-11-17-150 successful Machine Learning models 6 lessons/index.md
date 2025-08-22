---
authors:
- aki
date: '2019-11-16 13:15:00-08:00'
keywords:
- model
- 予測
- 高速化
- ラベル
- 頻度
- kpi
- high
- 'true'
- 論文
- sparse
lastmod: '2019-11-26 09:25:00-08:00'
recommendations:
- /post/2019-12-09-facebook prophet-plot/
- /post/2018-05-17_mlse-kickoff/
- /post/2025-05-02-ml-project-and-scrum/
summary: Booking.comの話題の論文から気になるところをメモ
tags:
- MLOps
- MachineLearning
- Paper
title: '150 successful Machine Learning models: 6 lessons learned at Booking.comのメモ'
---

![](https://images.unsplash.com/photo-1571942790878-b43e71f29476?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

各所で話題のBooking.comがKDD2019で発表した論文のメモ

元論文: [https://www.kdd.org/kdd2019/accepted-papers/view/150-successful-machine-learning-models-6-lessons-learned-at-booking.com](https://www.kdd.org/kdd2019/accepted-papers/view/150-successful-machine-learning-models-6-lessons-learned-at-booking.com)

# 何を予測しているのか

- Traveler preference model
- Traveler Context Model
    - 家族なのか、カップル、友達同士か、ビジネスか観光か、など
    - 家族判定をすると子供の入力を促す
- Item space navigation model
- User interface optimization model
- Content curation
    - これだけきいてなかった
- Content Augumentation

# 3 MODELING: OFFLINE MODEL PERFORMANCE IS JUST A HEALTH CHECK

MLCTで昔からグノシーの関さんが言っていた話だが、実際にモデルの精度改善とKPIとが相関すらないのを図示していて良い。

あと、精度改善してもKPIはサチるからな、という話も言われてみればそりゃそうだ。

ProxyとなるKPI(CTR)に過剰に最適化しても、本当のビジネス指標のCVRは上がらない、という話はCTRに寄せすぎた不快な広告の話を思い出す。

# 5 DEPLOYMENT: TIME IS MONEY

予測のレイテンシーが30%上がると0.5%CVRが下がったので、相関あるか見てみたよという話。

## 高速化のための手法

- Model redundancy: モデルをコピーしてクラスターにdistribute
- In-house developed Linear Prediction engine: 自前で線形予測エンジンを内製。内積を使うモデルを高速化
- Sparse model: パラメータ数が減ると計算時間が減る
- Precomputation and caching: 特徴空間が小さいときは予測結果をKVSに入れる。大きいときでも高頻度のリクエストをメモリにキャッシュする
- Bulking: ネットワーク負荷を減らすためにまとめて1リクエストにする
- Minimum Feature Transformation: 特徴計算の回数を減らして高速化する

なお、これらはシンプルなインターフェースでデプロイとmodelのconsumeができるように抽象化されており

- prediction latency
- high availability
- fault tolerance
- monitoring

をクリアしている。

## モニタリング: 教師なしの赤信号

- Issues for label dependent feedback
    - Incomplete feedback
        - 特定の条件下（予約時）ではtrueラベルがつくが、そうではない条件のときにtrueラベルがつかず発火しない
    - Delayed feedback
        - 数日〜数週間、数ヶ月後にしかtrueラベルが得られないケース。
- 教師なしのResponse Distribution Charts
    - 予測結果のhistogramで判断
    - 0-1の中心に高頻度の単峰性の山 → High bias model or high Bayes error in data
    - 極端に高頻度なmodeがあるとき → スケールミスか学習データの外れ値
    - ノイジーな分布は極端なsparse model
    - 双峰性の分布は2クラスをきちんと分類している
- 便利なヒューリスティクスだけど、modelが高品質かどうかはわからない
- estimators（regression?） or rankersには使えない

他で紹介されていないところを中心にメモしたが、論文直接読んだ方が面白い。