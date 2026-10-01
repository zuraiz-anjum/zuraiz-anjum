# Hi, I'm Muhammad Zuraiz Anjum

### RL Engineer & AI Engineer

I'm an AI engineer from Lahore. Right now most of my time goes into reinforcement learning evaluation environments: the tasks, the verifiers that grade them, and the sandboxes they run in. Before that I worked on backend services and model evaluation, and I still build LLM systems, agents, and full-stack apps on the side. I don't trust a model until I've watched it fail, so I tend to write the tests first.

![Profile views](https://komarev.com/ghpvc/?username=zuraiz-anjum&color=blueviolet&style=flat) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/zuraiz-anjum-9aa191372) [![Portfolio](https://img.shields.io/badge/Portfolio-Visit-8A2BE2?style=flat&logo=vercel)](https://zuraiz-portfolio.vercel.app)

---

## Currently

- **AI Research Engineer (RL) @ Tensium (UK)**: designing the CPU and GPU ML engineering environments that frontier models are trained and evaluated on
- **Data Science Intern @ 10Pearls**: applied data science and AI work for enterprise clients
- **BS Data Science @ FAST-NUCES**, Lahore (2023 to 2027)

### Focus Areas

- RL evaluation environments and reward signals
- LLM and agentic systems (LangGraph, RAG, evaluation)
- Backend APIs and infrastructure (FastAPI, Node.js, PostgreSQL, Docker)
- Full-stack products with React and Next.js

---

## Open Source Contributions

I fix the things I run into while using a project, mostly in evaluation and sandbox tooling.

**Open**

- **[rLLM #791](https://github.com/rllm-org/rllm/pull/791)**: fix(eval): join Dockerfile `RUN` continuation lines with a space, so multi-line commands are not glued together when they are replayed.
- **[rLLM #792](https://github.com/rllm-org/rllm/pull/792)**: fix(sandbox): skip Dockerfile `RUN` replay for prebuilt task images, since those steps are already baked into the image.

---

## Projects

- **[fuel-route-planner-api](https://github.com/zuraiz-anjum/fuel-route-planner-api)**: Django REST API that plans the cheapest fuel stops for a US road trip from the route and fuel prices.
- **[pearls-aqi](https://github.com/zuraiz-anjum/pearls-aqi)**: three-day AQI forecast for Lahore on a serverless stack (Hopsworks, GitHub Actions, Flask/FastAPI, Streamlit).
- **ARES**: a 26-agent LangGraph research assistant over 14 workflows that turns a question into a cited report, with RAG on ChromaDB, provider failover, and 123 automated tests. [Live demo](https://web-production-41acc.up.railway.app)
- **AI Agent SaaS Platform**: AI agents that join live video calls, talk in real time, and return a summary and transcript (Next.js, TypeScript, Stream SDK, Stripe).
- **[RouteLog](https://github.com/zuraiz-anjum/RouteLog-HOS-Trip-Planner)**: HOS trip planner and ELD log generator for truck drivers, with a Django API and a React frontend. [Live](https://full-stack-assesment-smoky.vercel.app)

---

## Tech Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

**AI & ML**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

**Backend & Frontend**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

**Data & Infra**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## Experience

### AI Research Engineer (RL), Tensium (UK), Remote
Jul 2026 to Present
- Design and ship long-horizon **reinforcement learning environments** that frontier AI models are trained and evaluated on, across **CPU ML engineering** and **GPU ML engineering** tracks
- Own each environment end to end: the task, the real-world data behind it, the sandboxed service the model works against, and the grader that decides whether it truly solved the problem
- Calibrate difficulty against frontier models so every environment separates real engineering skill from shortcuts, and harden graders against exploits, leakage and reward hacking
- Turn evaluation traces into design decisions, iterating environments until they hold up to maintainer review

### Data Science Intern, 10Pearls
Jul 2026 to Present
- Applied data science and AI engagements for enterprise clients: data pipelines, model prototyping, and analysis

### Software Engineer, Mercor (Contract, Remote)
Nov 2025 to Jun 2026
- Worked with global AI labs on **model training and evaluation**, building the data and backend systems that sit behind production AI models
- Designed database schemas, REST APIs and backend services that integrate models into real ML applications
- Evaluated models for accuracy, performance and reliability, and turned the findings into concrete improvements

### AI/ML Intern, Project19 (Remote, US-based)
Jun 2025 to Aug 2025
- Fine-tuned and evaluated LLMs for applied use cases
- Built and tested agentic workflows that automate multi-step tasks

### Leadership
- **Event Coordinator, SOFTEC** (FAST-NUCES tech festival): executive committee, worked up from Deputy Decor & Logistics to Head of Logistics to Event Coordinator
- **Head of Management, NUCES Media Group**: the university's media wing, covering campus events and content
- **Aspire Leader**: nine-week leadership program

---

## Education

**BS Data Science**, FAST National University of Computer and Emerging Sciences, Lahore, Pakistan (2023 to 2027)

---

## GitHub Analytics

<div align="center">

<img height="170" src="https://github-stats-extended.vercel.app/api?username=zuraiz-anjum&show_icons=true&include_all_commits=true&hide_rank=true&hide=stars&theme=tokyonight&hide_border=true" alt="GitHub stats" />
<img height="170" src="https://github-stats-extended.vercel.app/api/top-langs/?username=zuraiz-anjum&layout=compact&hide=jupyter%20notebook,html&theme=tokyonight&hide_border=true" alt="Top languages" />

</div>

---

## Connect

- **Portfolio:** https://zuraiz-portfolio.vercel.app
- **LinkedIn:** https://www.linkedin.com/in/zuraiz-anjum-9aa191372
- **GitHub:** https://github.com/zuraiz-anjum
- **Email:** zuraizwork@gmail.com

Open to AI engineering roles and collaborations.
