---
aliases: [/blog/how-to-connect-secure-impala-cluster-from-rstudio-on-macos-with-implyr-213c6536e4c7,
  /blog/213c6536e4c7]
authors: [aki]
categories: []
date: '2017-03-25 14:35:45-07:00'
description: Impala is very fast SQL-on-Hadoop, and it will enhance your R experience
  with implyr, a dplyr based interface for Apache Impala…
title: How to connect secure Impala cluster from RStudio on macOS with implyr
keywords: [impala, driver, cloudera, configuration, setting, set, install, replace,
  connect, description]
recommendations: [/blog/2017-02-11_visualize-your-massive-data-with-impala-and-redash-afe31133c644/,
  /blog/2016-10-15_building-predictive-model-with-ibis--impala-and-scikit-learn-356b41f404e0/,
  /blog/2017-08-02_how-to-run-cloudera-director-on-your-macos-windows-10-710f82aa1d63/]
---

Impala is very fast SQL-on-Hadoop, and it will enhance your R experience with [implyr](https://github.com/ianmcook/implyr), a [dplyr](https://cran.r-project.org/package=dplyr) based interface for [Apache Impala (incubating)](https://impala.apache.org/) created by [Ian Cook](https://medium.com/u/d7dc303a303b). I will show you how to setup connection to Kerberized Impala cluster with implyr from local macOS. You can find my GitHub repo as follows:

[**chezou/implyr-example**  
_implyr-example - Example repository of implyr_github.com](https://github.com/chezou/implyr-example "https://github.com/chezou/implyr-example")[](https://github.com/chezou/implyr-example)

### Setting up ODBC environment for macOS

#### Install unixODBC with homebrew

First, we will install [unixODBC](http://www.unixodbc.org/) to handle Impala with ODBC. In R world, ODBC is preferred to connect Impala because of its performance and compatibility. Let’s install unixODBC with homebrew.

$ brew install unixodbc

#### Download and install the latest version of the Impala ODBC driver from Cloudera

You can download [the latest Impala ODBC Driver](https://www.cloudera.com/downloads/connectors/impala/odbc.html).

#### Configure your .odbc.ini and .odbcinst.ini

After installing Impala ODBC driver for macOS, basic configuration templates can be found in `/opt/cloudera/impalaodbc/Setup/`.

cp /opt/cloudera/impalaodbc/Setup/odbc.ini ~/.odbc.ini  
cp /opt/cloudera/impalaodbc/Setup/odbcinst.ini ~/.odbcinst.ini

Before using following setting, you must replace `HOST` and `KrbRealm` with appropriate ones. Let’s modify your `.odbc.ini` as follows:

\[ODBC\]  
\# Specify any global ODBC configuration here such as ODBC tracing.

\[ODBC Data Sources\]  
Impala=Cloudera ODBC Driver for Impala

\[Impala\]

\# Description: DSN Description.  
\# This key is not necessary and is only to give a description of the data source.  
Description=Cloudera Impala ODBC Driver DSN

\# Driver: The location where the ODBC driver is installed to.  
Driver=/opt/cloudera/impalaodbc/lib/universal/libclouderaimpalaodbc.dylib

\# The DriverUnicodeEncoding setting is only used for SimbaDM  
\# When set to 1, SimbaDM runs in UTF-16 mode.  
\# When set to 2, SimbaDM runs in UTF-8 mode.  
#DriverUnicodeEncoding=2

\# Values for HOST, PORT, KrbFQDN, and KrbServiceName should be set here.  
\# They can also be specified on the connection string.  
HOST=\[REPLACE\_YOUR\_IMPALA\_HOST\]  
PORT=21050  
Schema=default

\# The authentication mechanism.  
\# 0 — No authentication (NOSASL)  
\# 1 — Kerberos authentication (SASL)  
\# 2 — Username authentication (SASL)  
\# 3 — Username/password authentication (NOSASL or SASL depending on UseSASL configuration)  
AuthMech=1

\# Set to 1 to use SASL for authentication.   
\# Set to 0 to not use SASL.   
\# When using Kerberos authentication (SASL) or Username authentication (SASL) SASL is always used  
\# and this configuration is ignored. SASL is always not used for No authentication (NOSASL).  
UseSASL=1

\# Kerberos related settings.  
KrbFQDN=\_HOST  
KrbRealm=\[REPLACE\_YOUR\_REALM\]  
KrbServiceName=impala

\# Username/password authentication with SASL settings.  
UID=  
PWD=

\# Set to 0 to disable SSL.  
\# Set to 1 to enable SSL.  
SSL=1  
CAIssuedCertNamesMismatch=1  
TrustedCerts=/opt/cloudera/impalaodbc/lib/universal/cacerts.pem

\# If you use SSL with AllowSelfSignedServerCert, you can set this configuration.  
#AllowSelfSignedServerCert=1

\# Specify the proxy user ID to use.  
#DelegationUID=

\# General settings  
TSaslTransportBufSize=1000  
RowsFetchedPerBlock=10000  
SocketTimeout=0  
StringColumnLength=32767  
UseNativeQuery=0

After setting up the `.odbc.ini` , your application will refer this setting with appropriate DSN name, like `Impala` in this case.

#### Check the configuration

After configuration, you should kinit with your principal.

$ kinit $USER@YOUR\_REALM

You should replace \`$USER\` and \`YOUR\_REALM\` with the appropriate REALM.

Before using RStudio on you mac, you can check configuration with \`isql\` command.

$ isql -v “Impala”  
\+ — — — — — — — — — — — — — — — — — — — -+  
| Connected!                             |  
|                                        |  
| sql-statement                          |  
| help \[tablename\]                       |  
| quit                                   |  
|                                        |  
\+ — — — — — — — — — — — — — — — — — — — -+  
SQL>

### Implyr Example

After setting .odbc.ini you can connect secure Impala cluster with `{implyr}`. For instance, We will visualize [the airports’ data](http://openflights.org/data.html#airport).

First, install R packages.

install.packages(c(“implyr”, “odbc”, “DBI”, “dplyr”, “ggplot2”, “ggExtra”))

Then, connect the Impala cluster.

library(implyr)  
library(odbc)  
drv <- odbc::odbc()  
impala <- src\_impala(  
 drv = drv,  
 dsn = “Impala”  
)

If your `.odbc.ini` is configured properly, you can connect to Impala cluster.

Let’s visualize the airports data. In this case, we assume the data is in `u_ariga` database, so that we will change database using SQL `use u_ariga`.

library(DBI)  
\# Change database  
dbExecute(impala, “use u\_ariga”)  
dbGetQuery(impala, “show tables”)  
airports <- tbl(impala, “airports\_pq”)

\# Show the head of airports data  
View(airports)

airports %>% filter(latitude < 35) %>% count()  
#903

Finally, we will show a joint histogram of longitude and latitude.

airports\_by\_geo <- airports %>% select(longitude, latitude) %>% collect()

library(ggplot2)

p <- ggplot(airports\_by\_geo, aes(longitude, latitude)) + geom\_point() + theme\_classic()  
ggExtra::ggMarginal(p, type = “histogram”)

![](1_SscW2sneYR_lphETyF7y1A.png)

### Conclusion

`{implyr}` is a great package for Impala and dplyr but it is pretty young project. If you find some problems, why don’t you post into [the GitHub issue](https://github.com/ianmcook/implyr/issues)?