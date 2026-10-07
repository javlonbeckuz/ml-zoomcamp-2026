"""Course tutor for Jupyter: `%ask <question>` or `%%ask` answers from the course notes.

Retrieval is TF-IDF over the course .md files; the answer comes from Qwen
(OpenAI-compatible API). Settings live in .env: QWEN_API_KEY, QWEN_BASE_URL, QWEN_MODEL.
"""
import os
import re
from pathlib import Path

import requests
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).parent
COURSE = ROOT.parent / "course"
TOP_K = 5

SYSTEM = """You are a tutor for ML Zoomcamp 2026. The student is learning ML themself.
- Answer from the course excerpts below. Cite the lesson/file you used, e.g. (02-regression/07-linear-regression-training.md).
- You know the full video list (below the rules) and get detailed lesson notes as excerpts with each question.
  The notes are written versions of the videos, so treat them as the video content.
- "Exercise" in the video list is the student's own task for that lesson (from INSTRUCTION.md, their study guide).
  When asked what to do for a lesson, give that exercise. You may explain it and hint, but don't solve it for them.
- The student can't see the notes you are given; call them "the course notes", never "the excerpts you provided".
- When you point to a lesson, give its number and video link, e.g. "Lesson 2.9 (video: <link>)".
- If the excerpts don't cover it, say so, then answer briefly from general knowledge.
- Never write full homework solutions. Give hints, explain concepts, point to the relevant lesson.
- For errors: explain the cause first and let the student fix it. Show the fix only if asked twice.
- Reply in the language of the question. Code and code comments in English.
- Connect ideas to econometrics (OLS, logit, inference vs prediction) when useful.
- pandas 3 uses Copy-on-Write: df['col'] = df['col'].fillna(x), not inplace=True."""

_index = None
_history = []


def _env():
    path = ROOT / ".env"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            key, sep, value = line.partition("=")
            if sep and not line.lstrip().startswith("#"):
                os.environ.setdefault(key.strip(), value.strip())


def _indexable(p):
    rel = p.relative_to(COURSE).parts
    if any(part.startswith(".") for part in rel) or "solution" in p.name.lower():
        return False
    # old cohorts carry past homework answers; keep only this year's
    return rel[0] != "cohorts" or rel[1] == "2026"


def _lesson(rel):
    """'02-regression/04-validation-framework.md' -> '2.4'; None for non-lesson files."""
    m = re.fullmatch(r"(\d\d)-[^/]+/(\d\d)-[^/]+\.md", rel)
    return f"{int(m[1])}.{int(m[2])}" if m else None


def _notes():
    """(rel, lesson, title, video_url, body) for every indexable course .md file."""
    for p in sorted(COURSE.rglob("*.md")):
        if not _indexable(p):
            continue
        rel = p.relative_to(COURSE).as_posix()
        text = p.read_text(encoding="utf-8", errors="ignore")
        # lesson notes start with YAML front matter holding video_url
        video = re.search(r'^video_url:\s*"?([^"\n]+)', text, re.M)
        if text.startswith("---"):
            text = text.split("\n---", 1)[-1]
        title = re.search(r"^# (.+)", text, re.M)
        yield rel, _lesson(rel), title[1].strip() if title else "", video[1].strip() if video else None, text


def _tasks():
    """Lesson -> 'what to do: task' from the tables in INSTRUCTION.md (the course notes have no exercises)."""
    path = ROOT / "INSTRUCTION.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return {m[1]: f"{m[2].strip()}: {m[3].strip()}"
            for m in re.finditer(r"^\| \[(\d+\.\d+) [^\]]*\]\([^)]*\) \|([^|]+)\|(.+)\|\s*$", text, re.M)}


def _catalog(notes):
    """Every video: number, title, link, the lesson's opening line and its exercise. Sent with every question."""
    lines, module, tasks = [], None, _tasks()
    for rel, lesson, title, video, body in notes:
        if not (lesson and video):
            continue
        folder = rel.split("/")[0]
        if folder != module:
            module = folder
            meta = re.search(r'^title:\s*"?([^"\n]+)', (COURSE / folder / "module.yaml").read_text(encoding="utf-8"), re.M) \
                if (COURSE / folder / "module.yaml").exists() else None
            lines.append(f"\nModule {int(folder[:2])} ({folder}): {meta[1] if meta else ''}")
        intro = next((para for para in re.split(r"\n\s*\n", body)
                      if para.strip() and not para.lstrip().startswith(("#", "!", "<", "```", "|"))), "")
        intro = " ".join(intro.split())
        line = f"- {lesson} {title} | {video} | {intro[:220] + ('…' if len(intro) > 220 else '')}"
        if lesson in tasks:
            line += f" | Exercise: {tasks[lesson]}"
        lines.append(line)
    return "\n".join(lines).strip()


def _chunks(notes):
    for rel, lesson, title, video, text in notes:
        # every chunk gets the lesson header, otherwise only the first section knows its video
        header = f"Lesson {lesson}: {title}\n" if lesson else ""
        if video:
            header += f"Video: {video}\n"
        # one chunk per heading section, long sections cut at ~2000 chars
        for section in re.split(r"\n(?=#{1,3} )", text):
            for i in range(0, len(section), 2000):
                piece = section[i:i + 2000].strip()
                if len(piece) > 80:
                    yield rel, lesson, header + piece


