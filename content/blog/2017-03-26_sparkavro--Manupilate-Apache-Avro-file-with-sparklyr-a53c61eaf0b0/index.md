---
title: 'sparkavro: Manupilate Apache Avro file with sparklyr'
description: I created a simple sparklyr extension to handle Apache Avro file. It
  is just a simple wrapper of DataBrick’s spark-avro. It is listed in…
date: '2017-03-26T21:02:01+09:00'
categories: []
keywords: [avro, spark, sparklyr, sparkavro, sc, df, devtools, _avro, simple, library]
authors: [aki]
recommendations: [/blog/2016-12-30_Livy---Jupyter-Notebook---Sparkmagic---Powerful---Easy-Notebook-for-Data-Scientist-a8b72345ea2d/,
  /blog/2016-10-15_Building-predictive-Model-with-Ibis--Impala-and-scikit-learn-356b41f404e0/,
  /blog/2017-01-09_tabula-py--Extract-table-from-PDF-into-Python-DataFrame-6c7acfa5f302/]
---

I created a simple [sparklyr](http://spark.rstudio.com/) extension to handle Apache Avro file. It is just a simple wrapper of DataBrick’s [spark-avro](https://github.com/databricks/spark-avro). It is listed in [the official document of sparklyr extensions](http://spark.rstudio.com/extensions.html).

[**chezou/sparkavro**  
_sparkavro - Load Avro data into Spark with sparklyr_github.com](https://github.com/chezou/sparkavro "https://github.com/chezou/sparkavro")[](https://github.com/chezou/sparkavro)

### Installation

Use `{devtools}` to install sparkavro.

devtools::install\_github("chezou/avrospark")

### Simple usage

You can read and write Avro file as follows:

library(sparklyr)  
library(sparkavro)  
sc <- spark\_connect(master = "spark://HOST:PORT")  
df <- spark\_read\_avro(sc, "test\_table", "/user/foo/test.avro")  
spark\_write\_avro(df, "/tmp/output")

This is the very first version, so there might be bugs especially around options. If you find any bug, please raise on the [GitHub issue](https://github.com/chezou/sparkavro/issues).