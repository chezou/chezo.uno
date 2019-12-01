---
title: "KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-07-15T12:07:29+00:00
lastmod: 2011-07-15T12:07:29+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
**[2011/07/23追記]  
SWIGで生成したmykytea\_wrap.cxxをgithubに追加したので、SWIGのインストールは必要なくなりました。それに伴い実行すべき事が当初と変わっています。**

KyTeaという[@neubig](http://twitter.com/neubig)さんが作られた、テキストの形態素解析や読み付与ができるツールがあります。

[KyTea (京都テキスト解析ツールキット)](http://www.phontron.com/kytea/index-ja.html)  
処理のイメージですが、少し前のバージョンの物ですが[@nokuno](http://twitter.com/nokuno)さんの[紹介記事](http://d.hatena.ne.jp/nokuno/20100307/1267923299)がわかりやすいと思います。

これをRubyやPythonなどのLLで使えることができれば、Webアプリとかでも使えるようになって嬉しいのでは、と思いラッパーを書いてみました。  
Ubuntu 11.04, KyTea v0.3.1, SWIG 2.0.1&amp;nbsp; Ruby 1.8.7, 1.9.2, Python 2.7.1にて動作を確認しています。  
KyTeaと同じApache Licence 2.0でお使いください。

Ruby向け： [Mykytea-ruby@github](https://github.com/chezou/Mykytea-ruby)  
Python向け： [Mykytea-python@github](https://github.com/chezou/Mykytea-python)

# 

Mykyteaの使い方

## kyteaをダウンロード＆インストール
[こちら](http://www.phontron.com/kytea/index-ja.html#download)を参考にダウンロード＆インストール

    wget http://www.phontron.com/kytea/download/kytea-0.3.1.tar.gz tar -xzf kytea-X.X.X.tar.gz cd kytea-X.X.X ./configure make sudo make install kytea --help

うちの場合、「libkytea.so.0が見つからない」といわれたので、LD\_LIBRARY\_PATHを/usr/local/libに通しました。

    export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/usr/local/lib

**[2011/07/17追記]**

    sudo ldconfig

こうすれば良いだけだったんですね。。。参考URL：[GETAssoc インストール/MeCabのインストール](http://getassoc.cs.nii.ac.jp/?%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%2FMeCab%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)

## SWIGをインストール
**[2011/07/23追記]  
SWIGで生成したmykytea\_wrap.cxxをgithubに追加したので、SWIGのインストールは必要なくなりました。**  

SWIGは、異なる言語へラッパーを作るのをサポートしてくれるソフトです。今回はこれを使ってラッパーを作成しました。  
SWIGを使えば、javaやperlなどの他の言語のラッパーも作れるはずです。

今回は、SWIGのバージョン1.x系列ではRuby1.9.2向けのラッパーが作れなかったため、2.x系列をインストールします。

    sudo apt-get install swig2.0

## githubからMykyteaをダウンロード
git cloneでソースを入手します。

    git clone git://github.com/chezou/Mykytea-ruby.git

もしくは、githubからブラウザでDownloadしてください。python版はrubyをpythonに読み替えてください。

## Mykyteaの共有ライブラリを作成する
ダウンロードしたソースに対して、共有ライブラリを作成します

**[2011/07/23追記]  
SWIGで生成したmykytea\_wrap.cxxをgithubに追加したので、SWIGの実行は必要なくなりました。もしmakeに失敗したら、最初に下記を実行してください。**

    swig2.0 -c++&amp;nbsp; -ruby -I/usr/local/include mykytea.i

(pythonの場合は下記)

    swig2.0 -c++ -python -I/usr/local/include mykytea.i

- Rubyの場合

    ruby extconf.rb make

- Pythonの場合
**[2011/07/23追記]  
setup.pyを追加しましたので、pytonの場合は以下を実行してください**    

    python setup.py

下記はmake方法です。

    swig -c++ -python mykytea.i g++ -c mykytea\_wrap.cxx -I/usr/include/python2.7 g++ -c mykytea.cpp g++ -shared mykytea.o mykytea\_wrap.o -o \_Mykytea.so -lkytea

**-I/usr/include/python2.7** の部分は適宜バージョンなどによって場所を読み替えてください。  
 (ちなみに、python版に入っているなんちゃってMakefileはpython2.7でしか通りませんorz  
 autoconfの使い方が分からない…)

## 動作を確認する

- Rubyの場合

&gt; ruby mykytea\_test.rb

- Pythonの場合

    python mykytea\_test.py

でテストプログラムを実行してください。  
下記のような実行結果が得られるはずです。(注釈はでません)

&gt; #分かち書きの結果を出力  
&gt; 今日  
&gt; は  
&gt; い  
&gt; い  
&gt; 天気  
&gt; で  
&gt; す  
&gt; 。
&gt; 
&gt; #タグ付き結果を文字列で出力  
&gt; 今日/名詞/きょう は/助詞/は い/形容詞/い い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。
&gt; 
&gt; #表層及び1位のタグとスコアを出力  
&gt; 今日&amp;nbsp;&amp;nbsp;&amp;nbsp; /名詞/3.2847062802112355&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /きょう/1.3268831168939792  
&gt; は&amp;nbsp;&amp;nbsp;&amp;nbsp; /助詞/3.924858405365926&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /は/100.0  
&gt; い&amp;nbsp;&amp;nbsp;&amp;nbsp; /形容詞/2.591390241156937&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /い/100.0  
&gt; い&amp;nbsp;&amp;nbsp;&amp;nbsp; /語尾/2.155161693042765&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /い/100.0  
&gt; 天気&amp;nbsp;&amp;nbsp;&amp;nbsp; /名詞/4.7486561215119565&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /てんき/100.0  
&gt; で&amp;nbsp;&amp;nbsp;&amp;nbsp; /助動詞/2.8068949386999753&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /で/100.0  
&gt; す&amp;nbsp;&amp;nbsp;&amp;nbsp; /語尾/2.7237397162868087&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /す/100.0  
&gt; 。&amp;nbsp;&amp;nbsp;&amp;nbsp; /補助記号/3.3392877514055774&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /。/100.0
&gt; 
&gt; #表層と、全てのタグとそのスコアを出力  
&gt; 今日&amp;nbsp;&amp;nbsp;&amp;nbsp; /名詞/3.2847062802112355&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/0.0&amp;nbsp;&amp;nbsp;&amp;nbsp; /代名詞/-0.12999710377780294&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /きょう/1.3268831168939792&amp;nbsp;&amp;nbsp;&amp;nbsp; /こんにち/0.0  
&gt; は&amp;nbsp;&amp;nbsp;&amp;nbsp; /助詞/3.924858405365926&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-3.6483403104137224e-17&amp;nbsp;&amp;nbsp;&amp;nbsp; /代名詞/-0.23536067702781097&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /は/100.0  
&gt; い&amp;nbsp;&amp;nbsp;&amp;nbsp; /形容詞/2.591390241156937&amp;nbsp;&amp;nbsp;&amp;nbsp; /動詞/0.0&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-0.00428323670492603&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /い/100.0  
&gt; い&amp;nbsp;&amp;nbsp;&amp;nbsp; /語尾/2.155161693042765&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-3.946495907847236e-17&amp;nbsp;&amp;nbsp;&amp;nbsp; /web誤脱/-0.23382596743536913&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /い/100.0  
&gt; 天気&amp;nbsp;&amp;nbsp;&amp;nbsp; /名詞/4.7486561215119565&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-9.215718466126788e-18&amp;nbsp;&amp;nbsp;&amp;nbsp; /web誤脱/-0.18273736539912366&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /てんき/100.0  
&gt; で&amp;nbsp;&amp;nbsp;&amp;nbsp; /助動詞/2.8068949386999753&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-1.5937771935536915e-17&amp;nbsp;&amp;nbsp;&amp;nbsp; /動詞/-0.21163142806550297&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /で/100.0  
&gt; す&amp;nbsp;&amp;nbsp;&amp;nbsp; /語尾/2.7237397162868087&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/-1.4690939437178585e-17&amp;nbsp;&amp;nbsp;&amp;nbsp; /代名詞/-0.36184293534455636&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /す/100.0  
&gt; 。&amp;nbsp;&amp;nbsp;&amp;nbsp; /補助記号/3.3392877514055774&amp;nbsp;&amp;nbsp;&amp;nbsp; /言いよどみ/1.9136168344369153e-17&amp;nbsp;&amp;nbsp;&amp;nbsp; /代名詞/-0.268961070659961&amp;nbsp;&amp;nbsp;&amp;nbsp; &amp;nbsp;&amp;nbsp;&amp;nbsp; /。/100.0

使い方の詳細についても、サンプルプログラムを見れば大体分かると思います。
## タグの取得について
KyTeaで取得したタグですが、次のような構造体に格納しています。

    struct Tags{ string surface; vector\&lt; vector\&lt; pair\&lt;string, double\&gt; \&gt; \&gt; tags; };

これに対し、getAllTags()でタグを取得するとこうなります。

&gt; 今日 /名詞/3.2847062802112355 /言いよどみ/0.0 /代名詞/-0.12999710377780294 /きょう/1.3268831168939792 /こんにち/0.0

で、上記の出力に対するタグはjsonで書くとこんな感じになってます。

    { surface : 今日, tags : [[[名詞 , 3.2847062802112355], [言いよどみ , 0.0], [代名詞 , -0.12999710377780294] ], [[きょう , 1.3268831168939792], [こんにち , 0.0] ]]}

tagsの部分ですが、タグとスコアのペアの系列が二つあります。一つ目の系列が品詞で二つ目の系列が読みです。(v 0.3.1ではこの順番のようです)

これは、KyTeaのタグが特に形態素だとか読みだとか特定のラベルを取得しているのではないため、バージョンやモデルやconfigによっては別のラベルになり得るということが考えられます。

## まとめ
KyTeaのRuby,PythonラッパーMykyteaを作りました。結局は、KyTeaにラッパーコードを書いて、SWIGで共有ライブラリを作っただけです。

内部のコードはあまりスマートではありませんが、とりあえず出してしまいました。  
コメントなどありましたら、当ブログまたは[@chezou](http://twitter.com/chezou)までご連絡ください。

今後の予定としては、sinatraで簡単なWebアプリとの連携をさらっと書いてみたいです。  
**【2011/07/20追記】[sinatraで動くkytea\_sinatra書きました](http://chezou.wordpress.com/2011/07/18/sinatra%e3%81%a7kytea%e3%82%92%e3%83%96%e3%83%a9%e3%82%a6%e3%82%b6%e3%81%8b%e3%82%89%e8%a9%a6%e3%81%99kytea-sinatra%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ &quot;sinatraでKyTeaをブラウザから試すkytea-sinatra作ってみた&quot;)**

## 参考URL
[睡眠不足？：](http://d.hatena.ne.jp/sleepy_yoshi/20091123/p1)[SWIGでPythonラッパを書いてみる](http://d.hatena.ne.jp/sleepy_yoshi/20091123/p1)
