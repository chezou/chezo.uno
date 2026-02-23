---
authors: [aki]
date: '2020-03-01 02:17:00-08:00'
lastmod: '2020-03-01 17:00:00-08:00'
summary: pandas.NAに関連するmissing value周りのあれこれ
tags: [Python, pandas]
title: pandas 1.0 のpd.NAのハマりどころ
keywords: [pandas, int, na, 挙動, experimental, 登場, numpy, new, '64', documentation]
recommendations: [/post/2015-10-12-pyconjp-2015nican-jia-sita-number-pyconjp/, /post/2011-11-25-googlezhi-nozheng-gui-biao-xian-enzinre2wori-ben-yu-deshi-sitemita/,
  /post/2014-12-24-juliadeword-countsiteqi-duitakoto-number-juliaac/]
---

![[https://unsplash.com/photos/_7HU079sGNw](https://unsplash.com/photos/_7HU079sGNw)](https://images.unsplash.com/photo-1497514440240-3b870f7341f0?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

[https://unsplash.com/photos/_7HU079sGNw](https://unsplash.com/photos/_7HU079sGNw)

pandas 1.0.0 からexperimental featureとして登場した `pandas.NA` 。これは今まで0.x系では `numpy.nan` で表していた missing valueを `pandas.NA` で表現しようというもの。

この検索しにくい名前のおかげで、情報を探してもなかなかたどり着かないので苦労をする。公式の "What's new in 1.0.0" の "Experimental new features" の項と hkzmさんのQiitaの記事がよくまとまっているので困ったらここに立ち返るとよい。

[What's new in 1.0.0 (January 29, 2020) - pandas 1.0.1 documentation](https://pandas.pydata.org/docs/whatsnew/v1.0.0.html#experimental-new-features)

[pandas 1.0.0 (rc0) での pd.NA の特徴 - Qiita](https://qiita.com/hkzm/items/52195729e9b00ae88789)

この記事では、nullableなdtype周りでハマったことをまとめていく。

## そもそもなぜ `pandas.NA` が登場したのか

以下のドキュメントには、 `numpy.nan` 周りの説明がざらっと書いてある。特にcastされるときの挙動は今でも役に立つだろう。（というか昔の説明がなくなっているように思う）

[Frequently Asked Questions (FAQ) - pandas 1.1.0.dev0+609.g52a63ab42 documentation](https://dev.pandas.io/docs/user_guide/gotchas.html#nan-integer-na-values-and-na-type-promotions)

pandasを利用されている方は、このintからfloatへのcastに遭遇したことも多いだろう。pandas 0.24から[Nullable Integer type](https://pandas.pydata.org/pandas-docs/version/0.24.2/user_guide/integer_na.html) (`pandas.Int64Dtype()` いわゆる `Int64` 。 `int64` はnumpyのdtypeを指すので注意。 `Int32`, `Int16`, `Int8` もある) も登場し、Intのままで NaNを保持できるようになった。

```python
In [1]: arr = pd.array([1, 2, np.nan], dtype=pd.Int64Dtype())
# pd.array([1, 2, np.nan], dtype="Int64") でもOK
In [2]: arr
Out[2]: 
<IntegerArray>
[1, 2, NaN]
Length: 3, dtype: Int64
```

では、なぜpandasはfloatにデフォルトcastしているのだろうか？

実は、 `NaN` というのはIEEE 754でfloatと決まっているのである。

[NaN](https://ja.wikipedia.org/wiki/NaN)

だから、 `numpy.nan` もfloatだし、pandasはもともと `numpy.nan` があるとfloatのdtypeにcastしていたのである。IEEEで決まっていたら仕方がない。 `type()` を調べても `nan` は `float` になるわけだ。

```python
In [1]: np.nan
Out[1]: nan

In [2]: type(np.nan)
Out[2]: float

In [3]: float('nan')
Out[3]: nan

In [4]: type(float('nan'))
Out[4]: float
```

## `pandas.NA` の登場と、新しいdtypeの追加

仕方がないというわけにはいかないので、pandasは通称 `Int64` を導入したのである。しかしこれだけでは、 [`boolean` が `numpy.nan` や `pandas.NA` が入ると `object` にcastされてしまうのは続いている](https://dev.pandas.io/docs/user_guide/gotchas.html#na-type-promotions)。また、 `str` も `object` 型というなんでもごった煮のdtypeで扱いたくない。というので、pandas 1.0.0から `pandas.BooleanDtype()` (string表記は `"boolean"`)と `pandas.StringDtype()` (string表記は `"string"`)が登場した。また、合わせて `pandas.NA` も登場した。

つまり、nullableな型は以下のように遷移してきた。

- 0.23まで
    - `float`, `object`
- 0.24〜0.25
    - `float`, `object`, `Int64`, `Int32`, `Int16`, `Int8`
- 1.0以降
    - `float`, `object`, `Int64`, `Int32`, `Int16`, `Int8`,  `boolean`, `string`,

## Nullable Valueの有無でのハマりどころ

以下はpandas 0.23.4, 0.25.3と 1.0.1で比較をしている。最初は1.0前後で比較をしようとしたが、大きな変更は0.24の前後で変わっていたようである。

### `Int64` を指定したDataFrameで `numpy.nan` ではなく `pandas.NA` が返ってくる

0.25以前では `dtype="Int64"` を指定したときは、 `numpy.nan` がmissing valueとして返ってきた。

```python
In [13]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}], dtype="Int64")

In [14]: df
Out[14]:
   a  b    c
0  1  2  NaN
1  3  4    5

In [15]: df.c.iloc[0]
Out[15]: nan

In [16]: type(df.c.iloc[0])
Out[16]: float

In [18]: pd.np.isnan(df.c.iloc[0])
Out[18]: True
```

これが、以下のようになる。

```python
In [2]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}], dtype="Int64")

In [3]: df
Out[3]:
   a  b     c
0  1  2  <NA>
1  3  4     5

In [4]: df.c.iloc[0]
Out[4]: <NA>

In [5]: type(df.c.iloc[0])
Out[5]: pandas._libs.missing.NAType

In [6]: np.isnan(df.c.iloc[0])
Out[6]: <NA>
```

そうだよね、と思うだろうがこれに伴い以下の挙動が変わってきている。

### Noneへの置換をしたい場合

これは0.24で `Int64` 導入時からの挙動だが、 `Int64` のdtypeのcolumnは、手でNoneを代入すると `numpy.nan` や `pandas.NA` が保持される。これは `df.where` や `df.applymap` などで `numpy.nan` や `pandas.NA` を置換しようとしてもdtypeを変えないと `None` に置換できないということを意味する。 `df.replace` は `object` dtypeになる。

0.25.3の挙動

```python
In [25]: df
Out[25]:
   a  b    c
0  1  2  NaN
1  3  4    5

# cは何も変わらない
In [26]: df.where(pd.notnull(df), None)
Out[26]:
   a  b    c
0  1  2  NaN
1  3  4    5

# cがfloatにcastされてしまう
In [27]: df.applymap(lambda x: None if np.isnan(x) else x)
Out[27]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

# cはobject dtypeにcastされている
In [38]: df.replace({np.nan: None})
Out[38]:
   a  b     c
0  1  2  None
1  3  4     5

In [39]: df.replace({np.nan: None}).dtypes
Out[39]:
a     Int64
b     Int64
c    object
dtype: object
```

1.0.1での挙動

```python
In [2]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}], dtype="Int64")

In [7]: df
Out[7]:
   a  b     c
0  1  2  <NA>
1  3  4     5

In [3]: df.where(pd.notnull(df), None)
Out[3]:
   a  b     c
0  1  2  <NA>
1  3  4     5

# np.isnanはTypeErrorを返す（当たり前）
In [5]: df.applymap(lambda x: None if np.isnan(x) else x)
TypeError: boolean value of NA is ambiguous

# pd.isnullならOK。floatには変わる
In [6]: df.applymap(lambda x: None if pd.isnull(x) else x)
Out[6]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

# cはobjectに置換される
In [8]: df.replace({np.nan: None})
Out[8]:
   a  b     c
0  1  2  None
1  3  4     5

In [9]: df.replace({np.nan: None}).dtypes
Out[9]:
a     Int64
b     Int64
c    object
dtype: object
```

1.0.1でのNullableなtypeを使わない挙動

```python
In [27]: df2 = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}])

In [28]: df2
Out[28]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

# cはobjectになる
In [29]: df2.where(pd.notnull(df2), None)
Out[29]:
   a  b     c
0  1  2  None
1  3  4     5

In [30]: df2.where(pd.notnull(df2), None).dtypes
Out[30]:
a     int64
b     int64
c    object
dtype: object

# cはfloatになる
In [31]: df2.applymap(lambda x: None if np.isnan(x) else x)
Out[31]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

# cはobjectになる
In [33]: df2.replace({np.nan: None})
Out[33]:
   a  b     c
0  1  2  None
1  3  4     5

In [34]: df2.replace({np.nan: None}).dtypes
Out[34]:
a     int64
b     int64
c    object
dtype: object
```

まとめると以下の表のようになる。

|Name|non-nullable dtype|nullable dtype|
|---|---|---|
|df.where|object にcast|変化なし|
|df.applymap|float にcast|float にcast|
|df.replace|object にcast|object にcast|



### `df.to_dict(orient="record")` の挙動の罠

行ごとにデータを処理したいのであれば、 `df.to_dict(orient="record")` を使うことができる。 が、これは後述するように挙動がバージョン感で差異があったり、古いバージョンではちょっと想定と違う挙動をするので `df.to_records` を使うほうが良い。具体的には、0.23以前は、カラムごとに `nan` の有無でdtypeを変えることが期待されるが、行ごとにdtypeを揃えに行こうとするため、 `nan` がある行が含まれていると全行 `float` に変わってしまった。なお、1.0.1ではこの挙動は期待通りに修正されている。

**0.23.4**

```python
In [37]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}])

In [38]: df
Out[38]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

# 全部の値が numpy.float64 にキャストされている
In [39]: df.to_dict(orient="record")
Out[39]: [{'a': 1.0, 'b': 2.0, 'c': nan}, {'a': 3.0, 'b': 4.0, 'c': 5.0}]

In [40]: type(df.to_dict(orient="record")[0]['a'])
Out[40]: numpy.float64

In [41]: type(df.to_dict(orient="record")[0]['c'])
Out[41]: numpy.float64
```

**1.0.1**

```python
In [2]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}])

In [3]: df2 = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}], dtype="Int64")

In [4]: df
Out[4]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

In [5]: df2
Out[5]:
   a  b     c
0  1  2  <NA>
1  3  4     5

# Cのみfloatに、他はintのまま変換されている
In [6]: df.to_dict(orient="record")
Out[6]: [{'a': 1, 'b': 2, 'c': nan}, {'a': 3, 'b': 4, 'c': 5.0}]

# 基本、numpy.int64で保持されている
In [7]: df2.to_dict(orient="record")
Out[7]: [{'a': 1, 'b': 2, 'c': <NA>}, {'a': 3, 'b': 4, 'c': 5}]

In [9]: type(df.to_dict(orient="record")[0]['a'])
Out[9]: int

In [10]: type(df2.to_dict(orient="record")[0]['a'])
Out[10]: numpy.int64

In [11]: type(df.to_dict(orient="record")[0]['c'])
Out[11]: float

In [13]: type(df2.to_dict(orient="record")[0]['c'])
Out[13]: pandas._libs.missing.NAType
```

`df.to_records` を使った処理例は以下の通り。

**1.0.1**

```python
In [2]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}])

In [3]: df2 = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}], dtype="Int64")

In [4]: df
Out[4]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

In [5]: df2
Out[5]:
   a  b     c
0  1  2  <NA>
1  3  4     5

In [25]: df2.to_records(index=False)
Out[25]:
rec.array([(1, 2, <NA>), (3, 4, 5)],
          dtype=[('a', 'O'), ('b', 'O'), ('c', 'O')])

# listで受け取りたい場合
In [26]: list(df2.to_records(index=False))
Out[26]: [(1, 2, <NA>), (3, 4, 5)]

# コラム名を取得したい場合
In [27]: df2.to_records(index=False).dtype.names
Out[27]: ('a', 'b', 'c')

# nullableなdtypeを使わない場合の type
In [19]: list(map(lambda x: type(x), df.to_records(index=False)[0]))
Out[19]: [numpy.int64, numpy.int64, numpy.float64]

In [22]: list(map(lambda x: type(x), df.to_records(index=False)[1]))
Out[22]: [numpy.int64, numpy.int64, numpy.float64]

# nullableなdtypeを使った場合の type
In [23]: list(map(lambda x: type(x), df2.to_records(index=False)[0]))
Out[23]: [int, int, pandas._libs.missing.NAType]

In [24]: list(map(lambda x: type(x), df2.to_records(index=False)[1]))
Out[24]: [int, int, int]
```

**0.23.4**

```python
In [45]: df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}])

In [46]: df
Out[46]:
   a  b    c
0  1  2  NaN
1  3  4  5.0

In [47]: df.to_records(index=False)
Out[47]:
rec.array([(1, 2, nan), (3, 4,  5.)],
          dtype=[('a', '<i8'), ('b', '<i8'), ('c', '<f8')])

# 各値のtype
In [48]: list(map(lambda x: type(x), df.to_records(index=False)[0]))
Out[48]: [numpy.int64, numpy.int64, numpy.float64]

In [49]: list(map(lambda x: type(x), df.to_records(index=False)[1]))
Out[49]: [numpy.int64, numpy.int64, numpy.float64]
```

### dtypeの比較ができない場合がある

`Int64` などは `numpy.dtype` と比較できるが、 `boolean`, `string` とは比較できない。うっかり、DataFrameのdtypeごとに比較しようとすると死ぬ。

```python
In [60]: pd.Int64Dtype() == "boolean"
Out[60]: False

In [61]: pd.Int64Dtype() == "Int8"
Out[61]: False

In [62]: np.dtype('float64') == "Int8"
.venv-10/bin/ipython:1: DeprecationWarning: Numeric-style type codes are deprecated and will result in an error in the future.
  #!/Users/aki/src/pytd/.venv-10/bin/python3.7
Out[62]: False

In [59]: np.dtype('float64') == "boolean"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-59-bc057c799968> in <module>
----> 1 np.dtype('float64') == "boolean"
```

これは回避の仕方が見つかっていない。

## まとめ

当初は `pandas.NA` の挙動を調べるつもりで1.0前後の差異を調べたが、気がつけばすでに0.24のときに変わっていたことがわかった。1.0内での挙動も違ったりするし、 `StringDtype` などは experimental featureなので挙動は今後も変わりうる。msgpackへの変換などでPythonのpremitive型に変換するのは気をつける必要がありそう。