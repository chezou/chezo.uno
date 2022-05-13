---
title: How to run Cloudera Director on your macOS/Windows 10
description: Cloudera Director is a provisioning tool for CDH and Cloudera Enterprise.
  We can launch cluster with Web GUI or CLI tool. Using Cloudera…
date: '2017-08-02T12:12:31+09:00'
categories: []
authors: [aki]
aliases: [/blog/how-to-run-cloudera-director-on-your-macos-windows-10-710f82aa1d63,
  /blog/710f82aa1d63]
keywords: [cloudera, director, server, windows, launch, install, homebrew, '10', docker,
  com]
recommendations: [/blog/2017-03-26_how-to-connect-secure-impala-cluster-from-rstudio-on-macos-with-implyr-213c6536e4c7/,
  /blog/2016-12-30_livy---jupyter-notebook---sparkmagic---powerful---easy-notebook-for-data-scientist-a8b72345ea2d/,
  /blog/2017-07-24_simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9/]
---


Cloudera Director is a provisioning tool for CDH and Cloudera Enterprise. We can launch cluster with Web GUI or CLI tool. Using Cloudera Director CLI tool, you can manage your cluster with configuration file, that enables you to manage configurations with git. In this article, I will introduce how to install Cloudera Director into your local macOS or Windows 10.

For usage of Cloudera Director, see also the document.

[**_Cloudera Director 2.5.x Documentation_**  
Cloudera Director 2.5.x Documentationwww.cloudera.com](https://www.cloudera.com/documentation/director/latest.html "https://www.cloudera.com/documentation/director/latest.html")[](https://www.cloudera.com/documentation/director/latest.html)

### Install Cloudera Director on you macOS with homebrew

If you’re homebrew user, you can install Cloudera Director easily.

[**chezou/homebrew-cloudera**  
_homebrew-cloudera - Homebrew Formulas for cloudera tools_github.com](https://github.com/chezou/homebrew-cloudera "https://github.com/chezou/homebrew-cloudera")[](https://github.com/chezou/homebrew-cloudera)

$ brew tap chezou/cloudera  
$ brew install cloudera-director-server

Then, you can launch/terminate Cloudera Director as follows:

\# Start Cloudera Director Server background  
$ cloudera-director-server-start  
\# After launching director server, you can open with http://locahost:7189/

\# Stop Cloudera Director Server background  
$ cloudera-director-server-stop

### Install Cloudera Director on you Windows 10

If you are Windows 10 user, you can install Ubuntu as the [Linux Subsystem](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

Launch bash on windows, then run as follows:

Make sure to get not IP address of Windows but Ubuntu’s one.

### Use Docker image

If you don’t want to install your machine directly, you can use Docker image of Cloudera Director.

[**tsuyo/cloudera-boot**  
_cloudera-boot - Cloudera Director Utilities_github.com](https://github.com/tsuyo/cloudera-boot "https://github.com/tsuyo/cloudera-boot")[](https://github.com/tsuyo/cloudera-boot)

After installation of Docker, run following commands then your Director will launch.

```
$ git clone https://github.com/tsuyo/cloudera-boot$ cd cloudera-boot$ . bin/cloudera-boot.sh # load several functions/aliases$ cb-build # may take a while# set you secrets
```

You can launch a Director server or use client as well. To get further information, see also README.md.
