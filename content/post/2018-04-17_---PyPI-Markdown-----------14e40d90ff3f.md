---
title: 新しいPyPIでMarkdownのドキュメントを使う
description: >-
  長い間、Pythonでパッケージを作った場合、構造化されたドキュメントを使う場合は、reStructuredText
  (reST)でドキュメントを書く必要がありました。
date: '2018-04-17T12:55:15.825Z'
categories: [python]
keywords: []
authors: [aki]
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

[**Handle markdown long description for Pypi by chezou · Pull Request #85 · chezou/tabula-py**  
_Thanks for PEP 566, as of setuptools v38.6.0, PyPI can render long description written in markdown. This PR allows…_github.com](https://github.com/chezou/tabula-py/pull/85 "https://github.com/chezou/tabula-py/pull/85")[](https://github.com/chezou/tabula-py/pull/85)

### wheelを作ってtwineでアップロードする

後はいつもどおりwheelを作ってtwineでPyPIにアップロードしました。なお、

$ python setup.py bdist\_wheel  
$ twine upload dist/\*

![test.pypi.orgのMarkdownのドキュメントの様子](https://cdn-images-1.medium.com/max/800/1*dskznp-UI9jw4D9L6gAQLA.png)
test.pypi.orgのMarkdownのドキュメントの様子

今回はこれだけのためにpatch versionを上げるのもなぁということで、test.pypi.orgにあげています。

[**tabula-py**  
_Simple wrapper for tabula, read tables from PDF into DataFrame_test.pypi.org](https://test.pypi.org/project/tabula-py/1.0.0/ "https://test.pypi.org/project/tabula-py/1.0.0/")[](https://test.pypi.org/project/tabula-py/1.0.0/)

### 参考文献

*   [PEP 566](https://www.python.org/dev/peps/pep-0566/#description-content-type-optional)の関連箇所
*   [https://github.com/pypa/readme\_renderer](https://github.com/pypa/readme_renderer)
*   [https://github.com/pypa/sampleproject/pull/66](https://github.com/pypa/sampleproject/pull/66)