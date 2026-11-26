"""Writes a topographic-lines SVG (the Vende Digital 2022 system's texture) as a crisp vector for the phones panel.
Deterministic: a smooth field from a few Gaussian hills, cut into contour lines."""
import numpy as np, contourpy, pathlib
W, H, step = 1600, 720, 8
rng = np.random.default_rng(2022)
xs, ys = np.meshgrid(np.arange(0, W + step, step), np.arange(0, H + step, step))
z = np.zeros_like(xs, dtype=float)
for _ in range(9):
    cx, cy = rng.uniform(-100, W + 100), rng.uniform(-100, H + 100)
    sx, sy = rng.uniform(160, 420), rng.uniform(120, 320)
    z += rng.uniform(0.6, 1.2) * np.exp(-(((xs - cx) / sx) ** 2 + ((ys - cy) / sy) ** 2))
gen = contourpy.contour_generator(xs, ys, z, line_type='Separate')
paths = []
for lv in np.linspace(z.min() + 0.08, z.max() - 0.02, 14):
    for line in gen.lines(lv):
        if len(line) < 8: continue
        pts = line[::2]
        d = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
        paths.append(f'<path d="{d}"/>')
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#e7b3e6" stroke-width="1.4" stroke-linejoin="round">{"".join(paths)}</g></svg>'
out = pathlib.Path(__file__).resolve().parent.parent / 'a-v3' / 'assets' / 'img' / 'vd-topo.svg'
out.write_text(svg)
print(out, len(svg) // 1024, 'KB', len(paths), 'lines')
