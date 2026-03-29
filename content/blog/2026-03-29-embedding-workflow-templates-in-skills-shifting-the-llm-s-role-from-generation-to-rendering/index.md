---
title: 'Embedding workflow templates in skills: shifting the LLM''s role from "generation"
  to "rendering"'
subtitle: ''
summary: ''
date: 2026-03-28 18:23:00-07:00
lastmod: ''
categories: [agent, LLM]
tags: [Development]
draft: false
featured: false
image: null
recommendations: [/blog/2020-03-05_py-operator-development-guide-for-python-users/,
  /blog/2022-05-05-sqllineage-with-digdag-log/, /blog/2019-06-04_the-first-conference-of-operational-machine-learning--opml--19-308baad36108/]
---

## The dream of LLM-powered ML workflow generation

At my company, an ML feature called [AI Signals](https://docs.treasuredata.com/products/customer-data-platform/machine-learning/ai-signals) provides capabilities like RFM analysis, recommendation, and contextual bandits. To run ML predictions at scale, the system calls an ML API that spins up parallel workers on AWS Batch behind the scenes. To make this parallelization work, input tables are aggregated per profile, which is a deliberate trade-off for scalability. These processes are orchestrated through digdag workflows (.dig files, executed on Treasure Workflow, a hosted digdag service) containing SQL (Hive or Trino), where the ML API is invoked via digdag's `http>` operator.

Originally, the pre-processing and post-processing workflows were built by MLEs on a paid Professional Services team using their own templates, then deployed to customers who purchased PS engagements. But there was a desire to scale this beyond PS customers, and LLM-based workflow and SQL generation was seen as the path forward. Despite models getting better every day, generating stable workflows and SQL with LLMs proved difficult. For example, TD-specific UDFs in SQL don't come naturally to the models. After several attempts, we had given up.

## The rise of Claude Code and agent-friendly CLIs

Then our CEO called for a push toward becoming an AI-native organization, and Claude Code was rolled out company-wide. Adoption spread beyond software engineers to PdMs, Solution Architects, and even sales. Two developments were particularly impactful: [tdx](https://tdx.treasuredata.com/), a unified agent-friendly CLI that can call TD's various microservice APIs, and [Treasure Studio](https://tdx.treasuredata.com/studio/), a desktop application built on top of tdx. With Claude Code and tdx working together, agents could create marketing journeys, analyze tables in TD, and visualize results. The CEO personally created onboarding challenge tasks for employees to accelerate adoption, and as a result, automation has been spreading across both internal and customer environments.

Out of this momentum, a Skills marketplace was born for both [customer-facing](https://github.com/treasure-data/td-skills) and internal use. These skills improve reproducibility and accelerate automation of complex tasks.

## What the agent-friendly CLI made possible

The biggest contribution of tdx was exposing Treasure Workflow's endpoints through a CLI, which let Claude Code autonomously create workflows, push them, run them, inspect the results, and iterate. Workflows can take anywhere from a few minutes to over an hour to execute, which has always made automated testing painful.

Thanks to Claude Code + tdx, it became possible to generate a workflow, queue it for execution in the background, and verify the results. This was a game changer.

An agent-friendly CLI that handles API interactions end-to-end is no longer a nice-to-have. It's essential.

## Turning ML workflow templates into skills

That said, as I mentioned at the top, no matter how smart Claude Code's models get, it's still hard for an LLM to generate workflows that are consistently reliable for anyone to run, especially for customers with no prior knowledge.

So I reframed the problem. If generating workflows and SQL from scratch is too hard, why not create templates that generate workflows and SQL from configuration parameters? By embedding templates in a skill, the LLM's responsibility narrows from "generate workflows and SQL from scratch" to "choose the right parameters for the data and the problem." The workflows themselves become deterministic since they're pre-built as templates. Deterministic logic should live in scripts, not in the LLM's probabilistic output.

This idea was inspired by how cdp-api dynamically generates digdag workflows from database values.

<script defer class="speakerdeck-embed" data-slide="29" data-id="dcef99361823438cb3b542784fa07b56" data-ratio="1.7772511848341233" src="//speakerdeck.com/assets/embed.js"></script>

[https://speakerdeck.com/aamine/treasure-data-techtalk-2022-td-cdp-in-30-minutes?slide=29](https://speakerdeck.com/aamine/treasure-data-techtalk-2022-td-cdp-in-30-minutes?slide=29) (Japanese, see slide 29 for the code example)

## Jinja2 templates for digdag workflows

Concretely, I templated the .dig files with Jinja2 and had the LLM focus on determining configuration values, with config.yml as the single source of truth for all modifiable parameters. Claude renders the templates directly from config.yml without any external tooling. Seeing the `.dig.j2` extension for the first time gave me a small thrill.

Internally, I use two kinds of variables: render-time parameters with `{{ }}` and digdag runtime parameters with `${ }`. The former handles things like branching on whether the SQL engine is Hive or Trino, or when algorithms and hyperparameter candidates can be fixed ahead of time. The latter is for cases like storing hyperparameter tuning results in a table, then dynamically assigning those values to a training task at runtime via SQL.

## OpenAPI as the contract with the agent

One tricky part of templating was that the ML API accepts complex parameters, and somehow the agent needs to understand all of them. Fortunately, our project managed ML endpoint parameters with OpenAPI, so we could hand the full spec to the agent.

Our project uses [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) to generate model.py from the OpenAPI spec for parameter validation at runtime. Giving the machine-readable openapi.yml to the agent and having it translated into a markdown document within the skill turned out to work great. Long live standard formats.

## Skill-creator agent vs. skill-user agent

While building the skills, I asked Claude how best to test them. Its suggestion: spin up a separate agent process to exercise the skills through trial and error. I tried it, and it was an excellent experience.

When you're using the skill-user agent, you're not reading the OpenAPI spec or skill documentation yourself. Instead, you start thinking in terms of what you want to try: "I want to run this algorithm with this parameter combination." Normally, when doing manual sanity checks, the spec is already in your head, and you tend to skip the tedious, complex parameter combinations. But when an agent can do it for you, you get greedy.

The skill-user agent came back and told me: "I looked at the skill, but that parameter combination isn't supported in the OpenAPI spec yet." I had assumed our QA end-to-end tests would have caught this, but it was a close call. Because the OpenAPI spec was maintained manually, the Python code internally supported the combination, but the spec was missing the parameter, so requests couldn't pass through.

I fixed the bug quickly, deployed to the development environment, and updated the skill. Claude then picked up the new parameter combination and used it as if it had always been there. Impressive.

Building the skill alongside the product taught me that having a live execution environment pays for itself many times over.

## Wrapping up

By sharing these skills on the internal marketplace, the workflow creation step that used to require paid PS engagements was simplified, and even customers without PS contracts could benefit.

Treasure Studio also helped here: ML prediction results can now be visualized directly, making it easy to run analysis and model improvement cycles. Turning those analysis patterns into skills too seems like a natural next step, but that's out of scope for this post.

When I was drafting this post, I bounced ideas off Claude, and it argued that "the LLM's strengths are understanding problem structure and parameter inference." Providing an end-to-end CLI to support that lets agents run the generate-execute-fix loop autonomously. And by templating the complex parts of that loop, you create a clean division of labor: domain experts build the templates, and agents (used by people without that domain knowledge) fill in the parameters.
