"""Remove CSS rules whose selectors only target classes that no page and no script uses.
Run after building: python3 redesign/tools/prune_css.py   (then rebuild, so the ?v= hash updates)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent / 'a-v3'
css_p = ROOT / 'assets' / 'site.css'; css = css_p.read_text()
used = set()
for f in ROOT.rglob('*.html'):
    for m in re.finditer(r'class="([^"]*)"', f.read_text()): used.update(m.group(1).split())
used.update(re.findall(r'[A-Za-z][\w-]*', (ROOT / 'assets' / 'site.js').read_text()))   # classes the script adds

def split_top(s, sep):
    out, depth, cur = [], 0, ''
    for ch in s:
        if ch in '([': depth += 1
        elif ch in ')]': depth -= 1
        if ch == sep and depth == 0: out.append(cur); cur = ''
        else: cur += ch
    return out + [cur]

def alive(sel):
    """True if the selector can match: every class it needs exists; inside :is()/:where() one alternative is enough;
    classes inside :not() are not required."""
    for fn in (':not(', ':is(', ':where('):
        i = sel.find(fn)
        if i != -1:
            depth, e = 1, i + len(fn)
            while depth: depth += (sel[e] == '(') - (sel[e] == ')'); e += 1
            inner, rest = sel[i + len(fn):e - 1], sel[:i] + '{}' + sel[e:]
            if fn == ':not(': return alive(rest.format(''))
            return any(alive(rest.format(alt.strip())) for alt in split_top(inner, ','))
    return all(c in used for c in re.findall(r'\.(-?[A-Za-z_][\w-]*)', re.sub(r'\[[^\]]*\]', '', sel)))

removed = []
def walk(text):
    out, i, n = '', 0, len(text)
    while i < n:
        j = text.find('{', i)
        if j == -1: out += text[i:]; break
        k = text.rfind('}', i, j); c = text.rfind('*/', i, j); start = max(k, c + 1) + 1 if max(k, c) >= i else i
        # prelude starts after the last closed block or comment
        m = max(text.rfind('}', i, j), text.rfind('*/', i, j) + 1 if text.rfind('*/', i, j) != -1 else -1, text.rfind(';', i, j))
        pre_start = m + 1 if m >= i else i
        head, prelude = text[i:pre_start], text[pre_start:j]
        depth, e = 1, j + 1
        while depth: 
            ch = text[e]; depth += (ch == '{') - (ch == '}'); e += 1
        body = text[j + 1:e - 1]; p = prelude.strip()
        if p.startswith(('@media', '@supports')):
            inner = walk(body)
            out += head + (prelude + '{' + inner + '}' if inner.strip() else '')
        elif p.startswith('@'):
            out += head + prelude + '{' + body + '}'
        else:
            keep = [s for s in split_top(prelude, ',') if alive(s)]
            if keep: out += head + (prelude if len(keep) == len(split_top(prelude, ',')) else '\n' + ','.join(k.strip() and ' ' + k.strip() for k in keep).strip() + ' ') + '{' + body + '}'
            else: out += head; removed.append(p[:70])
        i = e
    return out

new = walk(css)
new = re.sub(r'\n{3,}', '\n\n', new)
css_p.write_text(new)
print(f'{len(css)} -> {len(new)} bytes, {len(removed)} rules removed')
for r in removed[:400]: print('  -', r)
