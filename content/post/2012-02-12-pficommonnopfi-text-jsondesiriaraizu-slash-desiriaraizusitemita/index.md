---
title: "pficommonのpfi::text::jsonでシリアライズ/ デシリアライズしてみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2012-02-12T12:02:30+00:00
lastmod: 2012-02-12T12:02:30+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
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

    def build(bld): bld.program( source = &#39;json-test.cpp&#39;, target = &#39;json-test&#39;, includes = &#39;. ../include&#39;, lib = &#39;pficommon\_text pficommon\_data&#39;, use = &#39;JSON TEST&#39; )

見れば分かると思いますが、sourceにソースとなるファイル、targetにビルドした後の実行ファイル名、includesにヘッダーファイルの場所を書きます。libにはライブラリ名を列挙します。このとき、複数の場合はスペースで区切ればOKです。

で、できたらこんな感じでビルドします。

    ./waf configure ./waf

### 2.基本的なアクセスの仕方
良くあるmapみたいなアクセスをしていって最後にjson\_castをします。

    cout \&lt;\&lt; json\_cast(js[&quot;user&quot;][&quot;id&quot;]) \&lt;\&lt; endl;

### 3.stringとjsonの相互変換
基本的にはstringstreamを経由します。

実際にはこんな感じでします。

    #include \&lt;pficommon/text/json.h\&gt; #include \&lt;sstream\&gt;using namespace pfi::text::json;using namespace std;namespace util{ json string\_to\_json(string str){ json js; stringstream ss(str); ss \&gt;\&gt; js; return js; } string json\_to\_string(json js){ stringstream oss; oss \&lt;\&lt; js; return oss.str(); } }

こんな感じで使います。

    json js = util::string\_to\_json(&quot;{\&quot;foo\&quot;:true, \&quot;bar\&quot;: \&quot;buzz\&quot;}&quot;); string str = util::json\_to\_string(js);

### 4.オブジェクトとのシリアライズ/デシリアライズ
ドキュメントにもありますが、自分で作ったクラスのjsonへのシリアライズをしたい場合は、シリアライズしたい変数をMEMBERマクロで登録しておきます。  
boostのような感じですね。

    class SouvenirDef {public: pfi::data::optional\&lt;std::string\&gt; name; pfi::data::optional\&lt;int\&gt; price; pfi::data::optional\&lt;bool\&gt; famous; pfi::data::optional\&lt;bool\&gt; funny; template \&lt;class Archive\&gt; void serialize(Archive &amp;ar){ ar &amp; MEMBER(price) &amp; MEMBER(famous) &amp; MEMBER(name) &amp; MEMBER(funny); } };

シリアライズしたいときは、to\_jsonを、デシリアライズをしたい時はvia\_json\_with\_defaultを使うと良いでしょう(json\_castでやると不足したkeyがあるとbad\_castになってしまうので)。

    stringstream ss(&quot;{\&quot;name\&quot;:null,\&quot;famouse\&quot;:true}&quot;); Souvenir sv2; ss \&gt;\&gt; via\_json\_with\_default(sv2); cout \&lt;\&lt; to\_json(sv2) \&lt;\&lt; endl;

いくつか注意点・ポイントです。この辺、知っておくと無駄にハマらないかと思います。

- 基本的な型はpfi::data::optionalを使う。使わないとnullをシリアライズできない。シリアライズしたい型はpfi::data::optional&lt;t&gt;を使う。&lt;del datetime=&quot;2014-11-22T22:03:25+09:00&quot;&gt;デシリアライズしたい場合は使わない。&lt;/del&gt;&lt;/t&gt;
- 配列を表したい時はvector, ハッシュを表したい時はmapを使う。
- pairとmap&lt;int int&gt;は使えない。&lt;/int&gt;
特に1点目ですが、サンプルコードのSouvenirクラスを見てください。

    class Souvenir { public: std::string name; int price; pfi::data::optional\&lt;int\&gt; max\_price; bool famous; bool funny; template \&lt;class Archive\&gt; void serialize(Archive &amp;ar){ ar &amp; MEMBER(price) &amp; MEMBER(famous) &amp; MEMBER(name) &amp; MEMBER(funny) &amp; MEMBER(max\_price); } };

このmax\_priceのようにpfi::data::optionalとすると、変数に値が入っていない場合にto\_jsonでシリアライズするとnullになってくれるのですが、以下のように直接クラスの値を参照しようとすると、値の有無が0/1で取得できる形になってしまいます。

[20120320追記]

optionalで宣言した型を取得する場合は、ポインタのように\*演算子でアクセスするようです。  
[boost::optional](http://www.kmonos.net/alang/boost/classes/optional.html)が参考になるそうです。@eiichiroi さんありがとうございます！

&gt; [@chezou](https://twitter.com/chezou) pficommonのoptionalの件(jsonと、メンバにoptionalを持つユーザ定義型の相互変換)についてですが、optionalも(デ)シリアライズできるようになっていました。optionalな変数へのアクセス方法を少し変えて貰えれば大丈夫だと思います
&gt; 
&gt; — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174539653511266305)

&lt;script async src=&quot;//platform.twitter.com/widgets.js&quot; charset=&quot;utf-8&quot;&gt;&lt;/script&gt;

&gt; [@chezou](https://twitter.com/chezou) ドキュメントに書かれていなくて申し訳ないのですが、optionalはポインタのようなものです。値を取り出すときには、\*(sv2.max\_price)のような感じで取り出す必要があります。ポインタと違う点はoptional間で値を共有しない(コピーする)ところです
&gt; 
&gt; — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174540358154321920)

&lt;script async src=&quot;//platform.twitter.com/widgets.js&quot; charset=&quot;utf-8&quot;&gt;&lt;/script&gt;  

    
    
    &gt; [@chezou](https://twitter.com/chezou) 正確な挙動についてはsrc/data/optional.hを、使い方の雰囲気についてはboost optionalでググるとなんとなく分かるかと思います。もし何かうまくいかない点や分からないところがあったら、また教えてください
    &gt; 
    &gt; — Eiichiro Iwata (@eiichiroi) [2012, 2月 28](https://twitter.com/eiichiroi/status/174541460249645057)
    
    &lt;script async src=&quot;//platform.twitter.com/widgets.js&quot; charset=&quot;utf-8&quot;&gt;&lt;/script&gt;
    
         stringstream ss(&quot;{\&quot;name\&quot;:null,\&quot;famous\&quot;:true,\&quot;max\_price\&quot;:1200}&quot;); Souvenir sv2; ss \&gt;\&gt; via\_json\_with\_default(sv2); //max\_priceは型をpfi::data::optional\&lt;int\&gt;にしているため、1/0の値で格納される//アクセスは\*(max\_price)でアクセス cout \&lt;\&lt; &quot;name:&quot; \&lt;\&lt; sv2.name \&lt;\&lt; &quot; price:&quot; \&lt;\&lt; sv2.price \&lt;\&lt; &quot; max\_price:&quot; \&lt;\&lt; \&lt;strong\&gt;\*(sv2.max\_price)\&lt;/strong\&gt; \&lt;\&lt; &quot; famous:&quot; \&lt;\&lt; (sv2.famous ? &quot;true&quot; : &quot;false&quot;) \&lt;\&lt; &quot; funny:&quot; \&lt;\&lt; (sv2.funny ? &quot;true&quot; : &quot;false&quot;) \&lt;\&lt; endl; //max\_priceをjsonにする場合は問題ない cout \&lt;\&lt; to\_json(sv2) \&lt;\&lt; endl;
    
    
    
    このため、 **jsonを入力としてデシリアライズしたい場合はpfi::data::optionalを利用しない変数を、シリアライズしてjsonに出力したい場合はpfi::data::optionalを利用した変数にしないといけません。**
    

**きちんと\*演算子でアクセスすることで、入出力対象な形で利用できます！**

それでは、pficommonで楽しいJSONライフを！


