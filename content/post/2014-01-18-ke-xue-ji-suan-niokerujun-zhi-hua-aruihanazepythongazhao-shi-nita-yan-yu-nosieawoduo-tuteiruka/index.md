---
title: "科学計算における均質化、あるいはなぜPythonが着実に他言語のシェアを奪っているか"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-01-18T02:01:18+00:00
lastmod: 2014-01-18T02:01:18+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
最近、何故科学計算でPythonがほぼ一人勝ちなのか気になっていたのですが、[TAL YARKONI](http://www.talyarkoni.org/blog/author/admin/)氏による、[THE HOMOGENIZATION OF SCIENTIFIC COMPUTING, OR WHY PYTHON IS STEADILY EATING OTHER LANGUAGES’ LUNCH](http://www.talyarkoni.org/blog/2013/11/18/the-homogenization-of-scientific-computing-or-why-python-is-steadily-eating-other-languages-lunch/)という記事が、その答えに近づける鍵なのかもしれないと思い、試訳をしてみました。  
彼は心理学とニューロイメージングを専門とする研究者であり、元々Rを中心に様々な言語を利用していたのですが、最近ではPythonばかり使うようになってきたとのことです。

(更なる議論としては、[redditでの議論](http://www.reddit.com/r/Python/comments/1qxalh/the_homogenization_of_scientific_computing_or_why/)も興味深いです。)

訳すこと自体が初めてで拙い訳だとは思いますが、間違い等がありましたらコメント等で指摘ください。  
翻訳の公開を快諾していただいたYARKONI氏、翻訳のアドバイスをいただいたmrkn氏に感謝します。

* * *

ここ2年で、私の科学計算のツールボックスが着実に均質化している。  
2010,2011年くらいは、私のツールボックスは以下のものを使っていた。

- Ruby: テキスト処理や雑多なscripting
- Ruby on Rails/JavaScript: Web開発
- Python/Numpy(たまにMATLAB): 数値計算
- MATLAB: ニューロイメージング&lt;sup id=&quot;fnref-1674-neuroimaging&quot;&gt;&lt;a href=&quot;#fn-1674-neuroimaging&quot; rel=&quot;footnote&quot;&gt;1&lt;/a&gt;&lt;/sup&gt;データの解析
- R: 統計的分析
- R: プロット、可視化
- それ以外のもののために、他の言語/環境の開拓

2013年には、こうなっている

- Python: テキスト処理や雑多なscripting
- Ruby on Rails/JavaScript: Web開発。DjangoやFlask(Pythonのフレームワーク)もたまに使う
- Python (Numpy/SciPy): 数値計算
- Python (Neurosynth, NiPyなど): ニューロイメージングデータの解析
- Python (Numpy/SciPy/pandas/statsmodels): 統計的分析
- Python (MatPlotLib): プロット、可視化(Webベースの可視化にはJavaScriptのd3.jsを使う)
- Python (scikit-learn): 機械学習
- 他言語の開拓は顕著に減った

もうお分かりだろう。

私が使うツールの均質化(Pythonification?)が進むことで、定期的に最近のPythonのエコシステムの驚くべき成長について考えるようになった。数年前までは、多くの時間を髪をかきむしりPythonがもっとRライクなら良かったのにと祈ることに費やさない限り、Pythonでは本当の統計を扱うことはできなかった。(そしてそれは、[Rがなんであるか](http://www.talyarkoni.org/blog/2012/06/08/r-the-master-troll-of-statistical-languages/)を考えていることを告白するに等しい)  
ニューロイメージングデータはSPM(MATLABベース)やFSLなどの様々なパッケージで解析されるが、完全な機能を持って、フリーで、オープンソースなPythonの代替になるものはなかった。機械学習や、自然言語処理、Webアプリーケーションの開発のためのパッケージは出現し始めたばかりだった。

今日では、科学計算のあらゆる方面のためのツールがPythonならすぐに手に入る。そしてますます多くの事例で、競合の美味しいところを奪っている。

Rを例にとって考えてみよう。Rが手軽にそのまま使えるというメリットは、大量のメモリを必要とするデータセットに対しては適応できない弱点として認識されていた(もちろん、あなたが時間を投資するなら[回避する](http://cran.r-project.org/web/views/HighPerformanceComputing.html)ことができることは知っているが、多くの科学者は時間がない)。しかし、Rが大規模データに首を締められる方法や言語としての間抜けさを嫌っている人たちでさえも、しばしば迅速で重大なデータ処理が求められた時にRに戻らざるを得なかった。頑張ってPythonや他の高級言語にピボットや集約、整形、粉々にするためのコードを書くことはできたが、それをしようと思ったか？Rの[plyr](http://cran.r-project.org/web/packages/plyr/index.html)のような美しいパッケージは、他言語では実装に何時間もかかる処理を、2,3行のコードで実現できる。否定的な側面としては、学習曲線がそれぞれのパッケージの比較的複雑なAPIを学習するのに密接に関わる(例えばggplot2は信じられないほど表現力が高いが、学び直すのに毎回3ヶ月はかかる)。そして、Rの全般的なぎこちなさについて取り組まなければならない。しかし、概して明らかにその価値はあった。

現在に戻って考えよう。先週、誰かが2,3年前私がRで書いたシミュレーションコードについて聞いてきた。私は、それらについて調べるためにR Studioを叩いたが、R Studioをとても長い時間使っていないように思えた(実際には6ヶ月にみたない期間だと思うが)。NumPy/SciPyとMatPlotLib, pandas, statsmodelsの組み合わせはRを効果的に置き換え、そのことにすら気づいていなかった。あるときから、&quot;本当の&quot;データ分析が必要なときに、Pythonから逃げRを使うことをやめた。その代わり、pandasとstatsmodelsに自分のコードを移行することを始めた。そしてそれと同様のことが、機械学習(scikit-learn),自然言語処理(nltk),ドキュメントパース(BeautifiulSoup)、そして多くの他のPython以外で処理していたことで起こった。

開発や分析のすべてを一つの言語で行うことには、結局かなりの利点がある。第1には、1つの言語であらゆることができるようになると、Rubyは内包表記の代わりにブロックを使う、Pythonではarrayのサイズを取得するのにlen(array)をarray.lengthの代わりに使うなど、認知的な[切り替えコスト](http://en.wikipedia.org/wiki/Task_switching_(psychology))がなくなる。認知的なオーバーヘッドを最小限にして問題を解けばよくなる。もちろん、違うプロジェクトの異なる言語間でのインターフェースについて心配する必要もなくなる。Pythonでテキストをパースして、そして最終的に求める内部フォーマットにし、RやMATLABに他の分析をさせるために異なるフォーマットでディスクに書き出すことほどいらいらすることはない&lt;sup id=&quot;fnref-1674-footnote1&quot;&gt;&lt;a href=&quot;#fn-1674-footnote1&quot; rel=&quot;footnote&quot;&gt;2&lt;/a&gt;&lt;/sup&gt;。さらに、これらの類のことは重大なことではない。PythonからCSVやJSONを長時間かけて書き出して、Rに読み込むことはなくなる。しかし、それは納得がいく。統合的な開発はより複雑さを増す。なぜなら、益々多くのコードがディスクの中のあちこちに散らばるからだ(少なくともあなたが私の整理整頓能力と同じならば)。  
これでは、インターフェースのためのつまらないラッパーを書くという「データ分析(笑)」で日が暮れてしまう。本来データをどう変換し、扱うべきかを考える代わりに。  
つまり、あなたの美しい分析のためのコードが、醜いopen(), read()といったI/Oコールにまみれてしまうのだ！これらのオーバーヘッドすべてが、単一言語で書けば瞬く間に消える。

便利さは別としても、もう一点付け加えると、Pythonの科学計算のエコシステムではすさまじい量のPythonベースのツールが存在する。これらは、現段階でクラス最高のスコープ、使いやすさ、(Cバインディングの美徳であるところの)パフォーマンスを実現している。scikit-learnより使いやすい機械学習パッケージは想像できない。scikit-learnは、幅広いアルゴリズムが実装されており、[ドキュメントも素晴らしく](http://scikit-learn.org/stable/documentation.html)、[性能も傑出している](http://gael-varoquaux.info/blog/?p=169)。同様に、pandasに移行してからRのデータ操作の機能を恋しくなったことはない。実際に、Rでは知らなかった新しいトリックをpandasで見つけ出している(それについてはいつか書こうと思う)。pandasが[Rの性能をかなり超えている](http://wesmckinney.com/blog/?p=414)ことを考えても、Rや他のツールに戻る理由がどんどん減っている。

気をつけて欲しいのが、私は他言語で行ってきたこと _すべてを_ Pythonで実装しろと言っているわけではない。それはもちろん正しくない。例えば、いくつものRにあるような統計的なパッケージの代替になるものがない(lme4のPythonで使えるものがあれば、私に教えて欲しい)。信号処理の分野では、多くの人々がPythonで替えの効かないMATLABのツールボックスやパッケージとべったりだと思う。シビアな性能を求められる人や、とてもとても巨大なデータセットに対して取り組んでいる人にとっても、低級なコンパイル言語における非常に最適化されたコードの代替にはならない。従って、言うまでもなく私の言っていることがすべての人に適用されるわけではない。しかし、多くの科学者には受け入れられると睨んでいる。

個人的には、私のやることの90-95%がPythonで快適にこなせる所まで来ている。どの言語を新規プロジェクトで使用するかを決定するときに、「学びたい/使用に耐えられる中でのベストなツールは何か？」から「本当にPythonでやる方法はないのか？」と考えるようになってきている。時にはマイナス面があるということは否定しないけれど、概してこの考え方は良いことである。例えば、ほとんどのデータ分析をRで行っていた時代だったら、いろんな統計的なパッケージについて何をしているかを調べるためにこねくり回していたと思う。そんなことはもうしたくない。目的のない統計的な探求より、Rの知識をリフレッシュする苦痛に耐えるほうがマシだ。逆に、ただ単純に言語的な純粋さを保つために、他の言語より好きではなくても結局Pythonのパッケージに行き着く場合もある。例えば、RailsのORMであるActiveRecordは、明らかにPythonのSQLAlchemyより好きだ。でも、同一のアプリケーションでPythonとRubyのコードを混ぜることは許しがたい。明らかにコストはかかる。しかし、それはかなり小さいコストであり、個人的には、Pythonをほとんど全てに使うことで気にならなくなる。同じ経験をしてきた研究者を多く知っているし、これを提案することは不公平であるとは思わないが、今となってはPythonは多くのドメインにおける科学計算でデファクトとなりつつある。もしこれを読んでいるあなたがPythonに触れたことがなければ、今はじめるしかない！

追記:  
この記事を書き始めてから書き終わるまでに(2週間くらいだろう)、2つのPythonベースのデータ可視化のパッケージを新しく見つけた。  
Michael Waskomの[seaborn package](https://github.com/mwaskom/seaborn)(複雑な図をとても高度に抽象化してggplot2のように美しく書くことができる)と、Continuum Analyticsの[bokeh](https://github.com/ContinuumIO/Bokeh)(これはwebベースの可視化&lt;sup id=&quot;fnref-1674-footnote2&quot;&gt;&lt;a href=&quot;#fn-1674-footnote2&quot; rel=&quot;footnote&quot;&gt;3&lt;/a&gt;&lt;/sup&gt;を大きく変える可能性を持っている)である。Pythonのエコシステムのスピードを考えると、自分の考えを分析コードに直接してくれるPythonパッケージを使う時が来ることも夢ではないかもしれない。

  

* * *
  

1.   
訳注:[Wikipedia](http://en.wikipedia.org/wiki/Neuroimaging)&amp;nbsp;↩  
2.   
PythonとR等の間に、オブジェクトを内部的にやりとりできる様々なインターフェースがあることは知っている。私の経験上、これらは断然ポジティブではないし、常に複数の言語をまたぐために余計なコードを書く手間は依然として残っている。&amp;nbsp;↩  
3.   
そう、あなたが聞いたことは間違っていない。Pythonを使ってwebベースの可視化をするのだ。Bokehは静的なJavaScriptとJSONをPythonから生成する。あなたはネイティブなJSコードを書くこと無く、魅惑的な図をウェブページでユーザに見せることができるのだ。&amp;nbsp;↩  


