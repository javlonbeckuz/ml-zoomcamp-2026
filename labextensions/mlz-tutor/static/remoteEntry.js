// Floating "Ask tutor" chat for JupyterLab. Talks to POST <base_url>tutor/ask (tutor.py).
// ponytail: hand-written module-federation container (init/get) instead of a webpack build;
// it imports nothing from JupyterLab, so there are no shared modules to negotiate. If a plugin
// ever needs JupyterLab tokens, switch to the official extension template.
(function () {
  const CSS = `
#mlz-tutor-btn{position:fixed;right:20px;bottom:40px;z-index:10000;width:52px;height:52px;border-radius:50%;
  border:0;cursor:pointer;background:var(--jp-brand-color1,#1976d2);color:#fff;font:600 13px var(--jp-ui-font-family);
  box-shadow:0 4px 14px rgba(0,0,0,.25)}
#mlz-tutor-btn:hover{filter:brightness(1.1)}
#mlz-tutor{position:fixed;right:20px;bottom:104px;z-index:10000;width:380px;max-width:calc(100vw - 40px);
  height:520px;max-height:calc(100vh - 140px);display:none;flex-direction:column;border-radius:10px;overflow:hidden;
  background:var(--jp-layout-color1,#fff);color:var(--jp-ui-font-color1,#222);border:1px solid var(--jp-border-color1,#ccc);
  box-shadow:0 8px 30px rgba(0,0,0,.25);font:13px/1.5 var(--jp-ui-font-family)}
#mlz-tutor.open{display:flex}
#mlz-tutor header{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;
  border-bottom:1px solid var(--jp-border-color2,#e0e0e0);font-weight:600}
#mlz-tutor header button{background:none;border:0;color:var(--jp-ui-font-color2,#666);cursor:pointer;font:inherit;font-weight:400}
#mlz-tutor .log{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:10px}
#mlz-tutor .msg{padding:8px 10px;border-radius:8px;max-width:92%;overflow-wrap:anywhere}
#mlz-tutor .me{align-self:flex-end;background:var(--jp-brand-color1,#1976d2);color:#fff;white-space:pre-wrap}
#mlz-tutor .bot{align-self:flex-start;background:var(--jp-layout-color2,#f2f2f2)}
#mlz-tutor .bot p{margin:0 0 6px}
#mlz-tutor .bot pre{background:var(--jp-layout-color3,#e4e4e4);padding:8px;border-radius:6px;overflow-x:auto;margin:6px 0}
#mlz-tutor .bot a{color:var(--jp-content-link-color,#1976d2)}
#mlz-tutor code{font-family:var(--jp-code-font-family);font-size:12px}
#mlz-tutor .src{font-size:11px;color:var(--jp-ui-font-color2,#666);margin-top:6px}
#mlz-tutor form{display:flex;gap:6px;padding:10px;border-top:1px solid var(--jp-border-color2,#e0e0e0)}
#mlz-tutor textarea{flex:1;resize:none;height:54px;padding:6px 8px;border-radius:6px;font:inherit;
  border:1px solid var(--jp-border-color1,#ccc);background:var(--jp-layout-color0,#fff);color:inherit}
#mlz-tutor form button{border:0;border-radius:6px;padding:0 14px;cursor:pointer;color:#fff;background:var(--jp-brand-color1,#1976d2)}
#mlz-tutor form button:disabled{opacity:.5;cursor:default}`;

  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  // Small markdown subset: code blocks, inline code, bold, headings, lists, paragraphs.
  function md(text) {
    const parts = text.split(/```[^\n]*\n?/);
    return parts.map((part, i) => {
      if (i % 2) return `<pre><code>${esc(part.replace(/\n$/, ''))}</code></pre>`;
      return esc(part).split(/\n{2,}/).map(block => {
        block = block.trim();
        if (!block) return '';
        block = block
          .replace(/`([^`\n]+)`/g, '<code>$1</code>')
          .replace(/\*\*([^*\n]+)\*\*/g, '<b>$1</b>')
          .replace(/^#{1,6} (.*)$/gm, '<b>$1</b>')
          .replace(/^\s*[-*] /gm, '• ')
          .replace(/\[([^\]\n]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
          .replace(/(?<!href=")(?<!">)(https?:\/\/[^\s<]+[^\s<.,;:)])/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
        return `<p>${block.replace(/\n/g, '<br>')}</p>`;
      }).join('');
    }).join('');
  }

  function config() {
    try { return JSON.parse(document.getElementById('jupyter-config-data').textContent); } catch (e) { return {}; }
  }

  async function post(question) {
    const cfg = config();
    const xsrf = (document.cookie.match(/(?:^|;\s*)_xsrf=([^;]+)/) || [])[1];
    const headers = { 'Content-Type': 'application/json' };
    if (cfg.token) headers.Authorization = `token ${cfg.token}`;
    if (xsrf) headers['X-XSRFToken'] = decodeURIComponent(xsrf);
    const r = await fetch(`${cfg.baseUrl || '/'}tutor/ask`, {
      method: 'POST', headers, credentials: 'same-origin', body: JSON.stringify({ question })
    });
    if (!r.ok) throw new Error(`HTTP ${r.status} (was Jupyter started from start.bat?)`);
    return r.json();
  }

  function mount() {
    const style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    const btn = document.createElement('button');
    btn.id = 'mlz-tutor-btn';
    btn.title = 'Ask the course tutor';
    btn.setAttribute('aria-label', 'Ask the course tutor');
    btn.textContent = 'Ask';

    const box = document.createElement('div');
    box.id = 'mlz-tutor';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Course tutor');
    box.innerHTML = `
      <header><span>Course tutor</span>
        <span><button type="button" data-act="reset">New chat</button>
        <button type="button" data-act="close" aria-label="Close">✕</button></span></header>
      <div class="log" aria-live="polite"></div>
      <form><textarea placeholder="Ask about the course… (Enter to send, Shift+Enter for new line)"></textarea>
        <button type="submit">Send</button></form>`;
    document.body.append(btn, box);

    const log = box.querySelector('.log');
    const input = box.querySelector('textarea');
    const send = box.querySelector('form button');

    function add(cls, html) {
      const div = document.createElement('div');
      div.className = `msg ${cls}`;
      div.innerHTML = html;
      log.appendChild(div);
      log.scrollTop = log.scrollHeight;
      return div;
    }
    const hello = () => add('bot', md('Hi! Ask me anything about ML Zoomcamp. I answer from the course notes and give hints, not homework solutions.'));
    hello();

    const toggle = open => {
      box.classList.toggle('open', open);
      if (open) input.focus();
    };
    btn.addEventListener('click', () => toggle(!box.classList.contains('open')));
    box.querySelector('[data-act=close]').addEventListener('click', () => toggle(false));
    box.querySelector('[data-act=reset]').addEventListener('click', async () => {
      log.innerHTML = '';
      hello();
      try { await post('reset'); } catch (e) { /* history is server-side; nothing to clear if it is down */ }
    });
    // keep JupyterLab shortcuts (e.g. A/B/DD in a notebook) from firing while typing here
    box.addEventListener('keydown', e => e.stopPropagation());

    input.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); box.querySelector('form').requestSubmit(); }
      if (e.key === 'Escape') toggle(false);
    });
    box.querySelector('form').addEventListener('submit', async e => {
      e.preventDefault();
      const q = input.value.trim();
      if (!q || send.disabled) return;
      input.value = '';
      add('me', esc(q));
      const pending = add('bot', '<i>Thinking…</i>');
      send.disabled = true;
      try {
        const { answer, sources } = await post(q);
        pending.innerHTML = md(answer) +
          (sources.length ? `<div class="src">Sources: ${sources.map(esc).join(', ')}</div>` : '');
      } catch (err) {
        pending.innerHTML = `<p>Error: ${esc(err.message)}</p>`;
      }
      send.disabled = false;
      log.scrollTop = log.scrollHeight;
    });
  }

  const plugin = {
    id: 'mlz-tutor:plugin',
    description: 'Floating course tutor chat button.',
    autoStart: true,
    activate: app => { app.restored.then(mount); }
  };

  window._JUPYTERLAB = window._JUPYTERLAB || {};
  window._JUPYTERLAB['mlz-tutor'] = {
    init: () => Promise.resolve(),
    get: () => Promise.resolve(() => ({ __esModule: true, default: plugin }))
  };
})();
