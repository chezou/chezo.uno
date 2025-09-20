---
authors: [aki]
date: '2019-11-17 08:38:00-08:00'
lastmod: '2019-11-17 08:56:00-08:00'
summary: digdagのworkflowを実行可能かチェックするためのポイントとcookiecutterの紹介
tags: [Engineering, OSS]
title: digdagのworkflowをCIでrun throughする
keywords: [workflow, digdag, テスト, file, pycharm, boxes, 実際, ため, レンダー, デバッグ]
recommendations: [/post/2019-12-24-python-custom-scripting/, /post/2019-11-16-tdworkflow/,
  /post/2018-01-17_----------------b63a0763e904/]
---

![](https://images.unsplash.com/photo-1534644107580-3a4dbd494a95?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

以前、kawasaki.rbやマジフェスでdigdagのworkflowのデバッグやテストどうすればいいんだ〜という話をしました。

[How do you debug/test your Workflow?](https://docs.google.com/presentation/d/1hvF29KsE3WmIfoC98EONJjZKovqUFYlHNIKOSZIX_GU/edit?usp=drivesdk)

この話は、でかいデータと戯れるworkflowをどうdebug、テストすればいいのかという話から、PyCharmとDockerでdebugするという話をしましたが、今回はworkflowを実際にrun throughできるようにするためのtipsとそれを実現するためのcookiecutterを作ったので紹介しようと思います。

## cookiecutter-digdag

[chezou/cookiecutter-digdag](https://github.com/chezou/cookiecutter-digdag)

[cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html)はPythonで書かれたプロジェクトを作るためのテンプレートです。内部ではPythonのtemplate engineであるjinja2を使っており、普通HTMLをレンダーするために使うものをconfiguration fileやfile名、directoryに使ってしまおうと言うものです。

```bash
$ pip install --user cookiecutter
```

でcookiecutterをインストールしたら、

```bash
cookiecutter https://github.com/chezou/cookiecutter-digdag
```

とすれば、ディレクトリ以下に新しいpy> operatorを使ったdigdagプロジェクトができます。

```
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
├── run_test.sh             <- Test shell script for local run through test
└── test.dig                <- Test workflow for local run through test
```

## run through testをCIで走らせるためのポイント

これだけだとふーんなんですけど、ポイントとしては `test.dig` に詰まっています。

```yaml
_export:
  !include : config/params.yml

_error:
  td_ddl>:
  drop_databases: ["${td.database}"]

+ingest:
  call>: ingest.dig

+execute:
  call>: {{cookiecutter.main_workflow}}.dig

+cleanup:
  td_ddl>:
  drop_databases: ["${td.database}"]
```

特徴は

1.  `config/params.yml` にDB名の設定を指定する
2.  `ingest.dig` でデータのDBの作成とデータの書き込みをする
3.  `{{cookiecutter.main_workflow}}.dig` (デフォルトは `awesome_workflow.dig` )でcookiecutter使用時に指定されるメインのワークフローをcallする
4. `cleanup` と `_error` taskでDBを削除する

という4点です。

実際には、テストは `run_test.sh` を実行することで行われるのですが、その中身を見てみましょう。

```bash
mv config/params.test.yml config/params.yml
{{cookiecutter.digdag_path}} run test.dig
```

`digdag_path` はデフォルト `digdag`となり、local modeでdigdagを実行します。

`mv config/params.test.yml config/params.yml` と `params.test.yml` に差し替えをするのですが、

```yaml
# Target Database on Treasure Data
td:
  database: "{{cookiecutter.database}}_${session_uuid.replace(/-/g,'_')}"
  table: {{cookiecutter.table}}
```

このように、 `_${session_uuid.replace(/-/g,'_')}`とユニークな文字列を作ることで、一時的なDB名を作るようにしています。

このやり方をすることで、メインのワークフローに極力触ることなく、CIでlocalモードのdigdagを使い走り切るかのテストができます。実際にこの構成で行っているworkflowの例は[treasure-boxes](https://github.com/treasure-data/treasure-boxes)レポジトリにあるので、参考にしてください。

---

[Back to home](https://memo.chezo.uno/)