---
title: "Julia100本ノック"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-06-21T22:06:49+00:00
lastmod: 2014-06-21T22:06:49+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
[Julia vs Python: ビットコインオプションのモンテカルロシミュレーション](http://chezou.wordpress.com/2014/05/07/julia-vs-python-bitcoin-option/)に引き続き、[100 numpy exercises](http://www.loria.fr/~rougier/teaching/numpy.100/)という、面白いnumpyの練習問題があったのでそれのJulia版を作成しました。  
実際には46個しかないのと、numpyの便利関数がなくて挫折したものとかいくつかありますが、pythonistaな方々はオリジナルと比較してJuliaの世界に来ていただければ楽しいのではないかと思います。

この話で得たものをまとめて、[JuliaTokyo #1 - connpass](http://juliatokyo.connpass.com/event/6891/)で発表してこようと思います。  
コードは最後にgistのを貼るとして、発表するための雑感をメモしておきます。

## 調べるべき所

- [公式ドキュメント](http://julia.readthedocs.org/en/latest/)で検索
- 関連パッケージにないかどうかを調べる(from google)

  - 特に[StatsBase.jl](http://statsbasejl.readthedocs.org/en/latest/index.html)などの基本的なパッケージは調べると良い
- githubでissueを調べる
- Matlabではどう書くかを調べて、その関数名を調べる

  - [MATLAB Documentation - MathWorks 日本](http://www.mathworks.co.jp/jp/help/matlab/index.html)
- Numpyでどう書くかを調べてMatlabに変換する

  - [NumPy for MATLAB users – Mathesaurus](http://mathesaurus.sourceforge.net/matlab-numpy.html)
  - 他言語のドキュメント(英語)がわかると、特定の処理を検索するためのワードが分かって良い

## numpy, matlabとの比較

- matlab, numpyは歴史があるため充実した便利機能が沢山あることを実感
- Matlabはおろか、Pythonよりストイックな感じ

  - 「Matlabである○○はありませんか？」「No!それ高速に処理できないだろ！」
  - "removed pascal(matlabであった関数)"
  - 「これあると便利だと思うんだけど」「IMHO 一つのことを複数のやり方でやれるのはどうかと思う」
- たまに、独自の関数名をつけてきて辛い

  - `argmax`ならわかるのに`indmax`ってなんだよ(2014/06/22追記:`argmax`にrenameされそうな[動きがあるよう](https://github.com/JuliaLang/julia/pull/7327)です)

## code

[2014/06/22追記]

- レポジトリを作りました。最新のものはこちらをどうぞ [https://github.com/chezou/julia-100-exercises](https://github.com/chezou/julia-100-exercises)
- [notebook](https://nbviewer.ipython.org/github/chezou/julia-100-exercises/blob/master/julia-100-exercises.ipynb)を見えるようにしました。nbview便利すぎる

[2014/06/24追記]

- [MLに投稿](https://groups.google.com/forum/#!topic/julia-users/NquQLBRWHIU)しました。結構array comprehension使えという話が多く、vectorizeしない方がいいんだよ！というツッコミが新鮮です

[https://gist.github.com/chezou/5ec41ba0114370b05dcc](https://gist.github.com/chezou/5ec41ba0114370b05dcc)


