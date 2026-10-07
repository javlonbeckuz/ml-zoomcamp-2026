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


def _chunks():
    for p in sorted(COURSE.rglob("*.md")):
        if not _indexable(p):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        # one chunk per heading section, long sections cut at ~2000 chars
        for section in re.split(r"\n(?=#{1,3} )", text):
            for i in range(0, len(section), 2000):
                piece = section[i:i + 2000].strip()
                if len(piece) > 80:
                    yield p.relative_to(COURSE).as_posix(), piece


def _build():
    global _index
    docs = list(_chunks())
    vec = TfidfVectorizer(stop_words="english", sublinear_tf=True)
    _index = (docs, vec, vec.fit_transform(text for _, text in docs))


def search(question, k=TOP_K):
    if _index is None:
        _build()
    docs, vec, matrix = _index
    scores = (matrix @ vec.transform([question]).T).toarray().ravel()
    return [docs[i] for i in scores.argsort()[::-1][:k] if scores[i] > 0]


def ask(question):
    _env()
    hits = search(question)
    context = "\n\n".join(f"[{src}]\n{text}" for src, text in hits) or "(no matching course notes)"
    messages = [{"role": "system", "content": SYSTEM}, *_history[-6:],
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
    print(len(_index[0]), "chunks indexed; top hit:", hits[0][0])
