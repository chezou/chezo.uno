# Facebook Prophetのplotをmodelオブジェクトなしでする

Added By: Aki Ariga
Description: fbprophetの予測結果のグラフをmatplotlibだけでplotする
Tags: Python
Created at: December 9, 2019 12:36 AM
Last edited at: December 9, 2019 12:44 AM

![](https://images.unsplash.com/photo-1543286386-2e659306cd6c?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

Facebook Prophetを使っているときに、グラフのプロットは `model.plot()` などを使うと思います。しかし、 `model` が存在せずもとの訓練データと予測結果のデータだけあるときにプロットしたいという場合もあるかもしれません。

基本的には、以下のコードを再利用すればplotできます。

[facebook/prophet](https://github.com/facebook/prophet/blob/ca9a49d328ab1f2a991f246a3ebc37a7f9c896c5/python/fbprophet/plot.py#L41-L88)

実際のコードは以下の通り。

予測結果を `df` に、訓練データを `df_prev` に入れています。

[https://gist.github.com/chezou/71527cff1dc828f74d7f96a346b663a0](https://gist.github.com/chezou/71527cff1dc828f74d7f96a346b663a0)

気をつけないといけないのは、 `ds` カラムがきちんとソートしないといけないこと。

---

[Back to home](https://memo.chezo.uno/)