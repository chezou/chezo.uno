---
title: 4 Steps to Release a CLI in Python
subtitle: ''
summary: ''
authors: [aki]
tags: [python, poetry]
categories: [python]
date: 2022-05-20 23:32:41-07:00
lastmod: 2022-05-20 23:32:41-07:00
featured: false
draft: false
image: {caption: Photo by Marc-Olivier Jodoin on Unsplash, focal_point: '', preview_only: false}
projects: []
keywords: [project, cli, pypi, token, create, dependency, written, package, python,
  need]
recommendations: [/blog/2019-11-26_how-to-release-python-package-from-github-actions-d5a1d8edba6e/,
  /blog/2017-08-30_python-basics--package-management-462918458f96/, /blog/2018-04-17_use-markdown-document-on-brand-new-pypi-9723024f09c2/]
---

This is what I learned from creating a Python CLI ([digdaglog2sql](https://github.com/chezou/digdaglog2sql)) in a day.

In just 4 steps, you can release a CLI written in Python easily.

## Create a project by using poetry

[Poetry](https://python-poetry.org/) is a modern Python packaging and dependency management tool. Poetry is becoming popular and defacto rapidly.

By using Poetry, it enables us to manage package dependency, to create a project template, and to publish to PyPI.

To setup a project with Poetry, this article is the best to read even if you build a CLI.

https://future--architect-github-io.translate.goog/articles/20210611a/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=ja&_x_tr_pto=wapp
(originally written in Japanese)

One thing I added to my project is [isort](https://pycqa.github.io/isort/index.html). isort is to sort imports automatically.

Here is the example of my project.

```toml
[tool.taskipy.tasks]
test = { cmd = "pytest tests", help = "runs all unit tests" }
pr_test = "task lint"
fmt = { cmd = "black tests digdaglog2sql && isort digdaglog2sql tests", help = "format code" }
lint = { cmd = "task lint_black && task lint_flake8 && task lint_isort && task lint_mypy", help = "exec lint" }
lint_flake8 = "flake8 --max-line-length=88 tests digdaglog2sql"
lint_mypy = "mypy tests digdaglog2sql"
lint_black = "black --check tests digdaglog2sql"
lint_isort = "isort digdaglog2sql tests --check-only"
```

## Create a CLI with Click/Cloup

[Click](https://palletsprojects.com/p/click/) is a famous Python package to build a command line tool.
You can easily create a CLI by using decorator.

Here is the example from the Click website:

```py
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()
```

[Cloup](https://cloup.readthedocs.io/en/stable/) is an extension of Click.

Using by Cloup, you can handle option groups and complex constraints like `mutually_exclusive` as:

```py
@option_group(
    "Cool options",
    option('--foo', help='This text should describe the option --foo.'),
    option('--bar', help='This text should describe the option --bar.'),
    constraint=mutually_exclusive,
)
```

Constraints of Cloup can validate the dependency and it also renders constraints in help.

## Use poetry-dynamic-versioning for version management

[poetry-dynamic-versioning](https://pypi.org/project/poetry-dynamic-versioning/) is a Python package to do same thing as [setuptools-scm](https://pypi.org/project/setuptools-scm/). You don't need to write version number by hand since this package use the version from tag of Git, e.g., "v.0.1.0".

Managing version by Git enables you to release to PyPI from GitHub Actions. This means you can release to PyPI on mobile device by releasing from GitHub.

After installation of poetry-dynamic-versioning, you just add three thing in pyproject.toml:

```toml
[tool.poetry]
version = "0.0.0"

[tool.poetry-dynamic-versioning]
enable = true

[build-system]
requires = ["poetry-core>=1.0.0", "poetry-dynamic-versioning"]
build-backend = "poetry.core.masonry.api"
```

Note that build-system configuration may vary depending on how you install poetry-dynamic-versioning. See the document for detail.

## Introduce GitHub Actions to release the package to PyPI

As I mentioned above, I highly recommend to use GitHub Actions to release a Package to PyPI.

Since GitHub provides [Release notes generation feature](https://docs.github.com/ja/repositories/releasing-projects-on-github/automatically-generated-release-notes) now, creating a release from GitHub with triggering PyPI release is the best way to publish a new version.

Here is the snippet of GH Actions to release to PyPI by using poetry.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/digdaglog2sql/blob/ce35ce9b0220b77a79998f594304d850da231a94/.github/workflows/python-publish.yml" data-iframely-url="//iframely.net/39Qsg8o?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

```yaml
name: Upload Python Package

on:
  release:
    types: [created]

permissions:
  contents: read

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install poetry
    - name: Build and publish package
      run: |
        poetry version $(git describe --tags --abbrev=0)
        poetry build
        poetry publish --username __token__ --password ${{ secrets.PYPI_API_TOKEN }}
```

Note that, while PyPI API Token can be found on PyPI, if you need to create project scope token, you need to upload a package manually first.
