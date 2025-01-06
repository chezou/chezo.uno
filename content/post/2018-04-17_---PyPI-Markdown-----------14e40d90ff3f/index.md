---
title: 新しいPyPIでMarkdownのドキュメントを使う
description: 長い間、Pythonでパッケージを作った場合、構造化されたドキュメントを使う場合は、reStructuredText (reST)でドキュメントを書く必要がありました。
date: '2018-04-17T12:55:15+09:00'
categories: [python]
authors: [aki]
aliases: [/post/2018-04-17_-PyPI-Markdown-14e40d90ff3f/]
keywords: [pip, wheel, long, description, upgrade, content, py, version, setup, markdown]
recommendations: [/post/2018-12-01_windows-64bit-mecab--kytea-------2018-b283b6c7b33c/,
  /post/2017-08-26_python------------------dc8d8f2fe989/, /post/2015-06-06-pip-install-kyteadekiruyouninarimasita/]
---

長い間、Pythonでパッケージを作った場合、構造化されたドキュメントを使う場合は、[reStructuredText](http://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html) (reST)でドキュメントを書く必要がありました。

ところが、[aodag さん](https://twitter.com/aodag)に教えてもらったのですが2018年2月にアクセプトされた[PEP 566](https://www.python.org/dev/peps/pep-0566/#description-content-type-optional)のおかげで、PyPIのドキュメントがtxtかreSTでなければいけないという制約が外れました。そこで、昨日新しくなったばかりのPyPIでMarkdownがレンダーできる方法を試してみました。

### (必要に応じて)ライブラリをupgradeする

Markdownが扱えるようになったのは、[setuptoolsのv38.6.0](http://setuptools.readthedocs.io/en/latest/history.html#v38-6-0)からです。古いバージョンだとMarkdownがレンダーされないので、合わせてpipとwheelをupgradeしておきました。

$ python -m pip install --upgrade pip  
$ pip install --upgrade wheel  
$ pip --version  
pip 10.0.0 from c:\\users\\chezo\\documents\\source\\tabula-py\\venv\\lib\\site-packages\\pip (python 3.6)  
$ pip list  
Package           Version     Location  
\----------------- ----------- --------------------------------------  
(...snip...)  
setuptools        38.1.0  
(...snip...)  
wheel             0.31.0

### setup.pyを編集する

`long_description_content_type`という項目をsetup.pyに追加することで、reST以外の形式を使えるようになります。Markdownであれば例えば以下のようになると思います。

long\_description=open('README.md').read(),  
long\_description\_content\_type=”text/markdown”,

元々README.mdを読むようにしていたので、今回は `long_description_content_type` の行を追加するだけで済みました。

実際のPRはこちらです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/tabula-py/pull/85" data-iframely-url="//cdn.iframe.ly/HWuHFUO?card=small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

### wheelを作ってtwineでアップロードする

後はいつもどおりwheelを作ってtwineでPyPIにアップロードしました。なお、

$ python setup.py bdist\_wheel  
$ twine upload dist/\*

{{< figure src="1_dskznp-UI9jw4D9L6gAQLA.png" title="test.pypi.orgのMarkdownのドキュメントの様子" >}}

今回はこれだけのためにpatch versionを上げるのもなぁということで、test.pypi.orgにあげています。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://test.pypi.org/project/tabula-py/" data-iframely-url="//cdn.iframe.ly/NCS5gmm"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

### 参考文献

*   [PEP 566](https://www.python.org/dev/peps/pep-0566/#description-content-type-optional)の関連箇所
*   [https://github.com/pypa/readme\_renderer](https://github.com/pypa/readme_renderer)
*   [https://github.com/pypa/sampleproject/pull/66](https://github.com/pypa/sampleproject/pull/66)