def _build():
    global _index
    notes = list(_notes())
    guide = ROOT / "INSTRUCTION.md"  # study workflow, homework submission, deadlines
    if guide.exists():
        notes.append(("INSTRUCTION.md", None, "", None, guide.read_text(encoding="utf-8")))
    docs = list(_chunks(notes))
    vec = TfidfVectorizer(stop_words="english", sublinear_tf=True)
    _index = (docs, vec, vec.fit_transform(text for _, _, text in docs), _catalog(notes))


def search(question, k=TOP_K):
    if _index is None:
        _build()
    docs, vec, matrix, _ = _index
    # "2.4" is invisible to TF-IDF (tokens need 2+ word chars), so lesson numbers are looked up directly
    wanted = {f"{int(a)}.{int(b)}" for a, b in re.findall(r"\b(\d{1,2})\.(\d{1,2})\b", question)}
    hits = [next(i for i, d in enumerate(docs) if d[1] == w) for w in sorted(wanted) if any(d[1] == w for d in docs)]
    scores = (matrix @ vec.transform([question]).T).toarray().ravel()
    hits += [i for i in scores.argsort()[::-1][:k] if scores[i] > 0 and i not in hits]
    return [(docs[i][0], docs[i][2]) for i in hits[:k + len(wanted)]]


def ask(question):
    _env()
    hits = search(question)
    context = "\n\n".join(f"[{src}]\n{text}" for src, text in hits) or "(no matching course notes)"
    catalog = _index[3]
    messages = [{"role": "system", "content": f"{SYSTEM}\n\nAll course videos (number | title | link | what it covers):\n{catalog}"},
                *_history[-6:],
                {"role": "user", "content": f"Course excerpts:\n{context}\n\nQuestion: {question}"}]
    r = requests.post(
        os.environ.get("QWEN_BASE_URL", "https://dashscope-intl.aliyuncs.com/compatible-mode/v1") + "/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['QWEN_API_KEY']}"},
        json={"model": os.environ.get("QWEN_MODEL", "qwen3.8-max"), "messages": messages},
        timeout=120,
    )
    r.raise_for_status()
    answer = r.json()["choices"][0]["message"]["content"]
    # history keeps the bare question, not the excerpts, so it stays small
    _history.extend([{"role": "user", "content": question}, {"role": "assistant", "content": answer}])
    sources = sorted({src for src, _ in hits})
    return answer, sources


def _jupyter_server_extension_points():
    return [{"module": "tutor"}]


def _load_jupyter_server_extension(serverapp):
    """POST <base_url>tutor/ask {"question": ...} for the chat button (labextensions/mlz-tutor)."""
    import asyncio
    import json

    from jupyter_server.base.handlers import APIHandler
    from jupyter_server.utils import url_path_join
    from tornado.web import authenticated

    class AskHandler(APIHandler):
        @authenticated
        async def post(self):
            question = (self.get_json_body() or {}).get("question", "").strip()
            if question in ("", "reset"):
                _history.clear()
                return self.finish(json.dumps({"answer": "Conversation cleared.", "sources": []}))
            try:
                answer, sources = await asyncio.to_thread(ask, question)
            except Exception as e:  # show the failure in the chat instead of a silent 500
                answer, sources = f"Tutor error: {e}", []
            self.finish(json.dumps({"answer": answer, "sources": sources}))

    route = url_path_join(serverapp.web_app.settings["base_url"], "tutor/ask")
    serverapp.web_app.add_handlers(".*$", [(route, AskHandler)])


def load_ipython_extension(ip):
    from IPython.display import Markdown, display

    def ask_magic(line, cell=None):
        question = (cell or line).strip()
        if question in ("", "reset"):
            _history.clear()
            print("Conversation cleared. Usage: %ask <question>  or  %%ask on the first line of a cell.")
            return
        answer, sources = ask(question)
        foot = "\n\n---\n*Sources: " + ", ".join(f"`{s}`" for s in sources) + "*" if sources else ""
        display(Markdown(answer + foot))

    def as_cell_magic(lines):
        # "%ask what is x?" would hit IPython's trailing-? help lookup; a %%ask body is left alone
        if lines and lines[0].startswith("%ask "):
            return ["%%ask\n", lines[0][5:], *lines[1:]]
        return lines

    ip.register_magic_function(ask_magic, "line_cell", "ask")
    ip.input_transformers_cleanup.append(as_cell_magic)


if __name__ == "__main__":
    hits = search("root mean squared error validation")
    assert hits and any("regression" in src for src, _ in hits), hits
    assert all(_indexable(COURSE / src) for src, _ in hits)
    src, text = search("give me the video for lesson 2.4")[0]
    assert src == "02-regression/04-validation-framework.md" and "Video: https://www.youtube.com/" in text, (src, text[:200])
    assert sum("Video: " in t for _, t in hits) == len(hits)  # every chunk of a lesson carries its video
    catalog = _index[3]
    assert "- 2.4 Setting up the validation framework | https://www.youtube.com/" in catalog, catalog[:500]
    assert "| Exercise: 💻 Write code: Type the lesson's NumPy code yourself" in catalog
    print(catalog.count("\n- ") + 1, "videos in catalog,", catalog.count("| Exercise:"), "with exercises,", len(catalog), "chars")
    print(len(_index[0]), "chunks indexed; top hit:", hits[0][0])
