---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Create data lineage from Trino/Hive queries in digdag log with Python"
subtitle: "sqllineage visualize your query log into lineage"
summary: ""
authors: [aki]
tags: []
categories: [digdag, lineage, sql]
date: 2022-05-05T20:31:05-07:00
lastmod: 2022-05-05T20:31:05-07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "An example lineage of Treasure Workflow with sqllineage"
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
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

Note that, as of May 5, 2022, sqllineage and sqlparse, which is an important backend of sqllineage, are not fully compatible with Trino and Hive queries.

These are the PRs that approaches the issues:

- https://github.com/reata/sqllineage/pull/252
- https://github.com/reata/sqllineage/pull/255
- https://github.com/andialbrecht/sqlparse/pull/662
- https://github.com/andialbrecht/sqlparse/pull/664

Don't worry about it. I prepared patched branches on GitHub. You can install sqllineage and sqlparse as the following:

```sh
pip install git+https://github.com/chezou/sqlparse.git@trino#egg=sqlparse==0.4.3.dev0
pip install git+https://github.com/chezou/sqllineage.git@trino#egg=sqllineage==1.3.4
```

If you see some error on installation of sqllineage, double-check if you have node installed.

Then, you can visualize your SQL file as:

```sh
$ sqllineage -g -f output.sql
 * SQLLineage Running on http://localhost:5000/?f=output.sql
```

Now you can see visualization of data linage, both table level and column level.

{{< figure src="./featured.webp" title="SQL lineageの例" >}}

Let's try sqllineage!
