---
authors: [aki]
categories: null
date: '2011-07-15 05:07:29-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2011-07-15 05:07:29-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた
keywords: [mykytea, '100.0', swig, kytea, python, 名詞, タグ, '0.0', ruby, ラッパー]
recommendations: [/post/2011-09-23-kyteawota-yan-yu-deshi-uratupa-plus-amatome/, /post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/,
  /post/2015-08-30-number-tqrk09-de-accept-lt-sitehazimeteno-gem-woraiburirisunishi-bai-simasita/]
---

**[2011/07/23追記]  
SWIGで生成したmykytea\_wrap.cxxをgithubに追加したので、SWIGのインストールは必要なくなりました。それに伴い実行すべき事が当初と変わっています。**

KyTeaという[@neubig](http://twitter.com/neubig)さんが作られた、テキストの形態素解析や読み付与ができるツールがあります。

[KyTea (京都テキスト解析ツールキット)](http://www.phontron.com/kytea/index-ja.html)  
処理のイメージですが、少し前のバージョンの物ですが[@nokuno](http://twitter.com/nokuno)さんの[紹介記事](http://d.hatena.ne.jp/nokuno/20100307/1267923299)がわかりやすいと思います。

これをRubyやPythonなどのLLで使えることができれば、Webアプリとかでも使えるようになって嬉しいのでは、と思いラッパーを書いてみました。  
Ubuntu 11.04, KyTea v0.3.1, SWIG 2.0.1  Ruby 1.8.7, 1.9.2, Python 2.7.1にて動作を確認しています。  
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

    swig2.0 -c++  -ruby -I/usr/local/include mykytea.i

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

> ruby mykytea\_test.rb

- Pythonの場合

    python mykytea\_test.py

でテストプログラムを実行してください。  
下記のような実行結果が得られるはずです。(注釈はでません)

> #分かち書きの結果を出力  
> 今日  
> は  
> い  
> い  
> 天気  
> で  
> す  
> 。
> 
> #タグ付き結果を文字列で出力  
> 今日/名詞/きょう は/助詞/は い/形容詞/い い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。
> 
> #表層及び1位のタグとスコアを出力  
> 今日    /名詞/3.2847062802112355        /きょう/1.3268831168939792  
> は    /助詞/3.924858405365926        /は/100.0  
> い    /形容詞/2.591390241156937        /い/100.0  
> い    /語尾/2.155161693042765        /い/100.0  
> 天気    /名詞/4.7486561215119565        /てんき/100.0  
> で    /助動詞/2.8068949386999753        /で/100.0  
> す    /語尾/2.7237397162868087        /す/100.0  
> 。    /補助記号/3.3392877514055774        /。/100.0
> 
> #表層と、全てのタグとそのスコアを出力  
> 今日    /名詞/3.2847062802112355    /言いよどみ/0.0    /代名詞/-0.12999710377780294        /きょう/1.3268831168939792    /こんにち/0.0  
> は    /助詞/3.924858405365926    /言いよどみ/-3.6483403104137224e-17    /代名詞/-0.23536067702781097        /は/100.0  
> い    /形容詞/2.591390241156937    /動詞/0.0    /言いよどみ/-0.00428323670492603        /い/100.0  
> い    /語尾/2.155161693042765    /言いよどみ/-3.946495907847236e-17    /web誤脱/-0.23382596743536913        /い/100.0  
> 天気    /名詞/4.7486561215119565    /言いよどみ/-9.215718466126788e-18    /web誤脱/-0.18273736539912366        /てんき/100.0  
> で    /助動詞/2.8068949386999753    /言いよどみ/-1.5937771935536915e-17    /動詞/-0.21163142806550297        /で/100.0  
> す    /語尾/2.7237397162868087    /言いよどみ/-1.4690939437178585e-17    /代名詞/-0.36184293534455636        /す/100.0  
> 。    /補助記号/3.3392877514055774    /言いよどみ/1.9136168344369153e-17    /代名詞/-0.268961070659961        /。/100.0

使い方の詳細についても、サンプルプログラムを見れば大体分かると思います。
## タグの取得について
KyTeaで取得したタグですが、次のような構造体に格納しています。

    struct Tags{ string surface; vector\< vector\< pair\<string, double\> \> \> tags; };

これに対し、getAllTags()でタグを取得するとこうなります。

> 今日 /名詞/3.2847062802112355 /言いよどみ/0.0 /代名詞/-0.12999710377780294 /きょう/1.3268831168939792 /こんにち/0.0

で、上記の出力に対するタグはjsonで書くとこんな感じになってます。

    { surface : 今日, tags : [[[名詞 , 3.2847062802112355], [言いよどみ , 0.0], [代名詞 , -0.12999710377780294] ], [[きょう , 1.3268831168939792], [こんにち , 0.0] ]]}

tagsの部分ですが、タグとスコアのペアの系列が二つあります。一つ目の系列が品詞で二つ目の系列が読みです。(v 0.3.1ではこの順番のようです)

これは、KyTeaのタグが特に形態素だとか読みだとか特定のラベルを取得しているのではないため、バージョンやモデルやconfigによっては別のラベルになり得るということが考えられます。

## まとめ
KyTeaのRuby,PythonラッパーMykyteaを作りました。結局は、KyTeaにラッパーコードを書いて、SWIGで共有ライブラリを作っただけです。

内部のコードはあまりスマートではありませんが、とりあえず出してしまいました。  
コメントなどありましたら、当ブログまたは[@chezou](http://twitter.com/chezou)までご連絡ください。

今後の予定としては、sinatraで簡単なWebアプリとの連携をさらっと書いてみたいです。  
**【2011/07/20追記】[sinatraで動くkytea\_sinatra書きました](https://chezo.uno/post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/)**

## 参考URL
[睡眠不足？：](http://d.hatena.ne.jp/sleepy_yoshi/20091123/p1)[SWIGでPythonラッパを書いてみる](http://d.hatena.ne.jp/sleepy_yoshi/20091123/p1)