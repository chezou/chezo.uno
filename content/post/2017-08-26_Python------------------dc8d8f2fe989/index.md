---
title: Pythonの環境構築を自分なりに整理してみる
description: 先日、 kawasaki.rb の懇親会で「AWS LambdaのためにPythonはじめたいんです」とか「機械学習系の本を読み始めたので、そこに書いてあったcondaではじめました」とかいう話を聞きました。
date: '2017-08-26T13:58:07+09:00'
categories: [python]
keywords: [python, conda, パッケージ, venv, anaconda, 環境, virtualenv, ruby, os, windows]
authors: [aki]
recommendations: [/post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka/,
  /post/2018-12-01_Windows-64bit-MeCab--KyTea-------2018-b283b6c7b33c/, /post/2015-06-06-pip-install-kyteadekiruyouninarimasita/]
---


先日、 kawasaki.rb の懇親会で「AWS LambdaのためにPythonはじめたいんです」とか「機械学習系の本を読み始めたので、そこに書いてあったcondaではじめました」とかいう話を聞きました。

コレ読んでおけ系の記事は既に色々とあるんですが、今回は自分で触ってきて使っている環境を中心に説明をしようと思います。想定読者としては、Rubyを使っていたけど最近Pythonにも手を出すようになってきたという人です。

書き始めてから思ったんですが、ぶっちゃけPythonコミッターのmethaneさんの以下の記事を読めば十分な気もしてきましたが、一例としてお読みいただければと思います。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://qiita.com/methane/items/5afdabd513a18049c34f" data-iframely-url="//cdn.iframe.ly/7whUOpn?card=small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

### 私の立ち位置

もともとは、数年前まで 年に一回Python3でNLTKやらscikit-learnやら機械学習や自然言語処理の環境を作ろうと試みては失敗してPython使うものかと思っていた人でした。それが、Anacondaで環境導入すると、面倒なことは何も考えずに済むということを知り、CookpadではAnacondaを前提に環境構築を勧めていました。

今は、ymotongpooに「郷に入っては郷に従え」と言われたため、pip+virtualenv/venvで全てをこなしていますが、これで困ったことは特にありません。macOS, Windows, Linuxそれぞれでやっていますが、大きな苦労もなく大丈夫だなという印象です。

先に言っておくと自分のPython力はそこまで高くないです。もともとはRailsで開発はしていましたが、Pythonはほぼ機械学習やデータマイニング系のコードを一人で書くということが多いです。いくつかPythonのライブラリは書いて入るのですが、チーム開発の経験はないためその観点は弱いということを認識いただければと思います。

