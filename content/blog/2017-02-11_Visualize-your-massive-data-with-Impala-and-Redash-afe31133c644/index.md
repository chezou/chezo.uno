---
title: Visualize your massive data with Impala and Redash
description: Redash is a famous OSS visualization tool, which enables to visualize
  your data with SQL. It supports Apache Impala (incubating), fast…
date: '2017-02-11T14:14:44+09:00'
categories: []
keywords: [impala, redash, query, data, set, hiveserver2, admin, database, visualize,
  result]
authors: [aki]
recommendations: [/blog/2017-03-26_How-to-connect-secure-Impala-cluster-from-RStudio-on-macOS-with-implyr-213c6536e4c7/,
  /blog/2016-10-15_Building-predictive-Model-with-Ibis--Impala-and-scikit-learn-356b41f404e0/,
  /blog/2019-04-24_Ruby-for-Data-Science-and-Machine-Learning-9f03e99125e0/]
---

[Redash](https://redash.io/) is a famous OSS visualization tool, which enables to visualize your data with SQL. It supports [Apache Impala (incubating)](http://impala.apache.org/), fast SQL-on-Hadoop suitable for BI tools and exploratory analysis. With Impala, you can [query SQLs to tables on Amazon S3](http://blog.cloudera.com/blog/2016/08/analytics-and-bi-on-amazon-s3-with-apache-impala-incubating/).

In this post, we connect to Impala from Redash and visualize data.

### Set up Redash

You can set up Redash with various way. This time, I use [AMI for Redash](https://redash.io/help-onpremise/setup/setting-up-redash-instance.html#create-an-instance). Then, you can access with your browser with admin/admin.

### Add Data Source of Impala

After clicking Database icon, you can add data sources.

This time, I set configurations as follows:

![Example configuration](1_gMPHyBohg3nZKTDxtm_b_w.png)
Example configuration

*   Type: Impala
*   Database: default
*   Host: hostname of Impala daemon
*   Ldap\_password/user: (empty)
*   Port: 21050 (default port)
*   Please specify beeswax or hiveserver2: hiveserver2
*   Timeout: 3600
*   Use\_ldap: (empty)

Now, you can select Impala as a data source.

![Result of Impala query](1_Kk90BhI7L42fmIXPAn_mgg.png)
Result of Impala query
