### It ran. That was never the question.

I build RL environments for AI agents and the graders that score them.
Most of my work is making sure a pass means the task was actually done.

**Available now** for contract or full-time work, remote (UTC+5). zuraizwork@gmail.com

A grader that a model can talk into a 1. A forecast that looks fine until the data shifts, or a research agent that answers confidently from the wrong source. None of these crash. They return a wrong answer that looks right, and someone ships it. That is the bug I go looking for.

<br>

**Environments**

Through October 2026 I built long-horizon environments for an AI training-data company. Each one gives an agent a real public dataset (energy registers, weather stations, mine safety filings, bike docks, exoplanet catalogs), a broken or unfinished pipeline, and a job that takes a hundred or so tool calls to finish properly. A verifier in a Docker sandbox scores the result against data the agent never sees.

The hard part is the grader. I attack my own verifiers before anyone else does: stale or planted reward files, processes left running after the episode, outputs that only look right on the visible split, answers that can be recalled instead of worked out. Then I read the agent trajectories to see why attempts passed or failed, and change the task until a pass means what it should. The client's code stays private. The method is public in grader-redteam below.

<br>

**Think you can fool a grader?**

I keep a hardened grader for a deliberately tiny task. Get it to award a 1 without solving the task and I'll list your exploit and fix the grader. [Rules](https://github.com/zuraiz-anjum/grader-redteam/blob/main/challenge/CHALLENGE.md) · [submit an exploit](https://github.com/zuraiz-anjum/grader-redteam/issues/new?template=exploit.yml)

[![challenge](https://github.com/zuraiz-anjum/grader-redteam/actions/workflows/challenge.yml/badge.svg)](https://github.com/zuraiz-anjum/grader-redteam/actions/workflows/challenge.yml)

<br>

**Things I've built**

| | |
|:--|:--|
| [**grader-redteam**](https://github.com/zuraiz-anjum/grader-redteam) | Throws a battery of cheats at any grader and reports which ones get through. A naive grader misses 8 of 11 checks; a hardened one misses none. Write-up: [how models cheat graders](https://github.com/zuraiz-anjum/grader-redteam/blob/main/docs/how-models-cheat-graders.md). |
| [**ARES**](https://github.com/zuraiz-anjum/ares-research) | A 27-node LangGraph system with 14 research modes that turns a question into a cited report. A fact checker and a critic send weak drafts back. RAG over ChromaDB, failover across four LLM providers, 123 tests. |
| [**pearls-aqi**](https://github.com/zuraiz-anjum/pearls-aqi) | Three-day air quality forecast for Lahore that retrains and republishes itself on GitHub Actions. Next-day RMSE 13.1, 42% better than persistence on embargoed out-of-fold data. [Live page](https://zuraiz-anjum.github.io/pearls-aqi/). |
| [**pk-wiki-integrity-lakehouse**](https://github.com/zuraiz-anjum/pk-wiki-integrity-lakehouse) | Spark and Delta pipeline tracking edits and reverts on the Urdu, Punjabi, Sindhi and Pashto Wikipedias. Idempotent MERGE writes, schema drift quarantine, audit tables. |

**Fixes upstream**

| project | what was wrong | status |
|:--|:--|:--|
| [LiteLLM #44230](https://github.com/BerriAI/litellm/pull/44230) | Streams where the provider sent no usage were logged at 0 tokens and $0, so spend tracking undercounted that traffic. A regression from [#42323](https://github.com/BerriAI/litellm/pull/42323). | merged |
| [rLLM #792](https://github.com/rllm-org/rllm/pull/792) | Prebuilt task images re-ran their Dockerfile steps on top of an image that already had them baked in. | open |
| Gymnasium | `generate_random_map` hangs for a 1x1 map or `p=0` instead of raising an error. | fix tested, not yet filed |
| TorchRL | The Countdown reward parser accepts `**`, `//` and decimals, and a nested power can hang it. | fix tested, not yet filed |
| MLflow | The RAGAS tool-call metrics drop tool calls that take no arguments, so a correct agent can score 0.0. | fix tested, not yet filed |
| Opik | `evaluate_on_dict_items` raises a TypeError when an item has an `id`. | fix tested, not yet filed |
| inspect_ai | `multiple_choice(template=...)` always errors when given a file path. | fix tested, not yet filed |
| SGLang | The MiniMax-M3 streaming tool parser breaks on nested closing tags. | fix tested, not yet filed |

**What I ship with**

Python, TypeScript, Docker, PyTorch, LangGraph, FastAPI, PostgreSQL, Spark, GitHub Actions.

<br>

[portfolio](https://zuraiz-portfolio.vercel.app) · zuraizwork@gmail.com

<sub>If you're building environments or evals and need someone to break the grader before the model does, I'd like to hear about it.</sub>
