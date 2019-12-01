---
title: 'sparkavro: Manupilate Apache Avro file with sparklyr'
description: >-
  I created a simple sparklyr extension to handle Apache Avro file. It is just a
  simple wrapper of DataBrick’s spark-avro. It is listed in…
date: '2017-03-26T21:02:01.640Z'
categories: []
keywords: []
authors: [aki]
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