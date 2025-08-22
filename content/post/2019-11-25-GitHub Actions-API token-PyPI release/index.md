---
authors: [aki]
date: '2019-11-24 23:59:00-08:00'
lastmod: '2019-11-26 09:31:00-08:00'
summary: GitHub Actionsを使うとPythonのテストが便利でReleaseも自動でできる
tags: [GitHub, Python]
title: GitHub ActionsでAPI tokenを使ってPyPIへリリースする
keywords: [actions, テスト, python, github, uses, twine, 環境変数, ついで, workflow, version]
recommendations: [/post/2018-01-17_----------------b63a0763e904/, /post/2017-08-26_python------------------dc8d8f2fe989/,
  /post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka/]
---

![](https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

ふと思い立ってtravisを捨ててGitHub Actionsを使ったPythonのテストを行うようにしてみた。また、ついでにPyPIへリリースもできるようにしてみた。

# GitHub ActionsをPythonのテストに使う

GitHub ActionsをPythonに使うメリットとしては

- OS (Ubuntu, macOS, Windows) や Python versionのmatrixが使えて複数バージョンのテストが楽
- JDKなど追加の依存のインストールも `uses` を使ってサクッとできる
- 起動もまあまあ速い

といった点が上げられる。

例えば、JDK 12を入れようと思ったら、このような記述をしてあげれば良い。楽。

```yaml
- uses: actions/setup-java@v1
      with:
        java-version: '12'
        java-package: jdk
        architecture: x64
```

一方、残念な点としては

- Windowsのtemp directoryへの書き込みが何故かできない
- マイナーなハマりどころに対して情報が少なくデバッグも厳しい

というところだろう。

実際のテストのワークフローはこちら

[chezou/tabula-py](https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythontest.yml)

# GitHub ActionsからPyPIへリリースする

実際のworkflowを見てもらうと速いと思う。

[chezou/tabula-py](https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythonpublish.yml)

もともと、公式で用意されていたWorkflowはReleaseが作成されたときにpublishされるというものだったが、[setuptools-scm](https://pypi.org/project/setuptools-scm/)でタグを付けるとバージョンも付与されるようにしていたので、

1. tagをpush (するとversionも付与される)。あるいはtagをGitHubで作成しても良い
2. GitHub Actionsによって、tagからreleaseが作成される
3. releaseからwheelを作成、PyPIへAPI Tokenを使ってpublishする

という流れを作ってみた。便利なのはtagを打ってpushするだけでこれが行けること。

ポイントは

```yaml
on:
  push:
    tags:
      - 'v*'
```

のように、トリガーをtagsにすることと

```yaml
deploy:
    needs: release
```

のように、 `release` jobを依存関係として追加すること。

PyPIのAPI Tokenは、予めPyPIにて取得しておく。Project単位でのscopeを設定できるので、今回はtabula-pyのアップロードのためにだけ使うことにした。 Projectの Settings → Secrets から `PYPI_USERNAME` を `__token__` に、 `PYPI_PASSWORD` を `pypi-` からはじまるAPI Tokenにすれば良い。ちょいちょいこの仕様が変わっていたこともあるので、最新情報は[ドキュメント](https://pypi.org/help/#apitoken)を確認してほしい。

```yaml
TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
```

Workflowの中にはtwine用の環境変数が用意されている。便利。

---

[Back to home](https://memo.chezo.uno/)