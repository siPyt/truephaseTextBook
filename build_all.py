import sys; from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'figures'))
from engine import *
from render import render_chapter
import matter
mods=[]
for i in range(1,21):
    m=__import__('c%02d'%i); mods.append(getattr(m,'CH%d'%i))
story=[]
story+=matter.cover()
story+=matter.contents()
story+=matter.symbolkey()
for ch in mods: story+=render_chapter(ch)
story+=matter.backmatter()
OUT=str(__import__('pathlib').Path(__file__).resolve().parent / 'TruePhase_Electrical_Theory_Textbook.pdf')
doc=Book(OUT)
doc.multiBuild(flatten(story))
print('PAGES',doc.page)
