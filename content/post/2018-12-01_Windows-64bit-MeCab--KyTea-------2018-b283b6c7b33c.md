---
title: Windows 64bitでMeCab(とKyTea)を使う方法 2018
description: CIでWindowsバイナリとwheelを作った話
date: '2018-12-01T13:05:57.092Z'
categories: []
keywords: [Windows, MeCab, NLP, KyTea]
authors: [aki]
---

こんにちは、日本語のテキスト処理してますか。

最近はBERTやらTFhubで使えるのEmbeddingのモデルが一段と増えてきて、楽しいですね。BERTで用いられるWordPieceや、MeCabの作者としても有名な工藤さんの新作、[SentencePiece](https://qiita.com/taku910/items/7e52f1e58d0ea6e7859c)といった新しいTokenizerが出てくる一方で、TFhubで用意されているNNLMのtokenizerは公開されていないので結局MeCabで頑張らないといけない(少なくとも当初[Tokenizerなんて要らないよという返事をされた](https://groups.google.com/a/tensorflow.org/d/msg/hub/TG8XVsCVp9A/K1Yc0esiCAAJ))など、2018年の今でもMeCabの重要性は変わらず続いています。

そこで、今回はWindowsでも形態素解析をしたいという人にどうしたらいいんだっけという話の2018年12月版をしたいと思います。

### tl;dr

*   64bit版のMeCabインストーラーが欲しい場合はikegami-yukinoさんの[こちらの非公式インストーラ](https://github.com/ikegami-yukino/mecab/releases)が便利でしょう。Pythonは[mecab-python-windows](https://pypi.python.org/pypi/mecab-python-windows)もPypiに用意していただいています
*   最新のWindows用のMeCabのexeとdll、ipadicがzipでほしいという人は、私が[CIでビルドしている物](https://github.com/chezou/mecab/releases)を使ってください。Python用wheelもありますし、Rubyの人にも[libmecab.dllがあるとnatto経由で使えて便利](https://gist.github.com/chezou/2ab09df15ddb8e94006b8168fed76323)です
*   KyTeaも合わせて[Windows用のバイナリ](https://github.com/chezou/kytea/releases)と[Python用wheel](https://pypi.org/project/kytea/)を用意しました

### なぜこの記事を書くに至ったか

今年に入って、MeCab/SentencePieceの作者の工藤さんによる形態素解析本も出てきて、ますます皆さんの日本語処理熱は高まっているかと思います。

[**実践・自然言語処理シリーズ2 形態素解析の理論と実装**  
_Amazonで工藤 拓の{ProductTitle}。アマゾンならポイント還元本が多数。一度購入いただいた電子書籍は、KindleおよびFire端末、スマートフォンやタブレットなど、様々な端末でもお楽しみいただけます。_amzn.to](https://amzn.to/2Q9O6qt "https://amzn.to/2Q9O6qt")[](https://amzn.to/2Q9O6qt)

PythonでのモダンなNLPの処理向けのライブラリspaCyでは、他の言語との兼ね合いでPure Python実装のJanomeからUnidicベースのMeCabに[移行されました](https://github.com/explosion/spaCy/pull/1246)。需要は高まっています。

![[https://spacy.io/usage/models](https://spacy.io/usage/models) Spacy depends on MeCab (mecab-python3)](/img/1__nOVgkKYYMbIKaJFKSUEh6Q.png)
[https://spacy.io/usage/models](https://spacy.io/usage/models) Spacy depends on MeCab (mecab-python3)

また、日本語の機械学習の本が新たに出ていますが、大抵の場合Pythonでmecab-python3を使いましょうとありますが、[現状まだwheelの提供もない](https://github.com/SamuraiT/mecab-python3/issues/16)ためSWIGも用意しsourceからのビルドが前提です。Windowsの人にそれを要求するのはハードルが高いです。

### 64bit WindowsでMeCabを使うには

メモリ16GBは人権という言葉もありますが、この前提には4GB以上のマシンでは64bit OSを使っているということが前提だと思います。とはいえ、MeCabの[公式サイト](http://taku910.github.io/mecab/)には32bit版のバイナリしか存在しておらず、自前のビルド環境を用意していないことが多いWindowsの皆様におかれましては面倒くさい状況になっていると言えます。まさか、[8年前の自分の記事](https://chezou.hatenablog.com/entry/20101013/1416661193)が役に立つときが来るとは…。

しかし、３年前のMinGW用の修正が今年になってマージされたときにMSVCでのビルドが壊れてしまいました。一応PRを投げましたが、いつマージされるかはわからない状況です。

[**Make buildable MSVC 64bit by chezou · Pull Request #46 · taku910/mecab**  
_After #13 merging, the MSVC build has been broken since WPATH\_FORCE is not defined for MSVC…_github.com](https://github.com/taku910/mecab/pull/46 "https://github.com/taku910/mecab/pull/46")[](https://github.com/taku910/mecab/pull/46)

また、ikegami-yukinoさんという方が64bit版exeを配布されていますが（windows用wheelも）、CIでexe実行してインストーラ回すのどうすればいいんだっけということで、zipで固められたものがほしいなぁと思いました。

[**Windows で pip で mecab-python をいれる - Qiita**  
_はじめに ちゃお・・・† 個人的にですが、最近はWindowsでMeCabを使う機会が増えてきました。しかし、Windowsでmecab-pythonを入れるには、ソースをダウンロードしたりsetup.pyを書き換えたりコンパイ..._qiita.com](https://qiita.com/yukinoi/items/990b6933d9f21ba0fb43 "https://qiita.com/yukinoi/items/990b6933d9f21ba0fb43")[](https://qiita.com/yukinoi/items/990b6933d9f21ba0fb43)

韓国の先立ちはCIでWindows向け[MeCab](https://github.com/Pusnow/mecab-ko-msvc/)、 辞書（ipadic）、 Python用のwheelをbuildしているのを見つけました。

これはいい。ということで、車輪の再発明をしました。

### Yet another MeCab binaries for Windows x64 & x32

GitHubのreleaseにて最新のMeCabをベースにした[Windowsの64bit & 32bitバイナリを公開](https://github.com/chezou/mecab/releases)しています。

やったことは、[appveyor.yml](https://github.com/chezou/mecab/blob/master/appveyor.yml) と[build.bat](https://github.com/chezou/mecab/blob/master/ci/win/build.bat)にだいたい詰まっていますが、先程送ったPRをベースにMSVC用のMakefileを改めて作り、それらをCIでビルドしています。また、各Pythonバージョンごとのwheelも作っています。

libmecab.dllを使えばRubyなど別の言語のMeCabバインディングからも利用することができます。[libmecab.dllがあるとnatto経由で使えて便利](https://gist.github.com/chezou/2ab09df15ddb8e94006b8168fed76323)というのを手元で確認しています。

なお、Unidicは同梱しようと思えばできると思うのですが、皆大好きnelodogdはshell scriptやawk、perlの塊でビルドする必要があり、WSL使ってUbuntu用意するのが最短のようです（敗北感しかない）。

### Python拡張モジュールのbuildの話

そもそも、Pythonのパッケージでは予めビルドされたwheelという仕組みがあります。これのおかげで、ユーザは自分の環境でビルドすることなくさくっと `pip install awesome-package` するだけでC拡張があるパッケージが入れられるわけです。Rubyでいうところの `gem install nokogiri` で苦しまなくても良いような仕組みがあるということです。

#### WindowsのPython拡張周りの辛さ

Windows用のPython拡張モジュールを用意するためには、PythonのバージョンにマッチしたVisual Studioのバージョン（あるいはビルドツール）を用意しないといけません。詳しくはPythonコミッター稲田さんの以下の記事をご参照ください。

[**Windows での Python 2.7, 3.4, 3.5 の拡張モジュールビルド環境 - Qiita**  
_Windows 用に Python のバイナリパッケージを作成するときに知っておいたほうがいい基礎知識や便利情報をまとめて書いていきます。 Windows 上で Python を使っているユーザーは、 Python…_qiita.com](https://qiita.com/methane/items/2210712763b91e75fdf0 "https://qiita.com/methane/items/2210712763b91e75fdf0")[](https://qiita.com/methane/items/2210712763b91e75fdf0)

考えようによっては、MSVCの環境を用意すればWindowsのバージョンに依存しないバイナリパッケージが用意できるので、非常に楽です。少なくともmacOSはもっと楽なのですが、なぜ楽と言えるのかについてもお話しようと思います。

#### 余談: Linux用wheelを用意する

Linuxにおいては、様々なディストリビューションの違いがある中で、各種環境で共通のwheelを用意するのは難しい問題でした。しかし、Windows/macOSでwheelが使われるようになり、その恩恵をLinuxでもあずかれるようにということでmanylinuxという枠組みができました。最初にできたのはmanylinux1というもので、互換性を考慮してCentOS 5のDocker imageをベースとしてwheelをビルドします。[PEP 513](https://www.python.org/dev/peps/pep-0513/)に詳細は記述されています。

作り方等々は稲田さんの記事と、PyPAの[python-manylinux-demo](https://github.com/pypa/python-manylinux-demo)リポジトリが参考になるでしょう。

[**manylinux1 wheel を作ってみる - methaneのブログ**  
_先日の記事 で紹介した、 manylinux1 wheel を作ってみます。 ビルド環境を Docker image として公開してくれています。 docker pull quay.io/pypa/manylinux1\_x86\_64…_methane.hatenablog.jp](https://methane.hatenablog.jp/entry/trying-manylinux1 "https://methane.hatenablog.jp/entry/trying-manylinux1")[](https://methane.hatenablog.jp/entry/trying-manylinux1)

お気づきの方もいらっしゃるかもしれませんが、CentOS 5ベースのgccで新しいプロダクトのbindingを用意するのは地獄です。現に（非常に議論が沸き起こっているところですが）TensorFlowはmanylinux1というタグを使っているにもかかわらずもっと新しい環境で用意したwheelを用意しています。

これに対してCent OS 5もEOLになることなどを踏まえて、manylinux 2010が準備されています。以下のissueを見る限りでは、次のpipからmanylinux2010を扱えるようになり、そろそろ準備が整ってきているようです。

[**Tracking issue for manylinux2010 rollout · Issue #179 · pypa/manylinux**  
_I've accepted the manylinux2010 PEP, so that's now an active interoperability standard…_github.com](https://github.com/pypa/manylinux/issues/179 "https://github.com/pypa/manylinux/issues/179")[](https://github.com/pypa/manylinux/issues/179)

### KyTeaのWindowsバイナリとPythonバインディング

MeCabで得た知見を生かして、ついでにKyTeaもWindows用バイナリとPythonバインディングをpip installできるようにしました。本家にもPRを送ったんですが、appveyorの設定がまだされていないので、fork版をお使いください。

[**chezou/kytea**  
_The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc. - chezou/kytea_github.com](https://github.com/chezou/kytea/releases "https://github.com/chezou/kytea/releases")[](https://github.com/chezou/kytea/releases)

なお、 `pip install kytea` で[Windowsも入る](https://pypi.org/project/kytea/#files)ようになっています。（WindowsのPython 2.7は除く）issueがあればこちらにどうぞ。

[**chezou/Mykytea-python**  
_Python wrapper for KyTea. Contribute to chezou/Mykytea-python development by creating an account on GitHub._github.com](https://github.com/chezou/Mykytea-python "https://github.com/chezou/Mykytea-python")[](https://github.com/chezou/Mykytea-python)