---
title: 'Python basics: package management'
description: Python is a very famous programming language for machine learning. In
  this article, I will introduce basic Python environment.
date: '2017-08-30T11:31:15+09:00'
categories: [python]
authors: [aki]
aliases: [/blog/python-basics-package-management-462918458f96, /blog/462918458f96]
keywords: [python, package, install, virtualenv, venv, pip, windows, packages, management,
  users]
recommendations: [/blog/2018-04-17_use-markdown-document-on-brand-new-pypi-9723024f09c2/,
  /blog/2017-07-24_simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9/,
  /blog/2022-05-21_fastest-way-to-release-python-cli/]
---

Python is a very famous programming language for machine learning. In this article, I will introduce basic Python environment.

### Glossary

I will introduce basic terms about Python package management.

*   pip: A tool for package installation. It retrieves Python packages from [PyPI](http://pypi.python.org/). pip is gem command of Ruby.
*   virtualenv: Package isolation tool for Python. It has similar function with bundler of Ruby, but it also has the function to change Python versions over 2.x and 3.x.
*   venv: It is an official tool for package isolation introduced from Python 3.3. But, if you want to use Python 2.x or you are Debian/Ubuntu user, I recommend you to use virtualenv.

venv switches with a command like `python3.5 -m venv some-awesome-env`, so it can’t handle over Python 2 and 3. venv installed by Debian/Ubuntu installs useless dependencies for other OSs, so I’m an Ubuntu user so I don’t use venv.

These are common tool sets for many Pythonistas. They are [recommended tools](https://packaging.python.org/guides/tool-recommendations/) of [PyPA](https://www.pypa.io/en/latest/), a working group that maintains many of the relevant projects in Python packaging.

There is one more tool that is for the specific purpose.

*   conda: conda is a tool for package management for scientific computation developed by [Anaconda](https://www.anaconda.com/), Inc. It can manage not only Python but also R. PyData community loves conda.

I use [conda for my work](http://blog.cloudera.com/blog/2017/05/create-conda-recipe-to-use-c-extended-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/), but I recommend you to know the pros/cons of conda and virtualenv/venv and chose write tool for your purpose.

### Installation of Python

Since it is 2017, Python beginners should use the latest version of Python 3. However, there are some cases to use Python 2.x for some painful reasons.

If you need to install Python 2 and 3, you can install multiple Python with package management tools like `apt` or `yum`. In Ubuntu, you can install Python 2.7 with `apt install python-dev`, and you can install Python 3.6 via `apt install python3-dev`.

After installation, you can see the Pythons under `/usr/bin`:

/usr/bin/python     #<- 2.7  
        /python2    #<- 2.7  
        /python2.7  #<- 2.7  
        /python3    #<- 3.6  
        /python3.6  #<- 3.6

If you’re macOS user, you can install both Python 2 and 3 via `brew install` or `port install`.

For Windows users, you can install Python 2 and 3 using official installer or Chocolatey. From Python 3.6 for Windows, there is `py` command that switches Python version.

**Caution**: Never try to keep using System Python. System Python is often old, and it depends on system critical system such as yum. If you run `sudo pip install` carelessly, there is a risk of destroying the environment of the OS itself.

### Package management

As I mentioned, you should not do `sudo pip install awesome-package`. Hence, Many important systems depend on system Python, don’t use `sudo pip`.

If you’re a venv user, this tutorial will help you.  
[https://docs.python.jp/3/tutorial/venv.html](https://docs.python.jp/3/tutorial/venv.html)

For virtualenv users, I will write a tutorial of virtualenv. It is a translation of the document written by aodag.  
[https://gist.github.com/aodag/bea141d255e22d204a2140fba658ebf2](https://gist.github.com/aodag/bea141d255e22d204a2140fba658ebf2)

#### Why should we use virtualenv/venv?

virtualenv avoids:  
\- Conflicting Python packages with system Python  
\- Conflicting packages between projects  
\- Losing sight of which project depends on those packages

#### Install virtualenv

First, you can install `virtualenv` under user home directory.

```sh
$ wget https://bootstrap.pypa.io/get-pip.py
$ export PATH=”~/.local/bin/:$PATH”
$ python get-pip.py --user
$ pip install virtualenv --user
\# Windows user can isntall just via \`pip install\`
\> pip install virtualenv
```

With `--user` option, you can install packages under user directory.

`virtualenv` can create a Python virtual environment. Creating the environment under the project root is common.

Run `virtualenv` as follows:

```sh
$ virtualenv venv -p python3.6
```

then, you can get virtual environment.

Since Python packages will be installed under the `venv` directory, don’t forget to add venv directory into `.gitignore`.

```sh
$ source venv/bin/activate  
(venv) $   
\# For Windows  
\> . venv/Script/activate
```

#### Install Python packages via pip

You can install packages via `pip`. After activating virtualenv/venv, pip will install packages under `venv` directory.

```sh
(venv) $ pip install pyramid
```

If you want to install the specific version of the package, you can set version number:

```sh
(venv) $ pip install pyramid==1.8.1
```

Without version number, `pip` will install latest stable version.  
[https://www.python.org/dev/peps/pep-0440/](https://www.python.org/dev/peps/pep-0440/)

You can list installed packages with `pip list` command.

```sh
(venv) $ pip list  
numpy (1.13.1)  
pandas (0.20.3)  
pip (9.0.1)  
pkginfo (1.4.1)  
pytest (3.2.0)  
python-dateutil (2.6.1)  
pytz (2017.2)  
wheel (0.29.0)
```

#### Managing package version

From pip 7.1, we can fix version of packages with `constraints.txt`. Using `pip freeze` command, you can list packages with a version number.

```sh
(venv)$ pip freeze -l  
numpy==1.13.1  
pandas==0.20.3  
pkginfo==1.4.1  
pytest==3.2.0  
python-dateutil==2.6.1  
pytz==2017.2  
(venv)$ pip freeze -l > constraints.txt
```

You should list your required packages into `requirements.txt`,

```sh
(venv)$ cat requirements.txt  
pandas  
numpy
```

Then you can install required packages as follows:

```sh
(venv)$ pip install -r requirements.txt -c constraints.txt
```

#### Levelaging wheelhouse

Modern Python package is distributed by wheel format, which is the binary type format. There is another format, sdist, which is the source type format and it requires compile from source if it depends on native codes. I highly recommend using wheel format, because it is faster installation than sdist without compilation and even if you have an offline environment which unable to connect PyPI you can deploy the project easily.

Put all dependent `.whl` format package files under `wheelhouse` directory, you can install as follows:

```sh
$ pip install -r requirements.txt -c constraints.txt -f wheelhouse — no-index
```

`-w` or `--wheel-dir` option allows you to set wheel directory. `-f` or`--find-links` option uses wheelhouse directory primary.`--no-index` option prevent to connect PyPI.

If you want to export all the dependencies into `wheelhouse` directory, you can use `pip wheel` command.

```sh
$ pip wheel -r requirements.txt -c constraints.txt -w wheelhouse
```

### Should I use conda?

Anaconda is a Python distribution for scientific computing such as machine learning. Anaconda suit consists of Anaconda, which includes the recommended package and Miniconda, which is the minimum environment for conda and you can install only necessary packages yourself. Anaconda sometimes includes heavy packages. It used to include Django, so check the default package and use it properly.

Unlike virtualenv, Anaconda can create its original virtual environment. Characteristically, using the `--copy` option makes it possible to copy system level libraries, .so, etc. without creating symbolic links. If you archive a set of virtual environments with zip or tar, you can use it on other machines.

```sh
$ conda create -n myenv --copy python=3.6  
$ conda activate myenv
```

In other words, libraries, which are managed by OS level package management tools such as `apt`, are also managed by conda. Conda has its own package repository different from PyPI and upload binaries for each OS on it. Since the same package, such as OpenCV, is registered in the repository by multiple users, you should care which package is the best one.

In many machine learning books, it is often written that conda can be used, but I think that it is better not to use it much outside Windows.

The reasons are as follows:

*   In 2017, wheel is de facto for the binary package format, so conda’s original purpose, handling scientific packages like numpy, or Scipy, can be done without conda.
*   conda will replace commands such as openssl/curl/python in macOS / Linux System (strictly speaking, conda will pass PATH first) \[[issue](https://github.com/ContinuumIO/anaconda-issues/issues/1119)\]
*   Package developers are often not conda users, and they seem to be asked for support in an environment that they do not normally use, such as JRuby or Rubyinius (or Windows specific trouble).
*   In the conda world, it is difficult to pass information that should be included in a build of a native extension (such as Cython dependence)

So I recommend using conda for Windows users or people do not develop heavily but want to experience machine learning. Or, put Miniconda under pyenv control. I use conda under Docker environment.

However, we can not install the package like Scipy on Windows via `pip install`, you need to download wheel on your own. I think that this point is better for honest conda.

Historical details are detailed in [this article](https://translate.google.com/translate?sl=ja&tl=en&js=y&prev=_t&hl=ja&ie=UTF-8&u=http:%2F%2Fymotongpoo.hatenablog.com%2Fentry%2F2017%2F02%2F02%2F182647&edit-text=). In short, because old binary format egg was not good, conda was created.

### Conclusion

I introduced installation of Python and how to manage Python packages. I think we can manage Python packages via virtualenv/venv well without conda, but there is good case for conda to pack some environment with system libraries.

### References

Original Japanese document:

- [Pythonの環境構築を自分なりに整理してみる](https://chezo.uno/post/2017-08-26_python-dc8d8f2fe989/)
- [pip - pip 9.0.1 documentation](https://pip.pypa.io/en/stable/)
- [Simple way to distribute your private Python packages within your organization](https://chezo.uno/blog/2017-07-24_simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9/)
