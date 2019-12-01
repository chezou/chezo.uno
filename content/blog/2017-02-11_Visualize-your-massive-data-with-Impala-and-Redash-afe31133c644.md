---
title: Visualize your massive data with Impala and Redash
description: >-
  Redash is a famous OSS visualization tool, which enables to visualize your
  data with SQL. It supports Apache Impala (incubating), fast…
date: '2017-02-11T14:14:44.539Z'
categories: []
keywords: []
authors: [aki]
---

[Redash](https://redash.io/) is a famous OSS visualization tool, which enables to visualize your data with SQL. It supports [Apache Impala (incubating)](http://impala.apache.org/), fast SQL-on-Hadoop suitable for BI tools and exploratory analysis. With Impala, you can [query SQLs to tables on Amazon S3](http://blog.cloudera.com/blog/2016/08/analytics-and-bi-on-amazon-s3-with-apache-impala-incubating/).

In this post, we connect to Impala from Redash and visualize data.

### Set up Redash

You can set up Redash with various way. This time, I use [AMI for Redash](https://redash.io/help-onpremise/setup/setting-up-redash-instance.html#create-an-instance). Then, you can access with your browser with admin/admin.

### Add Data Source of Impala

After clicking Database icon, you can add data sources.

This time, I set configurations as follows:

![Example configuration](/img/1__gMPHyBohg3nZKTDxtm__b__w.png)
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

![Result of Impala query](/img/1__Kk90BhI7L42fmIXPAn__mgg.png)
Result of Impala query