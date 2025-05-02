---
title: Create data lineage from Trino/Hive queries in digdag log with Python
subtitle: sqllineage visualize your query log into lineage
summary: ''
authors: [aki]
tags: []
categories: [digdag, lineage, sql]
date: 2022-05-05 20:31:05-07:00
lastmod: 2022-05-05 20:31:05-07:00
featured: false
draft: false
image: {caption: An example lineage of Treasure Workflow with sqllineage, focal_point: '',
  preview_only: false}
projects: []
keywords: [data, sqls, logs, treasure, workflow, log, learned, visualize, level, python]
recommendations: [/blog/2016-10-15_building-predictive-model-with-ibis--impala-and-scikit-learn-356b41f404e0/,
  /blog/2017-02-11_visualize-your-massive-data-with-impala-and-redash-afe31133c644/,
  /blog/2019-04-24_ruby-for-data-science-and-machine-learning-9f03e99125e0/]
---

## What's data lineage?

Data lineage is something to describe "Where this data comes from and where it goes?"

I learned this term in my previous job. They provided "Cloudera Navigator" which includes data lineage from execution logs of Hive/Spark etc.

{{< figure src="./nav_lineage.webp" title="lineage of Cloudera Navigator via https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cn_lineage_generation.html" >}}

## sqllineage is awesome open source tool for visualizing lineage

Recently, I learned there is a Python package so called sqllinage, that makes analyze and visualize data lineage from SQLs.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/reata/sqllineage" data-iframely-url="//iframely.net/4q6WPtz?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

sqllineage consists of Python implementation to analyze SQL and web application written in React.

## Visualize data lineage from Treasure Data's workflow logs

I found that Treasure Data's workflow log outputs SQLs in its log. But it still needs to format pure SQLs.

Then, I create digdaglog2sql to extract SQLs from Treasure Workflow logs.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/digdaglog2sql" data-iframely-url="//iframely.net/5Up1iQ9?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

You can use it with Python 3.7+. Here is the overview of the usage and check details on GitHub.

Install via pip:

```sh
pip install --user digdaglog2sql
```

If you have a workflow log downloaded from Treasure Data, you can convert into SQL as:

```sh
digdaglog2sql --input workflow-log.txt --output output.sql
```

Or, if you want extract SQLs from specific workflow, you can use Session ID of it.

```sh
export TD_API_KEY=1234XXX/YYYYYYYY
digdaglog2sql --session-id 12345 --site us --output output.sql
```

You can fetch SQLs from your hosted digdag as the following:

```sh
digdaglog2sql --session-id 12345 --endpoint digdag.example.com --output output.sql
```

~~Note that, as of May 5, 2022, sqllineage and sqlparse, which is an important backend of sqllineage, are not fully compatible with Trino and Hive queries.~~

{{% callout note %}}
As of 2022/05/11, the issues in sqllineage around Hive/Trino were fixed and it is available in 1.3.5 on PyPI.
It means, you don't have to have node for sqllineage installation from source.

As of 2022/10/06, the issue in sqlparse was resolved in 0.4.3.
{{% /callout %}}

~~These are the PRs that approaches the issues:~~

- ✅ https://github.com/reata/sqllineage/pull/252 -> Released in 1.3.5
- ✅ https://github.com/reata/sqllineage/pull/255 -> Released in 1.3.5
- ✅ https://github.com/andialbrecht/sqlparse/pull/662 -> Released in 0.4.3
- ✅ https://github.com/andialbrecht/sqlparse/pull/664 -> Released in 0.4.3

~~Don't worry about it. I prepared patched branches on GitHub. You can install sqllineage and sqlparse as the following:~~

```sh
pip install git+https://github.com/chezou/sqlparse.git@trino#egg=sqlparse==0.4.3.dev0
pip install sqllineage
```

~~If you see some error on installation of sqllineage, double-check if you have node installed.~~

Then, you can visualize your SQL file as:

```sh
$ sqllineage -g -f output.sql
 * SQLLineage Running on http://localhost:5000/?f=output.sql
```

Now you can see visualization of data linage, both table level and column level.

{{< figure src="./featured.webp" title="SQL lineageの例" >}}

Let's try sqllineage!