なお、仕事では[Anacondaも使っている](http://blog.cloudera.com/blog/2017/05/create-conda-recipe-to-use-c-extended-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/)ので、適材適所だなと思ってこの話を書いています。単純にpyenvやcondaを使うな、というつもりはありません。リスクとベネフィットのトレードオフで選んでください。

### 環境構築のあれやこれや

以下では、macOS, Windows, Linuxで自分がどのように環境構築をしているかについて書いていこうと思います。

#### 最低限の前提知識

Pythonの実行環境の導入・パッケージ管理周りに出て来るキーワードについて簡単に説明します。

*   **pip**: パッケージインストールのためのツール。Rubyでいうところのgem。パッケージはPyPIというRubyで言うところのrubygems.orgから取ってくる。
*   **virtualenv**: パッケージを切り分ける仮想環境を作る人。Rubyで言うところのbundlerに近いが、Pythonの利用するバージョンも指定するのでrbenvのruby-build抜きの機能を持っている感じ
*   **venv**: Python 3から公式として入ったvirtualenv。ただし、venvはPythonのバージョン指定ができないとか、Debian/Ubuntuでは余計な依存関係が発生するとかで私は使ってません。

\[2017/08/30 追記\]  
venvはバージョンの指定が出来ないのではなく、2.7と3.6との切り替えができないという意味でした。 `python3.5 -m venv some-great-env`で切り分けられます。  
私自身パッケージ開発に2.7サポートをする場合があるのと、Ubuntu使いなのでvirtualenvを使っています。  
\[/追記\]

以上が、多くのPythonistaに使われている基本的なツールセットです。このあたりの話は、PyPAと呼ばれるパッケージ管理関係の標準と参照実装を決める目的で設立された団体によって[推奨ツール](https://packaging.python.org/guides/tool-recommendations/)として扱われています。（後述のcondaもでてきますが）

*   **conda**: Continuumという会社が作っているPythonを中心とした科学計算のパッケージ管理をするためのプラットフォーム
*   **pyenv**: rbenvのPython版。Pythonのソースからのビルドと、Pythonの実行環境（バージョンなど）の切り替えをする

これらは、特定の目的のために使うことが多いものです。

#### 実行環境の導入

2017年においては、Python 3系の最新版を入れておけばだいたい生きていけると思います。が、何かしらの辛い事情で2系も使わないといけない場合もあるかと思います。

その場合は、自分はOSのパッケージ管理ツールでPythonを入れています。例えばUbuntuで `apt install python-dev` とするとPython 2.7が `apt install python3-dev` をすると今ならPython 3.6が入ります。同時に入れると

```
/usr/bin/python    #<- 2.7  
         python2   #<- 2.7  
         python2.7 #<- 2.7  
         python3   #<- 3.6  
         python3.6 #<- 3.6
```

という感じで入ります。 `brew install`でも `python` と `python3` で2系と3系両方入れることができます。

バージョンの切り替えは、後述のvirtualenvで実行するバージョンを切り替えます。逆に言うとpyenvでのバージョン切り替えは、ライブラリ開発者のように細かいバージョン切り替えが必要な人でなければ不要でしょう。

なお、homebrewは彼らの方針で過去バージョンのPythonはpyenvを使ってくれ、と言っています。MacPortsは普通に過去バージョンが入りますし、Ubuntuは[deadsnake](http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu/)を使えばこの問題は解決される話です。homebrewで切り替えたい人はpyenvを使うほうが楽でしょう。

WindowsだとChocolateyで入れるか、オフィシャルのインストーラで入れれば良いです。（ Python 3.6からは `py` というコマンドが用意されており、それを使うとバージョンを切り替えた実行もできます）

なお、絶対にやってはいけないのはSystem Pythonを使い続けることです。System Pythonは往々にして古いことが多く、またyumなどシステム上重要なシステムに依存しています。うっかり、 `sudo pip install` などしようものなら、環境を壊してしまう恐れがあります。

なお、環境構築に関する話は、以下の記事が参考になるでしょう。

[**Pythonの環境設定でむかついてる人はとりあえずこれをコピペで実行してください 2017.01 - YAMAGUCHI::weblog**](http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124)

#### パッケージ管理

まず、大前提として先程も書きましたが `sudo pip install hogehoge` をするのは辞めましょう。システムPythonはOSで使っているため、これの環境を壊すことは危険です。

プロジェクトごとにパッケージのバージョンを依存関係を切り替えるのには `virtualenv`を使います。以下の aodagさんの資料を読んで下さると良いと思います。

[https://gist.github.com/aodag/bea141d255e22d204a2140fba658ebf2](https://gist.github.com/aodag/bea141d255e22d204a2140fba658ebf2)

また、Python 3に関しては以下の `venv`のチュートリアルがわかりやすくまとまっています。Debian/Ubuntu以外の人はPython 3だけで良ければ `venv` で十分かと思います。

[https://docs.python.jp/3/tutorial/venv.html](https://docs.python.jp/3/tutorial/venv.html)

ここに書いてあるけど大事な話としては、 `virtualenv`でPythonの実行環境を切り替えられる話をしておきます。

まずは、以下のようにしてユーザ領域に `virtualenv`を入れます。

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ export PATH="~/.local/bin/:$PATH"  
$ python get-pip.py --user  
$ pip install virtualenv --user  
```

```
# Windowsの場合は特に考えずにpip installで良い  
> pip install virtualenv
```


virtualenvでは、プロジェクトの下に仮想環境を作ります。プロジェクトルートで以下のコマンドを実行すると

```
$ virtualenv venv -p python3.6
```

Python 3.6を実行環境とした、仮想環境ができます。

```
$ echo venv >> .gitignore
```

で、 `.gitignore` に追加しておくとよいでしょう。

次に、 `activate` して仮想環境を有効化します。

```
$ source venv/bin/activate(venv) $
```

```
#Windows
> . venv/Script/activate
```

この状態で、 `pip install scikit-learn` とすると `venv` 以下にパッケージが入ります。仮想環境の利用を止めたい場合は `deactivate` コマンドを使いましょう。

pip 7.1以降ではconstraints.txtというGemfile.lockのようなものが扱えるようになりました。 `pip freeze` で現在インストールしているライブラリとバージョン一覧がでます。

```
(venv)$  pip freeze -l  
pylint==1.7.2  
pyparsing==2.2.0  
pytest==3.2.1  
requests==2.18.4  
six==1.10.0  
tox==2.7.0  
urllib3==1.22  
virtualenv==15.1.0

(venv)$ pip freeze -l> constraints.txt  
(venv)$ cat constraints.txt  
pylint==1.7.2  
pyparsing==2.2.0  
pytest==3.2.1  
requests==2.18.4  
six==1.10.0  
tox==2.7.0  
urllib3==1.22  
virtualenv==15.1.0
```

ここに、プロジェクトに必要な必要なライブラリをrequirements.txtに記述します。

```
(venv)$ cat requirements.txt  
requests  
pyparsing
```

そうすると、以下のコマンドで必要なライブラリの必要なバージョンを入れることができます。

```
(venv)$ pip install -r requirements.txt -c constraints.txt
```

#### condaの話

Anacondaは機械学習などの科学計算向けのPythonディストリビューションです。Anacondaは、推奨パッケージを含めて入れるAnacondaと、自分で必要なパッケージを入れるMinicondaが入ります。Anacondaは（今はないですが）昔はDjangoを入れているなど重いパッケージも入ってくることがあるので、きちんとデフォルトパッケージを調べてから使いましょう。

なお、Pythonディストリビューションと書いてありますが、Rなど他の言語の環境を作ることもできます。

Anacondaはvirtualenvと違い、独自の仮想環境を作ることができます。特徴的なのは、 `--copy` というオプションを付けるとライブラリや.soなどをシンボリックリンクを作らず、コピーするということができるため、仮想環境一式をzipやtarで固めると、そのまま実行可能な形で使いまわせることです。

```
$ conda create -n myenv --copy python**\=**3.6  
$ conda activate myenv
```

つまり、通常 `apt` などのOSのパッケージ管理で入れるようなところも、condaのパッケージで管理をします。condaはPyPIとは異なる独自のパッケージリポジトリを持ち、そちらにOSごとにバイナリをアップロードします。ですので、OpenCVなど同じ名前の同じものを入れるためのパッケージが複数のユーザによってレポジトリに登録されていたりと結構雑多な印象があります。

多くの機械学習の本では、condaを使えと書いて有ることが多いのですが、Windows以外ではあまり使わないほうが良いと私は考えています。

理由としては、以下が上げられます。

*   2017年においては、 wheel というバイナリパッケージのフォーマットがデファクトになっているので、condaの当初の目的の科学計算用のパッケージ（gfortanとかに依存していて辛い）を簡単に入れるという目的はcondaでなくてもできる。
*   普通に入れると、macOS/Linuxの[Systemに入っているopenssl/curl/pythonなどのコマンドを置き換えてしまう](http://qiita.com/t2y/items/dd6d7f9c70ac2b8a79da#anaconda-%E3%81%8C%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E9%A0%98%E5%9F%9F%E3%81%AE%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E9%9A%A0%E3%81%99%E3%81%AE%E3%81%AF%E6%82%AA%E3%81%84%E3%81%93%E3%81%A8%E3%81%AA%E3%81%AE%E3%81%8B)(厳密には、 condaの方が先にPATHが通ってしまう) \[[issue](https://github.com/ContinuumIO/anaconda-issues/issues/1119)\]
*   パッケージ開発者は、condaユーザーではないことが多く、彼らからするとJRubyやRubyinius（あるいはWindows固有の不具合）など通常使わない環境でのサポートを求められるように感じる。
*   condaの世界で閉じていないNative extensionのビルド（Cython依存など）でincludeしないといけない情報などがうまく渡せず、はまると辛い
*   Distributionごとの違いが発生する場合もあるのに、OSレベルの違いしか考慮できない

ですので、Windowsの人や、開発は通常しないけど機械学習を体験してみたいという人はcondaを使うと良いでしょう。あるいは、pyenvの管理下でMinicondaを入れるか、私自身はDockerの中でcondaを使っています。

ただ、ScipyなどWindows用の一部は `pip install`では入らないので[自前で](http://www.lfd.uci.edu/~gohlke/pythonlibs/)wheelをダウンロードする必要があります。この点は正直condaの方が良いかと思います。

歴史的な詳細は下記が詳しいです。端的に言うと、wheel以前の古いバイナリフォーマットがいまいちだったため、condaを作ったという形になります。

[**wheelのありがたさとAnacondaへの要望 - YAMAGUCHI::weblog**](http://ymotongpoo.hatenablog.com/entry/2017/02/02/182647)

#### カルチャーの違い

RubyとPythonでは色々と文化が違うのですが、一番大きな違いは個人的には以下の2点だと思っています。

*   できるだけ依存するものは最低限の薄いものが良い。ブラックボックスは好まないという思想
*   Rubyはいいものを皆が試して事実上のデファクトスタンダードになるのに対して、提案されたPEPという「標準」を合議して決めていくというスタイル

なので、Rubyはパッとデファクトが決まる印象がありますが、Pythonはじっくり議論の上で標準を決めていくという印象があります。（コレもあって、過渡期の実装が色々出てくる）

また、こうした経緯からかPythonの人たちはきっちり例外まで補足したがる傾向にあると思います（例えるなら、Pythonは数学科の数式にきっちり向き合う感じと、Rubyは工学部の数式に対する雑な扱いのような感じ）。なので、昔からのPythonistaが書くドキュメントは長くなる傾向にあると思いますが、そういうものだと思って割り切るしかないと思います。

### まとめ

個人的には、普通に使う分にはvirtualenv/venvとOSのパッケージ管理ツールでPythonを入れるというので、私は良いと思って使っています。

ただ、プロダクション要求などで必要なものもあると思うので、condaとpyenvは適材適所で用法用量を守って使いましょう。

### 参考文献

[**Pythonの環境設定でむかついてる人はとりあえずこれをコピペで実行してください 2017.01 - YAMAGUCHI::weblog**](http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124)

[**Rubyist が pyenv を使うときに知っておいてほしいこと - Qiita**](http://qiita.com/methane/items/5afdabd513a18049c34f)

[**pyenvが必要かどうかフローチャート - Qiita**](http://qiita.com/shibukawa/items/0daab479a2fd2cb8a0e7)

[**Anaconda は Environment Isolation Tool (環境分離ツール) ではない - Qiita**](http://qiita.com/t2y/items/dd6d7f9c70ac2b8a79da)

[**wheelのありがたさとAnacondaへの要望 - YAMAGUCHI::weblog**](http://ymotongpoo.hatenablog.com/entry/2017/02/02/182647)
