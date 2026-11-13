### It ran. That was never the question.

I build RL environments for AI agents and the graders that score them.
Most of my work is making sure a pass means the task was actually done.

**Available now** for contract or full-time work, remote (UTC+5). zuraizwork@gmail.com

A grader that a model can talk into a 1. A forecast that looks fine until the data shifts, or a research agent that answers confidently from the wrong source. None of these crash. They return a wrong answer that looks right, and someone ships it. That is the bug I go looking for.

<br>

**Environments**

Through July 2026 I built long-horizon environments for an AI training-data company. Each one gives an agent a real public dataset (energy registers, weather stations, mine safety filings, bike docks, exoplanet catalogs), a broken or unfinished pipeline, and a job that takes a hundred or so tool calls to finish properly. A verifier in a Docker sandbox scores the result against data the agent never sees.

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

**Bugs I caught upstream**

Most of these are graders or eval harnesses scoring something wrong, quietly. Merged so far:

| fix | what was wrong |
|:--|:--|
| [OpenEnv #1572](https://github.com/openenv/OpenEnv/pull/1572) | The Julia environment's safety filter matched `rm(` inside `norm(` and `transform(`, so ordinary numeric code got penalized as dangerous. It now matches whole calls only. |
| [OpenEnv #1570](https://github.com/openenv/OpenEnv/pull/1570) | A terminal-bench `reward.txt` holding `nan` or `inf` finished the episode as a success with no reward. Now it counts as no verdict, like an empty file. |
| [OpenEnv #1569](https://github.com/openenv/OpenEnv/pull/1569) | FinQA's percentage fallback never stripped labels like `2023:`, so a correct labelled answer scored 0. |
| [LiteLLM #44230](https://github.com/BerriAI/litellm/pull/44230) | Streams where the provider sent no usage were logged at 0 tokens and $0, so spend tracking undercounted that traffic. A regression from [#42323](https://github.com/BerriAI/litellm/pull/42323). |

<!-- UPSTREAM:START -->
Merged upstream: **5** across **2** projects. In review: **30** across **22** projects. Open ones are proposals until a maintainer merges them.

<details>
<summary>Every upstream pull request, merged and open</summary>

#### Merged

**openenv/OpenEnv**

- [#1580](https://github.com/openenv/OpenEnv/pull/1580) Run coding_tools_env verification outside the notebook kernel
- [#1572](https://github.com/openenv/OpenEnv/pull/1572) fix(julia_env): match dangerous calls on a word boundary
- [#1570](https://github.com/openenv/OpenEnv/pull/1570) fix(tbench2_env): treat a nan or inf reward.txt as no verdict
- [#1569](https://github.com/openenv/OpenEnv/pull/1569) fix(finqa_env): strip the year label before the percentage points fallback

**BerriAI/litellm**

- [#44230](https://github.com/BerriAI/litellm/pull/44230) fix(streaming): restore the token estimate for streams that send no usage

#### In review

**NVIDIA-NeMo/Gym**

- [#5803](https://github.com/NVIDIA-NeMo/Gym/pull/5803) fix(string_match): strip units only when no letter is attached
- [#5802](https://github.com/NVIDIA-NeMo/Gym/pull/5802) fix(generative_reward_model): treat NaN or infinite scores as a parse failure
- [#5761](https://github.com/NVIDIA-NeMo/Gym/pull/5761) fix(codex_agent): record the model's cmd for exec_command calls
- [#5760](https://github.com/NVIDIA-NeMo/Gym/pull/5760) fix(trajectory): export cached input tokens from the live transcript
- [#5733](https://github.com/NVIDIA-NeMo/Gym/pull/5733) feat(harbor): let a dataset name the reward.json key that is the score

**letta-ai/letta-evals**

- [#358](https://github.com/letta-ai/letta-evals/pull/358) fix(visualization): Count errors across all runs in the overall summary
- [#357](https://github.com/letta-ai/letta-evals/pull/357) fix(extractors): Make pattern group mean the same thing with search_all

**PrimeIntellect-ai/verifiers**

- [#3093](https://github.com/PrimeIntellect-ai/verifiers/pull/3093) docs: describe the artifact trust boundary and saved artifacts
- [#3092](https://github.com/PrimeIntellect-ai/verifiers/pull/3092) fix(judges): size prompt fences so a response can't close its block

**rllm-org/rllm**

- [#950](https://github.com/rllm-org/rllm/pull/950) fix(eval): do not read the next word as the MCQ answer letter
- [#792](https://github.com/rllm-org/rllm/pull/792) fix(sandbox): skip dockerfile RUN replay for prebuilt task images

**xlang-ai/OSWorld**

- [#687](https://github.com/xlang-ai/OSWorld/pull/687) fix(calc): read single absolute cells in conditional formatting formulas
- [#686](https://github.com/xlang-ai/OSWorld/pull/686) fix(gimp): only crop to visible content in check_image_size when ignore_transparent is set

**allenai/open-instruct**

- [#2212](https://github.com/allenai/open-instruct/pull/2212) Fix ReSearchVerifierF1 format check for responses with one finish tag

**BerriAI/litellm**

- [#50442](https://github.com/BerriAI/litellm/pull/50442) fix(cost): price a non-streamed reply without usage from counted tokens

**bespokelabsai/AutoResearchExam**

- [#24](https://github.com/bespokelabsai/AutoResearchExam/pull/24) FastAdv: normalize logit scale in both directions

**browser-use/rl-env-use**

- [#9](https://github.com/browser-use/rl-env-use/pull/9) grounded: count only the source's own repo on shared hosts, and skip pages that echo the answer from their URL

**collinear-ai/yc-bench**

- [#48](https://github.com/collinear-ai/yc-bench/pull/48) fix: start each episode with a fresh conversation in multi-episode runs

**comet-ml/opik**

- [#9503](https://github.com/comet-ml/opik/pull/9503) [issue-9502] [SDK] fix: keep an item's own id in evaluate_on_dict_items

**Farama-Foundation/Gymnasium**

- [#1837](https://github.com/Farama-Foundation/Gymnasium/pull/1837) Fix `generate_random_map` hanging for `size=1` or `p=0`

**harbor-framework/harbor**

- [#4160](https://github.com/harbor-framework/harbor/pull/4160) fix(rewardkit): score unreadable CSV and xlsx files instead of aborting

**JudgmentLabs/judgeval**

- [#837](https://github.com/JudgmentLabs/judgeval/pull/837) fix(evaluation): page through run results and match them to examples by id

**livekit/agents**

- [#8420](https://github.com/livekit/agents/pull/8420) fix(evals): count errored judges as not passed in JudgeGroup

**mlflow/mlflow**

- [#27541](https://github.com/mlflow/mlflow/pull/27541) Fix RAGAS `ToolCallAccuracy` and `ToolCallF1` ignoring tool calls with no arguments

**patronus-ai/speedrun_bench**

- [#11](https://github.com/patronus-ai/speedrun_bench/pull/11) Prefix the agent's output in the orchestrator log

**preferencemodel/karotte**

- [#141](https://github.com/preferencemodel/karotte/pull/141) Add final_answer_pattern so RegexJudge examples don't pass a list of guesses

**SalesforceAIResearch/CRMArena**

- [#32](https://github.com/SalesforceAIResearch/CRMArena/pull/32) fix(evaluator): import re for the judge reply fallback parser

**SapienzaNLP/ita-bench**

- [#2](https://github.com/SapienzaNLP/ita-bench/pull/2) fix(truthful_qa): score mc1 against the index of the true answer

**supermemoryai/memorybench**

- [#102](https://github.com/supermemoryai/memorybench/pull/102) fix(zep): judge Zep with the same prompts as every other provider

**thinking-machines-lab/tinker-cookbook**

- [#994](https://github.com/thinking-machines-lab/tinker-cookbook/pull/994) fix(eval): shuffle GPQA choices so the answer is not always A

<sub>Updated daily from the GitHub search API by <code>scripts/upstream.py</code>.</sub>

</details>
<!-- UPSTREAM:END -->

**What I ship with**

Python, TypeScript, Docker, PyTorch, LangGraph, FastAPI, PostgreSQL, Spark, GitHub Actions.

<br>

zuraizwork@gmail.com

<sub>If you're building environments or evals and need someone to break the grader before the model does, I'd like to hear about it.</sub>
