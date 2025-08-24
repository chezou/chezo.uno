---
title: tabula-py 2.8.0 now uses jpype to launch JVM
subtitle: ''
summary: ''
authors: []
tags: []
categories: [python]
date: 2023-09-09 17:13:08-07:00
lastmod: 2023-09-09 17:13:08-07:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [java_options, tabula, version, default, change, solved, allow, py, theme,
  release]
recommendations: [/blog/2017-01-09_tabula-py--extract-table-from-pdf-into-python-dataframe-6c7acfa5f302/,
  /blog/2017-05-28_tabula-py-now-able-to-extract-remote-pdf-and-multiple-tables-at-once-6108e24ac07c/,
  /blog/2019-02-18_a-recent-update-of-tabula-py-a923d2ab667b/]
---

Recently, I released tabula-py 2.8.0. It is a major release because it uses [jpype](https://jpype.readthedocs.io/en/latest/) to launch JVM. This means that it reduces JVM launch time since jpype reuse JVM via JNI.

## How fast is it?

I measured `read_pdf_with_template` function execution time, which repeatedly launches Java process in the previous version. 

The example template contains 4 rules, which means it calls tabula-java 4 times.

```sh
$ cat examples/data.tabula-template.json | jq
[
  {
    "page": 1,
    "extraction_method": "guess",
    "x1": 153.99985500000003,
    "x2": 565.5698550000001,
    "y1": 123.999615,
    "y2": 531.7446150000001,
    "width": 411.57,
    "height": 407.745
  },
  {
    "page": 2,
    "extraction_method": "guess",
    "x1": 153.99985500000003,
    "x2": 453.879855,
    "y1": 123.99884999999993,
    "y2": 210.44384999999994,
    "width": 299.88,
    "height": 86.44500000000001
  },
  {
    "page": 2,
    "extraction_method": "guess",
    "x1": 153.99985500000003,
    "x2": 487.53985500000005,
    "y1": 410.99625000000003,
    "y2": 497.44125,
    "width": 333.54,
    "height": 86.44500000000001
  },
  {
    "page": 3,
    "extraction_method": "guess",
    "x1": 153.99985500000003,
    "x2": 235.85485500000001,
    "y1": 123.99885000000012,
    "y2": 322.8988500000001,
    "width": 81.855,
    "height": 198.9
  }
```

The result is as follows:


v2.7.0:

```sh
$ python -m timeit 'import tabula; tabula.read_pdf_with_template("examples/data.pdf", "examples/data.tabula-template.json")' 2> /dev/null
1 loop, best of 5: 1.31 sec per loop
```

v2.8.0:

```sh
$ python -m timeit 'import tabula; tabula.read_pdf_with_template("examples/data.pdf", "examples/data.tabula-template.json")' 2> /dev/null
1 loop, best of 5: 75 msec per loop
```

It is 17 times faster than the previous version!

## Caveats

Since [jpype doesn't allow to reboot JVM](https://jpype.readthedocs.io/en/latest/api.html#jpype.shutdownJVM), you can pass `java_options` for the first time only. If you want to change `java_options`, you need to restart Python process.

## Challenges for releasing v2.8.0

I had to solve several challenges to release this version.

### The test issue with different `java_options`

As I mentioned, jpype doesn't allow to reboot JVM. This causes unit test with different `java_options` to fail. I solved this by separating run with nox session.

See https://github.com/chezou/tabula-py/pull/356/files#r1306600161 for details.

This limitation is not a big deal for tabula-py users because tabula-py users don't need to change `java_options` frequently.

### Read the docs default behavior change

Read the docs changed the default installation packages for Sphinx. I didn't declared the dependency for Sphinx, so it caused the build failure.

The default behavior of RTD was just installing the latest version of Sphinx and sphinx-rtd-theme, however, now it installs very old version of them like: https://github.com/readthedocs/readthedocs.org/issues/10670#issuecomment-1694761746

I solved this by pinning the versions of dependency for Sphinx and sphinx-rtd-theme.
