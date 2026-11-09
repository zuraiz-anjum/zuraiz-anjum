"""Rebuild the upstream pull request block in README.md from the GitHub search API.

Runs daily in GitHub Actions (GITHUB_TOKEN) or locally (GH_TOKEN). Standard library only.
Everything between the UPSTREAM:START and UPSTREAM:END markers is replaced.
"""
import collections
import json
import os
import pathlib
import urllib.parse
import urllib.request

USER = "zuraiz-anjum"
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- UPSTREAM:START -->", "<!-- UPSTREAM:END -->"


def search(q):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    items, page = [], 1
    while True:
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": q, "per_page": 100, "page": page})
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": USER})
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=30) as r:
            batch = json.load(r)["items"]
        items += batch
        if len(batch) < 100:
            return items
        page += 1


def repo_of(item):
    return item["repository_url"].split("/repos/", 1)[1]


def grouped(items):
    by = collections.defaultdict(list)
    for it in items:
        by[repo_of(it)].append(it)
    return sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))


def lines(items, newest_first=True):
    out = []
    for repo, prs in grouped(items):
        out.append(f"**{repo}**\n")
        for pr in sorted(prs, key=lambda p: p["number"], reverse=newest_first):
            title = pr["title"].replace("|", "/").strip()
            out.append(f"- [#{pr['number']}]({pr['html_url']}) {title}")
        out.append("")
    return out


def main():
    base = f"author:{USER} type:pr -user:{USER}"
    merged = search(base + " is:merged")
    open_ = search(base + " is:open")
    m_repos, o_repos = len({repo_of(p) for p in merged}), len({repo_of(p) for p in open_})
    block = [START,
             f"Merged upstream: **{len(merged)}** across **{m_repos}** {'project' if m_repos == 1 else 'projects'}. "
             f"In review: **{len(open_)}** across **{o_repos}** projects. Open ones are proposals until a maintainer merges them.",
             "",
             "<details>",
             "<summary>Every upstream pull request, merged and open</summary>",
             "",
             "#### Merged",
             ""] + lines(merged) + ["#### In review", ""] + lines(open_) + [
             "<sub>Updated daily from the GitHub search API by <code>scripts/upstream.py</code>.</sub>",
             "",
             "</details>",
             END]
    text = README.read_text(encoding="utf-8")
    a, b = text.index(START), text.index(END) + len(END)
    new = text[:a] + "\n".join(block) + text[b:]
    if new != text:
        README.write_text(new, encoding="utf-8", newline="\n")
        print(f"updated: {len(merged)} merged, {len(open_)} open")
    else:
        print("no change")


if __name__ == "__main__":
    main()
