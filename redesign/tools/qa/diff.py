"""Compare two snapshot folders pixel by pixel. Usage: python3 diff.py before after"""
import sys, pathlib
from PIL import Image, ImageChops
a, b = map(pathlib.Path, sys.argv[1:3]); bad = 0
for f in sorted(a.glob('*.png')):
    x, y = Image.open(f).convert('RGB'), Image.open(b / f.name).convert('RGB')
    if x.size != y.size: print('SIZE', f.name, x.size, y.size); bad += 1; continue
    box = ImageChops.difference(x, y).point(lambda v: 255 if v > 12 else 0).getbbox()
    if box: print('DIFF', f.name, box); bad += 1
print('identical' if not bad else f'{bad} differ')
