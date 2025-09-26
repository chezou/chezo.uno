---
authors: [aki]
categories: [Python, TreasureData]
date: '2019-12-23 07:00:00-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2019-12-23 07:00:00-08:00'
projects: []
subtitle: ''
summary: ''
tags: [Python]
title: Pythonistaのためのdigdag py> operator開発ガイド
toc: true
keywords: [treasure, workflow, 開発, タスク, イメージ, digdag, data, python, docker, 公式]
recommendations: [/post/2019-11-18-digdag-ci/, /post/2019-12-04-r-and-td/, /post/2019-11-16-tdworkflow/]
---

{{< toc >}}

この記事は、[Arm Treasure Data Advent Calendar 2019](https://adventar.org/calendars/3932)の24日目です。

今年の夏に新しくTreasure Dataで使えるようになったPython Custom Scriptingですが、
開発する際にどういう点を気をつければ良いのかという質問をいただくことが多いので、
今日はTreasure Workflowとdigdagのpy> operatorを使った開発の際に気をつけることを書いて行こうと思います。

なお、Treasure WorkflowとありますがOSSのdigdagでも活かせる内容があると思います。

なお、既にPython Custom Scriptingが試せる環境にある方は、このGoogle Colab notebook https://bit.ly/191212_cs で一通り試すことが出来ます。

## workflowをpushするまえにローカル環境で開発とテストをする方法

### 基本戦略:Pythonのタスクを合理的な粒度にまとめる

Treasure Workflowやdigdagのサーバーモードでは、タスク間の中間ファイルを置くためのストレージがないため、一つ一つのタスクの粒度が大きくなりがちです。
特に、Treasure Workflowでは一つ一つのtaskでコンテナが起動するため、そのオーバーヘッドを無視できません。
一方で、一つの巨大なタスクは、開発時のデバッグを難しくさせます。
そこで、開発時の戦略としては一つ一つは最低限の塊に分けた関数を用意します。そして、必要に応じてそれらを束ねる関数を用意するのが良いでしょう。

Treasure Workflow向けのworkflowをローカル環境で開発するにはいくつかの選択肢があります。

1. Treasure Dataの公式Dockerイメージを使う
2. Dockerイメージと同じPythonの仮想環境を使う

### 1. Treasure Dataの公式Dockerイメージを使う

基本的にはTreasure Dataが提供している公式イメージを利用すると、本番環境と同じイメージが使うことができるので良いでしょう。

その際には、他のPythonスクリプトの開発と同様に、切り分けた単体で実行できるようにして開発するのが良いでしょう。

```py
if __name__ == "__main__":
    your_function("default_argument")
```

2019/12/23現在、最新のDocker imageは以下の2つです。

- digdag/digdag-python:3.7 https://hub.docker.com/r/digdag/digdag-python
- digdag/digdag-anaconda3:2019.03 https://hub.docker.com/r/digdag/digdag-anaconda3

PyCharmのProfessional Editionを持っている場合、Dockerのコンテナにremote debuggerがアタッチできるので便利です。
詳しくは[PyCharmのドキュメント](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html)をご参照ください。

### 2. Dockerイメージと同様のPythonの仮想環境を作る

Python は仮想環境を作るための `venv` と呼ばれるモジュールがあります。
これを使うことで他のプロジェクトと分離したパッケージの環境を作ることができます。

#### digdag-python:3.7

digdag-python:3.7と同様の環境を作るには、次のgistからrequirements.txtとconstraints.txtをダウンロードします。
https://gist.github.com/chezou/d0a0fc62007af4d808752e78b31ae694

その後、以下のようにコマンドを実行することでDockerイメージと同様のPython環境が構築できます。

```sh
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt -c constraints.txt
```

> [!NOTE]
> この方法では、OSによる差異まで吸収ができない場合があります。
> 例えば、digdag-python:3.7はDebianベースなので、OSレベルのパッケージ管理は `apt-get` を使いますが、それをスクリプト内に書いても実行ができません。

#### digdag-anaconda3:2019.03

anacondaイメージと同じ環境を作りたい場合は、gistからenvironment.ymlをダウンロードします。
https://gist.github.com/chezou/d0a0fc62007af4d808752e78b31ae694#file-environment-yml

その後、以下のコマンドを実行するとデフォルトの環境に依存するパッケージをインストールします。

```sh
conda env update -n base -f environment.yml
```

なお、新しい環境を構築したい場合は、environment.ymlの中の `base` を `my-env` など好きな名前に変更した後、以下のコマンドで新規仮想環境を作成してください。

```sh
conda env create -f environment.yml
```

### py> operatorを含んだworkflowをローカルで実行する

もし、ローカル環境でworkflow全体を実行したい場合は、 <del>[digdagの v0_10ブランチ](https://github.com/treasure-data/digdag/tree/v0_10)を使うことで、
本番環境に近いdigdag環境が用意できます</del>。

> [!WARNING]
> 2019/12/23現在は、Treasure Dataではv0_10を使っていますが、将来これは変わる恐れがあります。

> [!WARNING]
> 2021/02/14現在、v0_11へと移行しました。今後は適宜適切なブランチを使うようにしてください。
> https://github.com/treasure-data/digdag/pull/1502
> https://github.com/treasure-data/digdag/pull/1504

## py> operatorにパラメータを渡す

py> operatorにパラメータを渡すには2つの方法があります。

1. digdagの引数を使う
2. 環境変数を使う
3. digdagの変数でやりとりする

### 1. digdagの引数を使う

以下のような `py_scripts/examples.py` というスクリプトがあるとします。

```py
def print_arg(msg):
    print(f"Message is {msg}")
```

`msg` という変数を `print_arg` という関数に渡す場合、以下のようなdigdagのtaskになります。

```yaml
+simple_with_arg:
  py>: py_scripts.examples.print_arg
  msg: "Hello World"
  docker:
    image: "digdag/digdag-python:3.7"
```

もし、複数の引数をPythonの関数へ渡したい場合、digdagの引数を増やせばよいでしょう。

ここで注意してほしいのが、digdagの変数はPythonにシームレスに渡されるということです。
つまり、 `**kwargs` などで引数を受け取る場合、意図しないdigdagの変数がPythonに渡る可能性に注意してください。

例えば、上の例では `docker` という変数には `{"image": "digdag/digdag-python:3.7"}` という辞書型の変数が代入されています。
ですので、 `**kwargs` で受けるのではなく、明示的な引数の指定を強くおすすめします。

た、同様に意図しないdigdagの変数と py> operatorの引数の衝突が起こる場合があります。
以下のようなワークフローがあったとします。

```yaml
_export:
  td:
    database: my_db

+simple_with_arg2:
  py>: py_scripts.examples.print_arg_td
  msg: "Hello World"
  docker:
    image: "digdag/digdag-python:3.7"
```

このとき、Pythonのスクリプトは以下のような関数を持っているとします。

```py
def print_arg_td(msg: str, td: str = None):
    print(f"'msg' is {msg} and 'td' is {td}")
```

`simple_with_arg2` タスク実行時に `print_arg_td` 関数へ渡される引数 `td` は何になるでしょうか？
通常のPythonの感覚では、デフォルト値である `None` が期待されます。
しかし、 digdagのワークフローで `td` という変数がすでにexportされているため、 引数 `td` には `{"database": "my_db"}` という辞書が格納されてしまいます。
これにより、変数 `td` の型(`dict`)が期待されていたもの(`str`)との不一致が起こりうるのです。

このようなミスマッチを避けるために、digdagで予約されている変数やよく利用される変数を避けたほうが良いでしょう。
特に `td` という変数や以下の変数は避けたほうが良いです。

- td.endpoint
- td.apikey
- td.use_ssl
- td.proxy.enabled
- td.proxy.host
- td.proxy.port
- td.proxy.password
- td.proxy.user

これらの既に利用されている変数は将来的に変更される可能性があります。

digdagの組み込み変数は次のドキュメントをご参照ください。
http://docs.digdag.io/workflow_definition.html#using-variables

また、digdagは `int` から `str` など意図しない型の変換を行う場合があります。そのため、型のチェックや明示的な変換をおすすめします。

### 2. 環境変数を使う

環境変数は、py> operatorに変数を渡すためのもう一つの方法です。

TDのAPI keyやAWSのsecret keyなどセキュアな情報はこの形式でやりとりすることが多いです。

例えば、以下のような `simple_with_env` というタスクがあったとします。

```yaml
+simple_with_env:
  py>: py_scripts.examples.print_env
  _env:
    MY_ENV_VAR: "hello"
  docker:
    image: "digdag/digdag-python:3.7"
```

このとき、 `MY_ENV_VAR` は以下のようにPythonから取得できます。

```py
import os
def print_env():
    print(f'Env var is {os.environ["MY_ENV_VAR"]}')
```

Treasure Workflowではセキュアな情報を扱うためにdigdagの `secrets` を格納するデータベースを提供しています。

{{< figure src="digdag_secrets.png" title="Digdag Secretsの設定フロー" >}}

1. Projectを `td workflow push` でプッシュする
2. secretsを `td workflow secrets` でデータベースに格納する
3. secretsを `{secret:my_secret}` という形式でworkflowに書き、環境変数経由でPythonにわたす

環境変数での受け渡しをしないとsecretsはPythonに渡されません。
例えば、以下のようなワークフローとPythonスクリプトでは正しくsecretsに格納された `td.apikey` という情報が渡されます。

```yaml
+simple_with_env2:
  py>: py_scripts.examples.access_td
  _env:
    TD_API_KEY: ${secret:td.apikey}
  docker:
    image: "digdag/digdag-python:3.7"
```

```py
import os
def access_td():
    # Able to fetch API key like "1234/XXXX"
    apikey = os.environ["TD_API_KEY"]
    # Do awesome execution
```

しかし、以下のようにdigdagの引数として渡した場合はsecretsが評価されません。

```yaml
+simple_with_env_ng:
  py>: py_scripts.examples.access_td_ng
  apikey: ${secret:td.apikey}
  docker:
    image: "digdag/digdag-python:3.7"
```

```py
def access_td_ng(apikey):
    # Always shows "${secret:td.apikey}" instead of actual API key like "1234/XXXX"
    print(apikey)
```

secretsに関する詳細は、[digdagのドキュメント](https://docs.digdag.io/command_reference.html#secrets)をご参照ください。

### 3. digdagの変数を使う

digdagのpy> operatorとして実行するPythonスクリプトでは、 `import digdag` とすることでdigdagモジュールを利用することが出来ます。

以下のように、 `digdag.env.params` と呼ばれる変数に辞書のようにアクセスすることでdigdagの変数を直接読むことが出来ます。

```py
def read_workflow_env():
    import digdag
    print(digdag.env.params["my_msg"])
```

このとき、実行するworkflowは例えば以下のようなものになります。

```yaml
_export:
  my_msg: "awesome message"

+simple_with_arg2:
  py>: py_scripts.examples.read_workflow_env
  docker:
    image: "digdag/digdag-python:3.7"
```

なお、読み込みだけではなく`digdag.env.store`を使うことでdigdagの変数の書き込みもできます。
ただし、あまり大きな変数の受け渡しはしないほうが良いでしょう。

```py
def store_workflow_env(msg):
    import digdag
    digdag.env.store({"my_msg": msg})
```

このdigdagモジュールは、digdagがpy> operator実行時に動的に生成しているため、ローカルでは実行できないことに注意してください。
ローカルの実行を考慮する場合は、 `try-expect` を利用するのが良いでしょう。

```py
try:
    import digdag
    digdag.env.store({"feature_query": feature_query})
except ImportError:
    pass
```

## PythonやOSのパッケージのインストール方法

Treasure WorkflowではDocker imageに入っていないパッケージは `os.system` や `subprocess.run`を使い実行します。

```py
import os, sys
os.system(f"{sys.executable} -m pip install --upgrade pytd==1.4.3")

import subprocess
# arguments should be passed by list
subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pytd==1.4.3"])
```

この際、パッケージのバージョンを指定しましょう。

OSのパッケージのインストールの場合も同様です。

```py
import os
os.system("apt-get update") # Need to run before doing apt-get install
os.system("apt-get install -y wkhtmltopdf")
```

## py> operatorを含むディレクトリ構成

一つのプロジェクトでは、以下のようなディレクトリ構成をおすすめしています。

```txt
my_project
├── README.md
├── config
│   ├── params.test.yml     <- Configuration file for run through test. Mirror params.yml except for `td.database`
│   └── params.yml          <- Configuration file for production
├── awesome_workflow.dig    <- Main workflow to be executed
├── ingest.dig              <- Data ingestion workflow
├── py_scripts              <- Python scripts directory
│   ├── __init__.py
│   ├── data.py             <- Script to upload data to Arm Treasure Data
│   └── my_script.py        <- Main script to execute e.g. Data enrichment, ML training
├── queries                 <- SQL directory
│   └── example.sql
├── run_test.sh             <- Test shell script for local run through test
└── test.dig                <- Test workflow for local run through test
```

この構成に従ったdigdagプロジェクトをcookiecutter-digdagを使うことで簡単にテンプレートから生成できます。
https://github.com/chezou/cookiecutter-digdag

## 実行時のエラーを通知する

Pythonのスクリプト実行時に発生したエラーをSlackなどで通知したい事があると思います。
digdagは `_error:` でworkflowが失敗した際の処理をできますが、そのとき`${error.message}`の中にPythonの例外情報が入っています。

以下のようなworkflowとPython scriptがあったとします。

```yaml
+simple_raise_error:
    py>: py_scripts.examples.error_sample
    docker:
        image: "digdag/digdag-python:3.7"

_error:
    echo>: ${error.message}
```

```py
def error_sample():
    int("a1234") # raises ValueError
```

このとき、以下のようなログが得られます。

```txt
2019-12-24 23:06:32 +0900 [INFO] (0039@[0:python]+simple^error): echo>: Python command failed with code 1: invalid literal for int() with base 10: 'a1234' (ValueError)
	from Traceback (most recent call last):
	from File ".digdag/tmp/digdag-py-2-1815457087076518360/runner.py", line 165, in <module>
    result = callable_type(**args)
	from File "/private/var/folders/y9/bnjb3krn39s22rmg_wvlnf7m0000gp/T/digdag-tempdir2111531196420040503/workspace/1_simple_1_2_2945225080250994454/py_scripts/examples.py", line 5, in print_arg
    int("a1234")
	from ValueError: invalid literal for int() with base 10: 'a1234' (runtime)
```

この例では、`echo>` operatorでエラーを出力しているだけですが、Slack等に例外を送ることで定期実行しているPythonタスクの通知が簡単に行なえます。

## まとめ

このように、様々なポイントをおさえることでTreasure Workflowの開発をしやすくなるかと思います。
また、digdagでもいくらかのポイントは使うことができるかと思います。
