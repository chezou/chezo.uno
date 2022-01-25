---
title: Thinkpad X1 Carbon (2017)をWindows 10/Ubuntu 17.04デュアルブートにした
description: 前回 Thinkpad X1 Carbon(2017)のWindows周りの設定について書きましたが、今回はUbuntu 17.04とのデュアルブートについて書きます。
date: '2017-07-10T00:11:00+09:00'
categories: []
authors: [aki]
keywords: [ubuntu, sudo, install, apt, 設定, .com, windows, デュアルブート, tool, キーボード]
recommendations: [/post/2017-07-08_mbp--thinkpad-x1-carbon-2017-------46c374167b79/,
  /post/2017-08-26_python------------------dc8d8f2fe989/, /post/2012-01-07-mercurialtoqin-he-xing-nogao-iripozitoriburauzarhodecodewoinsutorusitemita/]
---

前回 [Thinkpad X1 Carbon(2017)のWindows周りの設定](https://chezo.uno/post/2017-07-08_mbp-thinkpad-x1-carbon-2017-46c374167b79/)について書きましたが、今回はUbuntu 17.04とのデュアルブートについて書きます。

{{< figure src="0_3JDXsLhEggqGGeR_.jpg" title="Ubuntu 17.04 on 4k monitor" >}}

基本的に、X1 Carbonに最初から入っているWindows 10がBitlockerが有効化されていてセキュアなので、以下を参照しながらデュアルブートにしました。（とはいってもうっかりUbuntu側をセキュアにし忘れた）

[**［まとめ］Ubuntu LTS と Windows とのデュアルブート環境の構築**  
_Ubuntu の入手について ［UEFI基本編］Ubuntu 16.04 LTS と Windows10 とのデュアルブート環境の構築 ［UEFI暗号化編］Ubuntu 16.04 LTS と Windows10 とのデュアルブート環境…_www.abten.net](https://www.abten.net/2017/02/1094/ "https://www.abten.net/2017/02/1094/")[](https://www.abten.net/2017/02/1094/)

新しいマシンなので、OS新しめにしておいたほうが良いかなと思ったので、Ubuntuは17.04にしました。とりあえず、長く使うかもわからないなぁと思ったので、楽にできる[日本語Remix](https://www.ubuntulinux.jp/News/ubuntu1704-ja-remix)で入れました。

### トラックポインタ＆タッチパッドが動かない問題

デフォルトだと、16.04も17.04もトラックポインタもタッチパッドも動きません。USBのThinkpadキーボードがあったのでなんとか回避できましたが、これができないと結構きつかったです。

ursmさんのブログのお陰でマウス系が動かない問題も回避できました。(とりあえず、カーネルパラメータに`psmouse.proto=imps`を指定してる)

[**Gentoo Linux on ThinkPad X1 Carbon 5th — lab.ursm.jp**  
_diff — git a/drivers/input/mouse/synaptics.c b/drivers/input/mouse/synaptics.c index 16c3046..0dff49e 100644 — — a…_ursm.jp](https://ursm.jp/blog/2017/06/04/gentoo-on-thinkpad-x1-carbon-5th-gen/ "https://ursm.jp/blog/2017/06/04/gentoo-on-thinkpad-x1-carbon-5th-gen/")[](https://ursm.jp/blog/2017/06/04/gentoo-on-thinkpad-x1-carbon-5th-gen/)

これだと、タッチパッドに手を置くと誤動作するので、BIOSでタッチパッドをオフにしておきます。

[**_タッチパッドを有効/無効にするには - ThinkPad_**  
タッチパッドを有効/無効にするには - ThinkPadsupport.lenovo.com](https://support.lenovo.com/jp/ja/solutions/ht075599 "https://support.lenovo.com/jp/ja/solutions/ht075599")[](https://support.lenovo.com/jp/ja/solutions/ht075599)

### 1Password問題

1Passwordに依存していたのですが、Keypassとかを入れるのはだるいなということで、1PasswordはWineを使って入れています。あまり困っていないです。

[**Ubuntuで1Passwordを使ってみる**  
_1Password使ってますか？私はWindows、Mac、iOS、Android、たくさんのデバイスでお世話になっています。これらのOSでは公式でソフトを入手することができますが、Linuxは未対応です。 公式で対応してくれれば一番良…_ry0.github.io](http://ry0.github.io/blog/2015/04/12/ubuntu-1password "http://ry0.github.io/blog/2015/04/12/ubuntu-1password")[](http://ry0.github.io/blog/2015/04/12/ubuntu-1password)

### USキーボードでの右AltでIME on/左AltでIME off

人間はIMEの状態を覚えたくないので（２回目）、右AltをIME on/左AltをIME offにします。やり方は、ここを参考に設定しました。

[**Ubuntuの入力モード切り替えのキーバインドを変更してMac風にする - Qiita**  
_UbuntuのキーバインドはWindows風なので普段Macを使ってるおしゃれピーポー には使いにくい。 Macの日本語キーボードのように「かな」キーと「英数」キーで入力モードを切り替えできるようにしよう。 従来の「半角/全角」キーによ…_qiita.com](http://qiita.com/yas-nyan/items/55e764304c67736ff9ba "http://qiita.com/yas-nyan/items/55e764304c67736ff9ba")[](http://qiita.com/yas-nyan/items/55e764304c67736ff9ba)

ただし、キーボード(日本語)が存在しないと、Mozcで入力しているときなぜか日本語配列になってしまうので、なければ追加します。

[**UbuntuのmozcでUSキーボード入力/JISキーボード入力を簡単に切り替える方法 - Qiita**  
_Ubuntuで意外に難しい、キーボードの「US/JIS」の切り替え設定を簡単にできる方法を紹介します。 なお、Ubuntuのバージョンは14.04で日本語入力はmozcで行うことを前提とした方法です。 (2017/06/17追…_qiita.com](http://qiita.com/AnchorBlues/items/beeb40593fd4c579dbe5 "http://qiita.com/AnchorBlues/items/beeb40593fd4c579dbe5")[](http://qiita.com/AnchorBlues/items/beeb40593fd4c579dbe5)

### Ctrl-Capsの入れ替え & Emacs風キーバインド

gnome-tweak-toolを使う。

[**Ubuntu 16.04でcaps lockをCtrlに変更 - soy-curd's blog**  
_askubuntu.com どおりに。 gnome-tweak-toolをインストール sudo apt-get install gnome-tweak-tool tweak toolを起動 Typings -> Caps Lock…_soy-curd.hatenablog.com](http://soy-curd.hatenablog.com/entry/2016/07/09/105102 "http://soy-curd.hatenablog.com/entry/2016/07/09/105102")[](http://soy-curd.hatenablog.com/entry/2016/07/09/105102)

sudo apt-get install gnome-tweak-tool

ちなみに、gnome-tweak-toolでEmacs風のキー設定にできる。こちらはWindowsでkeyhacをやるより賢く？、テキスト入力エリアのときだけEmacs keybindになってくれるので、自分のようなぬるいEmacs keybindを求めている人には助かります。

[**UbuntuのキーバインドをEmacs風にする - Qiita**  
_Ubuntu使うの初めてでよくわからなかったので備忘録に $ uname -a Linux vm-wamei 4.2.0-17-generic #21-Ubuntu SMP Fri Oct 23 19:56:16 UTC 2015…_qiita.com](http://qiita.com/wamei/items/a83680a3ad9b2f8f8dcc "http://qiita.com/wamei/items/a83680a3ad9b2f8f8dcc")[](http://qiita.com/wamei/items/a83680a3ad9b2f8f8dcc)

ただ、この方法だとmediumのようにkeyboard shortcutをJSで奪ってくるタイプのサイトには負けるらしく、もう少し厳密に必要な人は別の手段が必要そうです。

[http://qiita.com/AnchorBlues/items/beeb40593fd4c579dbe5](http://qiita.com/AnchorBlues/items/beeb40593fd4c579dbe5)

### デュアルブート下で時計がずれるのを防ぐ

そのままだと、Windowsに戻ったときに9時間時間がずれるので、Ubuntu側で設定を変えておく。

sudo timedatectl set-local-rtc true

### Grubの設定変更をGUIでする

Ubuntuをprimaryでやろうとしたけど、Windowsの方をよく使っているので、Grubの優先順位をGrub Customizer使って変える。

[**Grub Customizer - A graphical Grub2 settings manager**  
_https://launchpad.net/grub-customizer GRUB 2ブートローダーのGUI設定ツールです。例えば...パソコンの電源を入れて飛び込んでくるOS選択画面を こういう風にすることができます…_linux.ikoinoba.net](http://linux.ikoinoba.net/index.php?UID=1290446391 "http://linux.ikoinoba.net/index.php?UID=1290446391")[](http://linux.ikoinoba.net/index.php?UID=1290446391)

sudo add-apt-repository [ppa:danielrichter2007/grub-customizer](https://launchpad.net/~danielrichter2007/+archive/grub-customizer)  
sudo apt-get update && sudo apt-get install grub-customizer

### エディタはVisual Studio Code

別にJet Brains製品でもいいんですけど、とりあえずVSCodeをdebから入れておきました。

[**Running Visual Studio Code on Linux**  
_The easiest way to install for Debian/Ubuntu based distributions is to download and install the .deb package (64-bit…_code.visualstudio.com](https://code.visualstudio.com/docs/setup/linux "https://code.visualstudio.com/docs/setup/linux")[](https://code.visualstudio.com/docs/setup/linux)

### Python3とJupyterを入れる

[**Pythonの環境設定でむかついてる人はとりあえずこれをコピペで実行してください 2017.01 - YAMAGUCHI::weblog**  
_こんにちは、最近 Python をまた書き始めたマンです。なんか古い記事が参照されててだいぶ害があるので現状にあったやつにします。 これから Pythonを使い始める人、という前提に立っているので今更Python2系を使い始める意味はな…_ymotongpoo.hatenablog.com](http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124 "http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124")[](http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124)

ymotongpooさんの記事にもあるとおり、Debian/Ubuntu系のvenvは余計なものを入れるらしいので、virtualenv入れて使っています。

sudo apt-get install python3  
pip3 install virtualenv  
virtualenv hoge  
. hoge/bin/activate

### iRubyを入れる

まずは、rbenvとruby-buildを入れます。

*   [https://github.com/rbenv/rbenv](https://github.com/rbenv/rbenv)
*   [https://github.com/rbenv/ruby-build](https://github.com/rbenv/ruby-build#readme)

次にiRubyですが、READMEに従って入れましょう。ただ、一点libzmq-devは16.04にしかないのでlibzmq3-devを入れましょう。

[**SciRuby/iruby**  
_iruby - Official gem repository: Ruby kernel for Jupyter/IPython Notebook_github.com](https://github.com/SciRuby/iruby "https://github.com/SciRuby/iruby")[](https://github.com/SciRuby/iruby)

READMEのインストール手順を改変したのがこちら。

sudo apt install libtool libffi-dev ruby ruby-dev make  
gem install cztop  
  
sudo apt install git libzmq3-dev autoconf pkg-config  
git clone https://github.com/zeromq/czmq  
cd czmq  
./autogen.sh && ./configure && sudo make && sudo make install  
  
gem install iruby  
iruby register --force

\[追記\]

とのことです。わざわざ自分でビルドしなくても、 `sudo apt install czmq` でいけるのかな。

\[/追記\]

### Sphinxの執筆環境

Dockerのドキュメントに従って入れる。操作に `sudo` いることすら知らなかった。。。

[**Get Docker CE for Ubuntu**  
_To get started with Docker CE on Ubuntu, make sure you meet the prerequisites, then install Docker. Prerequisites…_docs.docker.com](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/ "https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/")[](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)

あとは、以下の通りでOK。

sudo docker pull chezou/sphinx-recommonmark  
sudo docker run -it -v $(pwd):/documents chezou/sphinx-recommonmark:latest make latexpdfja

_\[追記\]user権限でもいけるとのこと\[/追記\]_

### iPhoneでの有線テザリング

勉強会などでテザリングが必要なときがよくありますが、その場合は

[**Ubuntu 16.04 でiPhone にUSB でインターネット共有する - Keep on moving**  
_Ubuntu 15.10 から16.04にアップグレードしたところiPhoneでUSBでつないでインターネット共有できなくなったので つながるようにした時の作業内容をまとめます iphethのインストール これのインストールと有効化がひ…_masahito.hatenablog.com](http://masahito.hatenablog.com/entry/2016/05/29/235631 "http://masahito.hatenablog.com/entry/2016/05/29/235631")[](http://masahito.hatenablog.com/entry/2016/05/29/235631)

sudo apt-get install ipheth-utils  
sudo modprobe ipheth

とすればOKです。これを永続化するためには、先程のサイトにあるように `/etc/modules` への登録をお忘れなく。

### pbcopy/pbpaste

xselを使えばいけます。やり方はこちらのとおりです。

[**端末からクリップボードへのコピペする - Qiita**  
_Mac の場合はデフォルトで pbcopy/pbpaste というコマンドが用意されています echo "abcde" | pbcopy とすれば確認出来ると思います 便利すぎるので Ubuntu からでも使えるようにします ま…_qiita.com](http://qiita.com/catatsuy/items/0fd67f706366b2355e8f "http://qiita.com/catatsuy/items/0fd67f706366b2355e8f")[](http://qiita.com/catatsuy/items/0fd67f706366b2355e8f)

sudo apt-get install xsel

xselをあとは以下のようにaliasを設定すればOK。 `~/.zshrc`に入れました。

alias pbcopy**\=**'xsel --clipboard --input'  
alias pbpaste**\=**'xsel --clipboard --output'

### 環境変数周り用にenvchainを入れる

[**sorah/envchain**  
_envchain - Environment variables meet macOS Keychain and gnome-keyring <3_github.com](https://github.com/sorah/envchain "https://github.com/sorah/envchain")[](https://github.com/sorah/envchain)

AWSのsecretsなんかを引数に渡して実行するために便利なenvchainを入れました。READMEに従うだけです。今回、libsecretのヘッダが入っていなかったので入れました。

sudo apt install libsecret-1-dev

### まとめ

指紋認証とか細かいものは動きませんが、Skypeも入ってDMM英会話もできそうだし、BluetoothもWiFiも特に不安定なことなく動いています。Slackもアプリあるので困りません。会社的のVPNも通るし。

その他細かい設定は以下のサイトからつまんで設定しました。

[**Ubuntu 17.04をインストールした直後に行う設定 & インストールするソフト**  
_Ubuntuにログインすると画面左側に表示される、アプリ起動用のサイドバーのこと。タスクバーも兼用している。ここにアイコンを登録したい場合は、Dashからドラッグ＆ドロップする。左側から移動させることが出来ないのが不評だった…_sicklylife.at-ninja.jp](http://sicklylife.at-ninja.jp/memo/ubuntu1704/settings.html "http://sicklylife.at-ninja.jp/memo/ubuntu1704/settings.html")[](http://sicklylife.at-ninja.jp/memo/ubuntu1704/settings.html)

困っていることとしては、例によってメモアプリをどうするかという点（これはGoogle Keepでなんとかやろうとしている）と、辞書をどうするかという点（これは絶望的）です。まぁ、ブラウザベースで頑張るかなぁ。
