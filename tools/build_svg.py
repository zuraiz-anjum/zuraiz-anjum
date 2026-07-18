"""
Assembles dark.svg / light.svg from portrait_tspan.txt + the bio/stats layout.
Re-run this any time the portrait changes; update.py only touches the
id-tagged <tspan> values (stats) after this has been generated.
"""
from pathlib import Path

PORTRAIT_TSPANS = Path("portrait_tspan.txt").read_text(encoding="utf-8")

THEMES = {
    "dark.svg": dict(
        bg="#05070A",
        ascii_fill="#67E8F9",
        key="#C4B5FD",
        value="#E5E7EB",
        cc="#4B5563",
        header="#F472B6",
        prompt="#67E8F9",
        add="#4ADE80",
        deL="#F87171",
    ),
    "light.svg": dict(
        bg="#F8FAFC",
        ascii_fill="#0891B2",
        key="#7C3AED",
        value="#1F2937",
        cc="#94A3B8",
        header="#DB2777",
        prompt="#0891B2",
        add="#16A34A",
        deL="#DC2626",
    ),
}

TEMPLATE = """<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="1180" height="560" viewBox="0 0 1180 560" fontsize="15px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key      {{ fill: {key}; }}
.value    {{ fill: {value}; }}
.cc       {{ fill: {cc}; }}
.addColor {{ fill: {add}; }}
.delColor {{ fill: {deL}; }}
text, tspan {{white-space: pre;}}
</style>
<rect width="1180px" height="560px" fill="{bg}" rx="15"/>
<g transform="translate(22,30) scale(0.42,0.88)">
<text x="0" y="0" fill="{ascii_fill}" class="ascii">
{portrait}
</text>
</g>
<text x="500" y="30" fill="{value}">
<tspan x="520" y="30" fill="{prompt}" fontsize="17px">zuraiz@neural-core</tspan> -————————————————————————————————————————————————————-—-
<tspan x="520" y="50" class="cc">. </tspan><tspan class="key">Subject</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">Zuraiz Anjum</tspan>
<tspan x="520" y="70" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">AI Engineer | Data Scientist</tspan>
<tspan x="520" y="90" class="cc">. </tspan><tspan class="key">Origin</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Lahore, Pakistan</tspan>
<tspan x="520" y="110" class="cc">. </tspan><tspan class="key">Status</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">Fine-tuning • Shipping • Building Agents</tspan>
<tspan x="520" y="130" class="cc">. </tspan><tspan class="key">ToolChain</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">VS Code, Git, Docker, Postman, Railway</tspan>
<tspan x="520" y="150" class="cc">. </tspan>
<tspan x="520" y="170" class="cc">. </tspan><tspan class="key">Neural</tspan>.<tspan class="key">Core</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Python, TypeScript, C++, C#, SQL</tspan>
<tspan x="520" y="190" class="cc">. </tspan><tspan class="key">Neural</tspan>.<tspan class="key">AI</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">LangChain, LangGraph, RAG, PyTorch, Transformers</tspan>
<tspan x="520" y="210" class="cc">. </tspan><tspan class="key">Neural</tspan>.<tspan class="key">Backend</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">FastAPI, Node.js, PostgreSQL, MySQL</tspan>
<tspan x="520" y="230" class="cc">. </tspan><tspan class="key">Neural</tspan>.<tspan class="key">Frontend</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">React, Next.js, Tailwind CSS</tspan>
<tspan x="520" y="250" class="cc">. </tspan><tspan class="key">Neural</tspan>.<tspan class="key">Stack</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">Agentic AI, Multi-Agent Orchestration, Fine-tuning</tspan>
<tspan x="520" y="270" class="cc">. </tspan>
<tspan x="520" y="290" fill="{header}">- Contact</tspan> -—————————————————————————————————————————————————————-—-
<tspan x="520" y="310" class="cc">. </tspan><tspan class="key">Grid</tspan>.<tspan class="key">Mail</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">zuraizwork@gmail.com</tspan>
<tspan x="520" y="330" class="cc">. </tspan><tspan class="key">Grid</tspan>.<tspan class="key">Github</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">zuraiz-anjum</tspan>
<tspan x="520" y="350" class="cc">. </tspan><tspan class="key">Grid</tspan>.<tspan class="key">Focus</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">LLM Systems, Agentic Pipelines, Full-Stack AI</tspan>
<tspan x="520" y="370" class="cc">. </tspan><tspan class="key">Grid</tspan>.<tspan class="key">Education</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">BS Data Science, FAST-NUCES</tspan>
<tspan x="520" y="410" fill="{header}">- GitHub Stats</tspan> -———————————————————————————————————————————————-—-
<tspan x="520" y="430" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">0</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">0</tspan>   }}  | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ............ </tspan><tspan class="value" id="star_data">0</tspan>
<tspan x="520" y="450" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> .................... </tspan><tspan class="value" id="commit_data">0</tspan>       | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ........ </tspan><tspan class="value" id="follower_data">0</tspan>
<tspan x="520" y="470" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">. </tspan><tspan class="value" id="loc_data">0</tspan> ( <tspan class="addColor" id="loc_add">0</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots">. </tspan><tspan class="delColor" id="loc_del">0</tspan><tspan class="delColor">--</tspan> )
</text>
</svg>
"""

for filename, theme in THEMES.items():
    svg = TEMPLATE.format(portrait=PORTRAIT_TSPANS, **theme)
    Path(filename).write_text(svg, encoding="utf-8")
    print(f"Wrote {filename}")
