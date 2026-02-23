---
aliases: [/blog/how-to-test-a-new-Docker-image-for-digdag-workflow-on-circleci-c8bb92987877,
  /blog/c8bb92987877]
authors: [aki]
categories: []
date: '2019-10-05 13:17:30-07:00'
description: Testing workflow runnability would be important when we build a complex
  workflow. digdag is a workflow engine which syntax is simple and…
title: How to test a new Docker image for digdag workflow on CircleCI?
keywords: [docker, run, workflow, image, volume, tmp, container, machine, repo, ll]
recommendations: [/blog/2020-03-05_py-operator-development-guide-for-python-users/,
  /blog/2017-08-02_how-to-run-cloudera-director-on-your-macos-windows-10-710f82aa1d63/,
  /blog/2017-03-26_how-to-connect-secure-impala-cluster-from-rstudio-on-macos-with-implyr-213c6536e4c7/]
---

{{< figure src="./0__Sj4niOaDd__W4bydD.jpg" title="Photo by [Campaign Creators](https://unsplash.com/@campaign_creators?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)" >}}
Photo by [Campaign Creators](https://unsplash.com/@campaign_creators?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Testing workflow runnability would be important when we build a complex workflow. [digdag](https://www.digdag.io) is a workflow engine which syntax is simple and is able to run tasks with SQL, Python, Ruby, shell script, etc. digdag has Docker executor and it works like a charm with `py>`, `rb>`, and `sh>` operators.

How to ensure a new Docker image runnable with existing digdag workflow? I’ll show the way to run through it on CircleCI.

You can see the example repo on GitHub:

[**chezou/digdag\_circleci**  
_You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…_github.com](https://github.com/chezou/digdag_circleci "https://github.com/chezou/digdag_circleci")[](https://github.com/chezou/digdag_circleci)

### An issue with digdag Docker executor on CircleCI

Although CircleCI docker executor is the primary choice for CircleCI 2.0, which easily run with arbitrary Docker image, [it doesn’t provide volume mount for docker](https://support.circleci.com/hc/en-us/articles/360007324514-How-can-I-mount-volumes-to-docker-containers-) since it launches remote sibling docker container. Hence digdag Docker executor assumes to mount a volume, like `-v /tmp:/tmp`, you need some workaround to avoid it.

[**FileNotFoundError occurs in python operator in docker · Issue #649 · treasure-data/digdag**  
_HI. I am running the digdag server in the docker container with the following version. # docker --version Docker…_github.com](https://github.com/treasure-data/digdag/issues/649 "https://github.com/treasure-data/digdag/issues/649")[](https://github.com/treasure-data/digdag/issues/649)

In this article, I’ll show you how to execute local mode digdag, a.k.a. `didgag run`, on CircleCI with digdag docker executor.

### Use CircleCI machine executor

tl;dr, use CircleCI [machine executor](https://circleci.com/docs/2.0/executor-types/#using-machine), which runs VM on CircleCI.

```
version: 2jobs:  test:    working_directory: ~/app    machine:      image: ubuntu-1604:201903-01      docker_layer_caching: true    steps:      - checkout      - run:          name: Install digdag          command: |            curl -o ~/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-latest"            chmod +x ~/bin/digdag            echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc      - run:          name: Test digdag run          command: |            set -x            digdag run test.dig
```

Machine executor has Python, Ruby, Java, and Docker CE by default, so you can easily run digdag on CircleCI.

Here are the dig file and Python script.

```
# test.dig+task:  py>: test.show  docker:    image: "python:3.7-slim-buster"
```

Python script:

```
# test.pydef show():    print("Hello CircleCI")
```

### Build custom Docker image and test with digdag

In some cases, you want to test whether a new Docker image works appropriately with existing workflow.

If you build a new Docker image for digdag Docker executor and test with existing workflow, you can write like the following:

```
version: 2jobs:  build_and_test:    working_directory: ~/app    machine:      image: ubuntu-1604:201903-01      docker_layer_caching: true    steps:      - checkout      - run:          name: Install digdag          command: |            curl -o ~/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-latest"            chmod +x ~/bin/digdag            echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc      - run:          name: Build application Docker image          command: |            docker build -f ./Dockerfile -t chezou/my-image:latest .      - run:          name: Test treasure-boxes workflows          command: |            set -x            digdag run test_custom.dig
```

Building a Docker image on CircleCI, you can use it form `digdag run` command with the following workflow and Dockerfile.

```
# test_custom.dig+task:  py>: test.show  docker:    image: "chezou/my-image:latest"
```

```
# DockerfileFROM python:3.7-slim-buster
```

```
RUN pip install tabula-py
```

```
CMD ["python3"]
```

### Conclusion

*   Using CircleCI’s machine executor enables to use `digdag run` with digdag Docker executor.
*   It empowers us to do run through test for new Docker image with existing workflow on CircleCI

You can try it with this GitHub repo:

[https://github.com/chezou/digdag_circleci](https://github.com/chezou/digdag_circleci)