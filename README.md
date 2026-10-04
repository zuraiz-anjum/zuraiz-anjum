### It ran. That was never the question.

I'm Zuraiz Anjum. I build AI systems end to end, and I spend most of my time on the part that quietly goes wrong.

A multi-agent pipeline that answers confidently from the wrong source. A forecast that looks great until the data shifts. A grader that a model can talk into a pass. None of these crash. They just return the wrong answer, and someone ships it. That is the bug I go looking for.

So I build the whole thing: the agents and retrieval in the middle, the backend under them, the interface on top, and the evaluation that tells me whether any of it is actually right. At Tensium I design the long-horizon environments frontier models are trained and judged in. Before that, at Mercor, I worked with AI labs on model training and evaluation and built the services behind production models.

<br>

**Think you can fool a grader?**

I keep a hardened grader for a deliberately tiny task. Get it to award a 1 without solving the task and I'll list your exploit and fix the grader. [Rules](https://github.com/zuraiz-anjum/grader-redteam/blob/main/challenge/CHALLENGE.md) · [submit an exploit](https://github.com/zuraiz-anjum/grader-redteam/issues/new?template=exploit.yml)

[![challenge](https://github.com/zuraiz-anjum/grader-redteam/actions/workflows/challenge.yml/badge.svg)](https://github.com/zuraiz-anjum/grader-redteam/actions/workflows/challenge.yml)

<br>

**Things I've built**

| | |
|:--|:--|
| [**grader-redteam**](https://github.com/zuraiz-anjum/grader-redteam) | Throws a battery of cheats at any grader and reports which ones get through. A naive grader misses 8 of 11 checks; a hardened one misses none. Write-up: [how models cheat graders](https://github.com/zuraiz-anjum/grader-redteam/blob/main/docs/how-models-cheat-graders.md). |
| [**ARES**](https://github.com/zuraiz-anjum/ares-research) | A 27-node LangGraph system across 14 research modes that turn a question into a cited research report. RAG over ChromaDB, provider failover, 123 automated tests. |
| [**RouteLog**](https://github.com/zuraiz-anjum/RouteLog-HOS-Trip-Planner) | Hours-of-service trip planner and ELD log generator for truck drivers. Django and React, with CI and 142 passing tests. |
| [**fuel-route-planner-api**](https://github.com/zuraiz-anjum/fuel-route-planner-api) | Cost-optimal fuel stops for any US road trip from a single routing call. |
| [**pearls-aqi**](https://github.com/zuraiz-anjum/pearls-aqi) | Three-day air quality forecast for Lahore on a fully serverless ML pipeline. |
| **Agent SaaS** | AI agents that join live video calls, hold a real-time conversation and hand back the summary. |

**Bugs I'm fixing upstream**

| project | what was wrong | status |
|:--|:--|:--|
| [LiteLLM #44201](https://github.com/BerriAI/litellm/pull/44201) | Updating a Lens finding with an id that doesn't exist returned 200 and changed nothing, so a typo looked like a successful update. | in review |
| [LiteLLM #44230](https://github.com/BerriAI/litellm/pull/44230) | Streams where the provider sent no usage were logged at 0 tokens and $0, so spend tracking undercounted that traffic. A regression from [#42323](https://github.com/BerriAI/litellm/pull/42323). | in review |
| [Strata #454](https://github.com/Niko1221/Strata/pull/454) | The local OpenAI and Anthropic API silently ignored `stop` and `stop_sequences`, so clients got text past their stop string. | in review |
| [Strata #455](https://github.com/Niko1221/Strata/pull/455) | The AMD setup menu didn't say the Unsloth models are NVIDIA only so far, and on a PC with both kinds of card it never pointed to the NVIDIA one. | in review |
| [rLLM #792](https://github.com/rllm-org/rllm/pull/792) | Prebuilt task images re-ran their Dockerfile steps on top of an image that already had them baked in. | in review |

**Now**

Shipping RL environments at Tensium · building tools that catch graders being fooled.

**What I ship with**

Python, TypeScript, PyTorch, LangGraph, FastAPI, Django, Next.js, PostgreSQL, Docker.

<br>

[portfolio](https://zuraiz-portfolio.vercel.app) · [linkedin](https://www.linkedin.com/in/zuraiz-anjum-9aa191372) · zuraizwork@gmail.com

<sub>Building something where wrong answers are expensive? I'd like to hear about it.</sub>
