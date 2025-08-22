---
aliases: [/blog/py-operator-development-guide-for-python-users]
categories: [Python, workflow]
date: '2020-03-05 14:15:52-08:00'
draft: false
featured: false
summary: This article show how to develop a digdag Python workflow task efficiently.
tags: [digdag]
title: py> operator development guide for Python users
keywords: [operator, task, env, local, image, docker, create, reasonable, huge, single]
recommendations: [/blog/2019-10-06_how-to-test-a-new-docker-image-for-digdag-workflow-on-circleci--c8bb92987877/,
  /blog/2025-05-02-ml-project-and-scrum/, /blog/2024-01-26_scrape-notion-to-pdf/]
---

[Japanese version is here](https://chezo.uno/post/2019-12-24-python-custom-scripting/)

# How to build & test custom scripts on local env before pushing

General strategy:

* Make a Python task reasonable granularity to run on local env

Since Treasure Workflow doesn't have intermediate storage between tasks, a task can be huge. Considering container launch time, it would be better to create a single huge task, but it makes difficult for debugging. Starting from creating a reasonable size of function which is able to debug easily. Then, you can create a function that calls those minimal functions at once.

There are few options to develop py> operator on the local environment.

1. Use TD docker image
2. Create a Python virtual environment on local env

## 1. Use TD docker image

To develop a single py> operator task, you can use the official docker image to run python tasks locally. Like ordinal Python script, you can add the main guard like:

```py
if __name__ == "__main__":
    your_function("default_argument")
```

As of Mar. 5, 2020, our latest official images are shown as the following:

* digdag/digdag-python:3.7 [https://hub.docker.com/r/digdag/digdag-python](https://hub.docker.com/r/digdag/digdag-python "https\://hub.docker.com/r/digdag/digdag-python")
* digdag/digdag-anaconda3:2019.03 [https://hub.docker.com/r/digdag/digdag-anaconda3](https://hub.docker.com/r/digdag/digdag-anaconda3 "https\://hub.docker.com/r/digdag/digdag-anaconda3")

If you want to run a debugger toward Docker container, we recommend using PyCharm to run a remote debugger. See also [PyCharm document](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html).

## 2. Create a Python virtual environment on local env

Python provides venv to create virtual environments, you can create the same environment by using pip.

Download requirements.txt and constraints.txt from [the gist](https://gist.github.com/chezou/d0a0fc62007af4d808752e78b31ae694 "https\://gist.github.com/chezou/d0a0fc62007af4d808752e78b31ae694") and you can install dependencies as same environment with digdag-python:3.7 as:

```sh
$ python -m venv .venv 
$ source .venv/bin/activate 
(.venv)$ pip install -r requirements.txt -c constraints.txt`
```

Using this virtual environment, you can develop by using the same packages on the local environment.

Note that this approach can't ensure OS differences, which means the production environment is running on Debian but the development environment might be Windows/macOS X. This causes errors when executing OS-dependent commands like apt-get.

If you want to create the same environment with anaconda image, you can download environment.yml from [the gist](https://gist.github.com/chezou/d0a0fc62007af4d808752e78b31ae694#file-environment-yml), and run:

```
conda env update -n base -f environment.yml
```

Now you have the same Python packages with digdag/digdag-anaconda3:2019.03

Note that this command will overwrite existing conda environment, we highly recommend to modify name in environment.yml from base to your environment name like my-env, and run:

```
conda env create -f environment.yml
```

## Test a workflow including Python

If you want to run an entire workflow on the local environment, <del>you can use [digdag v0_10 branch](https://github.com/treasure-data/digdag/tree/v0_10)</del>.

{{% callout warning %}}
As of Mar 5, 2020, Treasure Data uses digdag v0_10 branch, but it may change in the near future.
{{% /callout %}}

{{% callout warning %}}
As of Feb 14, 2021, Treasure Data moved to v0_11 branch. You may use the latest release branch.
https://github.com/treasure-data/digdag/pull/1502
https://github.com/treasure-data/digdag/pull/1504
{{% /callout %}}


# Passing Parameters to py> operator

There are two ways to pass parameters into py> operator:

1. ordinal digdag argument
2. environment variable
3. digdag variable

## 1. digdag argument

Assuming we have a Python script named py_scripts/examples.py like:

```py
def print_arg(msg):
    print(f"Message is {msg}")
```

Passing msg argument from simple_with_arg task can be like:

```yaml
+simple_with_arg:
  py>: py_scripts.examples.print_arg
  msg: "Hello World"
  docker:
    image: "digdag/digdag-python:3.7"
```

If you want to pass multiple arguments, you can add arguments in your function, then add them into digdag arguments as well.

Note that digdag arguments can be passed into Python seamlessly so that you might face unintended variables passed by using keyword arguments \*\*kwargs.

For example, in this case, docker variable can be passed as a dictionary {"image": "digdag/digdag-python:3.7"}. We recommend having implicit arguments on a Python function.

Note that there might be unintended conflicts between digdag and py> operator. Assuming you set some digdag variables like the following:

```yaml
_export:
  td:
    database: my_db

+simple_with_arg2:
  py>: py_scripts.examples.print_arg_td
  msg: "Hello World"
  docker:
   image: "digdag/digdag-python:3.7"
```

having python function print_arg_td with td argument like the following:

```py
def print_arg_td(msg, td=None):
    print(f"'msg' is {msg} and 'td' is {td}")
```

In this case, td variable never can be None since exported td variable, i.e., {"database": "my_db"} always should be passed. This may cause type mismatches like dictionary and string. We recommend avoiding to use preserved arguments for digdag, like td variables like:

* td.endpoint
* td.apikey
* td.use_ssl
* td.proxy.enabled
* td.proxy.host
* td.proxy.port
* td.proxy.password
* td.proxy.user

Note that these variables might be changed in the future. There are build-in digdag variables. See digdag build-in variables at [http://docs.digdag.io/workflow_definition.html#using-variables](http://docs.digdag.io/workflow_definition.html#using-variables "http\://docs.digdag.io/workflow_definition.html#using-variables")

Also, digdag might converts unintended type e.g., an integer from a string, so we recommend to evaluate or explicitly convert type on a Python function.

## 2. environment variable

Environment variables can be another option to pass parameters to py> operator. An environment variable is reasonable for passing secure information or secrets.

For example, if we have a task simple_with_env

```yaml
+simple_with_env:
  py>: py_scripts.examples.print_env
  _env:
    MY_ENV_VAR: "hello"
  docker:
    image: "digdag/digdag-python:3.7"
```

This MY_ENV_VAR can be accessed by using os.environ like:

```py
import os

def print_env():
    print(f'Env var is {os.environ["MY_ENV_VAR"]}')
```

Using an environment variable should be important especially when you need to use secrets information e.g. Treasure Data API key or AWS secrets key, etc.

digdag has a feature to store secrets information. Secrets are stored on digdag (or Treasure Workflow) database when executing td workflow secrets subcommand.

![](https://chezo.uno/post/2019-12-24-python-custom-scripting/digdag_secrets.png)


Assuming you've set a secret named td.apikey. This secret can be passed to py> operator like:

```yaml
+simple_with_env2:
  py>: py_scripts.examples.access_td
  _env:
    TD_API_KEY: ${secret:td.apikey}
  docker: image: "digdag/digdag-python:3.7"
```

from py_scripts/examples.py like:

```py
import os

def access_td():
    apikey = os.environ["TD_API_KEY"]
    # Do awesome execution
```

If you try to pass secrets from ordinal digdag arguments, secrets will never be fetched from secrets DB. For example, if you have a task like the following:

```yaml
+simple_with_env_ng:
  py>: py_scripts.examples.access_td_ng
  apikey: ${secret:td.apikey}
  docker: image: "digdag/digdag-python:3.7"
```

by using the following script like:

```py
def access_td_ng(apikey):
    print(apikey)
    # Always shows "${secret:td.apikey}" insted of actual API key like "1234/XXXX"
```

## 3. digdag variable

If you want to read digdag variable in a Python script, you can use digdag.env.params as the following:

```py
def read_workflow_env(msg):
    import digdag
    print(digdag.env.params["my_msg"])
```

Note that import digdag can be run only when the script is run as a digdag py> operator task. If you want to avoid import error, you should write try-except syntax like:

```py
try:
    import digdag
    digdag.env.store({"feature_query": feature_query})
except ImportError:
    pass
```



# Directory structures

I recommend having the following directory structure.

```
my_project
├── README.md
├── config
│   ├── params.test.yml     <- Configuration file for run through test. Mirror params.yml except for `td.database`
│   └── params.yml          <- Configuration file for production
├── awesome_workflow.dig    <- Main workflow to be executed
├── ingest.dig              <- Data ingestion workflow
├── py_scripts              <- Python scripts directory
│   ├── __init__.py
│   ├── data.py             <- Script to upload data to Arm Treasure Data
│   └── my_script.py        <- Main script to execute e.g. Data enrichment, ML training
├── queries                 <- SQL directory
│   └── example.sql
├── run_test.sh             <- Test shell script for local run through test
└── test.dig                <- Test workflow for local run through test
```

You can generate this structure from a template by using cookiecutter-digdag.

[chezou/cookiecutter-digdag](https://github.com/chezou/cookiecutter-digdag "https\://github.com/chezou/cookiecutter-digdag")

# How to install Python packages / OS packages

For installation of Python packages, you can use os.syste or subprocess.run like:

```py
import os, sys
os.system(f"{sys.executable} -m pip install --upgrade pytd==1.4.3")

import subprocess
# arguments should be passed by list
subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pytd==1.4.3"])
```

Ensure you set the version number of Python package.

To install OS packages, you can execute like the following:

```py
import os
os.system("apt-get update") # Need to run before doing apt-get install
os.system("apt-get install -y wkhtmltopdf")
```


# How to read/write tiny variables between digdag tasks

To read a digdag variable, you can use digdag.env.params as mentioned above.

To pass variables to another Python task, you can use import digdag.

```py
def store_workflow_env(msg):
    import digdag
    digdag.env.store({"my_msg": msg})
```


This example code sets my_msg variable which is able to use the following tasks like:

```yaml
+store_msg:
  py>: py_scripts.examples.store_workflow_env
  msg: "Hello World"
    docker:
      image: "digdag/digdag-python:3.7"

+restore_msg:
  echo>: ${my_msg}
```

# Error notification with Python stack trace

digdag has _error: syntax to send a notification for an error message. You can access ${error.message} digdag variable to send the notification for Slack or Email.

Assuming that if we have the following workflow:

```yaml
+simple_raise_error:
    py>: py_scripts.examples.error_sample
    docker:
        image: "digdag/digdag-python:3.7"

_error:
    echo>: ${error.message}
```


with this Python script:

```py
def error_sample():
    int("a1234") # raises ValueError
```


This script always raises ValueError and the workflow log shows stack trace of Python as the following:

```
2019-12-24 23:06:32 +0900 [INFO] (0039@[0:python]+simple^error): echo>: Python command failed with code 1: invalid literal for int() with base 10: 'a1234' (ValueError)
  from Traceback (most recent call last):
  from File ".digdag/tmp/digdag-py-2-1815457087076518360/runner.py", line 165, in <module>
    result = callable_type(**args)
  from File "/private/var/folders/y9/bnjb3krn39s22rmg_wvlnf7m0000gp/T/digdag-tempdir2111531196420040503/workspace/1_simple_1_2_2945225080250994454/py_scripts/examples.py", line 5, in print_arg
    int("a1234")
  from ValueError: invalid literal for int() with base 10: 'a1234' (runtime)
```


In this example, we use echo> operator to show the error message, but you can use mail> operator for sending Email or http> operator to send a Slack message.