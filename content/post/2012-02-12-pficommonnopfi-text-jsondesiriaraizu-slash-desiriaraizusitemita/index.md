---
title: pficommonのpfi::text::jsonでシリアライズ/ デシリアライズしてみた
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2012-02-12 12:02:30+00:00
lastmod: 2012-02-12 12:02:30+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [json, optional, price, pfi, data, max, string, js, ss, name]
recommendations: [/post/2017-12-31_2017--------c4901627b12d/, /post/2014-05-06-julia-vs-python-bitutokoinopusiyonnomontekarurosimiyuresiyon/,
  /post/2019-12-04-r-and-td/]
---
[@unnonounoさんが紹介してくださったpficommon](http://unnonouno.blogspot.com/2011/10/pficommon.html)のjsonライブラリを試してみました。  
pficommonのjsonライブラリはboostみたいにjsonと自分で作ったクラスのオブジェクトとのシリアライズ/デシリアライズができるのがとても魅力です。  
その一方で、結構[ドキュメント](http://pfi.github.com/pficommon/text/json.html)には書いてないことが色々あったので、メモしておきます。

いつものようにコードはgithubにあります。

[https://github.com/chezou/pficommon\_json\_test](https://github.com/chezou/pficommon_json_test)

今回のポイントは以下の通りです。

1. wafの使い方
2. 基本的なアクセスの仕方
3. stringとjsonの相互変換
4. オブジェクトとのシリアライズ/デシリアライズ

### 1.wafの使い方
wafはmakeの代わりのビルドシステムで、pythonでビルドします。詳細な使い方は[こちら](http://d.hatena.ne.jp/tanakh/20100212#p1)を参考にしてください。  
基本的には、wscriptと呼ばれるMakefileのような物をソースコードがあるディレクトリにそれぞれ書きます。  
この際、各ディレクトリに置かれたwscriptが再帰的に呼ばれるので、モジュール毎にディレクトリを切り分けている場合は、そのモジュールの必要なライブラリなどを書いておくべきです。

例としてsrcディレクトリにあるwscriptをのせます。

    def build(bld): bld.program( source = 'json-test.cpp', target = 'json-test', includes = '. ../include', lib = 'pficommon\_text pficommon\_data', use = 'JSON TEST' )

見れば分かると思いますが、sourceにソースとなるファイル、targetにビルドした後の実行ファイル名、includesにヘッダーファイルの場所を書きます。libにはライブラリ名を列挙します。このとき、複数の場合はスペースで区切ればOKです。

で、できたらこんな感じでビルドします。

    ./waf configure ./waf

### 2.基本的なアクセスの仕方
良くあるmapみたいなアクセスをしていって最後にjson\_castをします。

    cout \<\< json\_cast(js["user"]["id"]) \<\< endl;

### 3.stringとjsonの相互変換
基本的にはstringstreamを経由します。

実際にはこんな感じでします。

    #include \<pficommon/text/json.h\> #include \<sstream\>using namespace pfi::text::json;using namespace std;namespace util{ json string\_to\_json(string str){ json js; stringstream ss(str); ss \>\> js; return js; } string json\_to\_string(json js){ stringstream oss; oss \<\< js; return oss.str(); } }

こんな感じで使います。

    json js = util::string\_to\_json("{\"foo\":true, \"bar\": \"buzz\"}"); string str = util::json\_to\_string(js);

### 4.オブジェクトとのシリアライズ/デシリアライズ
ドキュメントにもありますが、自分で作ったクラスのjsonへのシリアライズをしたい場合は、シリアライズしたい変数をMEMBERマクロで登録しておきます。  
boostのような感じですね。

    class SouvenirDef {public: pfi::data::optional\<std::string\> name; pfi::data::optional\<int\> price; pfi::data::optional\<bool\> famous; pfi::data::optional\<bool\> funny; template \<class Archive\> void serialize(Archive &ar){ ar & MEMBER(price) & MEMBER(famous) & MEMBER(name) & MEMBER(funny); } };

シリアライズしたいときは、to\_jsonを、デシリアライズをしたい時はvia\_json\_with\_defaultを使うと良いでしょう(json\_castでやると不足したkeyがあるとbad\_castになってしまうので)。

    stringstream ss("{\"name\":null,\"famouse\":true}"); Souvenir sv2; ss \>\> via\_json\_with\_default(sv2); cout \<\< to\_json(sv2) \<\< endl;

いくつか注意点・ポイントです。この辺、知っておくと無駄にハマらないかと思います。

- 基本的な型はpfi::data::optionalを使う。使わないとnullをシリアライズできない。シリアライズしたい型はpfi::data::optional<t>を使う。<del datetime="2014-11-22T22:03:25+09:00">デシリアライズしたい場合は使わない。</del></t>
- 配列を表したい時はvector, ハッシュを表したい時はmapを使う。
- pairとmap<int int>は使えない。</int>
特に1点目ですが、サンプルコードのSouvenirクラスを見てください。

    class Souvenir { public: std::string name; int price; pfi::data::optional\<int\> max\_price; bool famous; bool funny; template \<class Archive\> void serialize(Archive &ar){ ar & MEMBER(price) & MEMBER(famous) & MEMBER(name) & MEMBER(funny) & MEMBER(max\_price); } };

このmax\_priceのようにpfi::data::optionalとすると、変数に値が入っていない場合にto\_jsonでシリアライズするとnullになってくれるのですが、以下のように直接クラスの値を参照しようとすると、値の有無が0/1で取得できる形になってしまいます。

[20120320追記]

optionalで宣言した型を取得する場合は、ポインタのように\*演算子でアクセスするようです。  
[boost::optional](http://www.kmonos.net/alang/boost/classes/optional.html)が参考になるそうです。@eiichiroi さんありがとうございます！

> [@chezou](https://twitter.com/chezou) pficommonのoptionalの件(jsonと、メンバにoptionalを持つユーザ定義型の相互変換)についてですが、optionalも(デ)シリアライズできるようになっていました。optionalな変数へのアクセス方法を少し変えて貰えれば大丈夫だと思います
> 
> — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174539653511266305)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

> [@chezou](https://twitter.com/chezou) ドキュメントに書かれていなくて申し訳ないのですが、optionalはポインタのようなものです。値を取り出すときには、\*(sv2.max\_price)のような感じで取り出す必要があります。ポインタと違う点はoptional間で値を共有しない(コピーする)ところです
> 
> — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174540358154321920)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>  

    
    
    > [@chezou](https://twitter.com/chezou) 正確な挙動についてはsrc/data/optional.hを、使い方の雰囲気についてはboost optionalでググるとなんとなく分かるかと思います。もし何かうまくいかない点や分からないところがあったら、また教えてください
    > 
    > — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174541460249645057)
    
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
    
         stringstream ss("{\"name\":null,\"famous\":true,\"max\_price\":1200}"); Souvenir sv2; ss \>\> via\_json\_with\_default(sv2); //max\_priceは型をpfi::data::optional\<int\>にしているため、1/0の値で格納される//アクセスは\*(max\_price)でアクセス cout \<\< "name:" \<\< sv2.name \<\< " price:" \<\< sv2.price \<\< " max\_price:" \<\< \<strong\>\*(sv2.max\_price)\</strong\> \<\< " famous:" \<\< (sv2.famous ? "true" : "false") \<\< " funny:" \<\< (sv2.funny ? "true" : "false") \<\< endl; //max\_priceをjsonにする場合は問題ない cout \<\< to\_json(sv2) \<\< endl;
    
    
    
    このため、 **jsonを入力としてデシリアライズしたい場合はpfi::data::optionalを利用しない変数を、シリアライズしてjsonに出力したい場合はpfi::data::optionalを利用した変数にしないといけません。**
    

**きちんと\*演算子でアクセスすることで、入出力対象な形で利用できます！**

それでは、pficommonで楽しいJSONライフを！


