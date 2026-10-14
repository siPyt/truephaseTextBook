# -*- coding: utf-8 -*-
import os, sys, zlib, base64, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGS = ROOT / "figures"
FIGS.mkdir(exist_ok=True)

# 1. Patch engine.py (Fixes Windows fonts, subscripts, equation formatting, and running headers)
eng = (ROOT / "engine.py").read_text(encoding="utf-8")

# Add Windows font fallbacks & fix slashed zero in Mono
eng = eng.replace(
    "'Disp': [", "'Disp': ['C:/Windows/Fonts/arialbd.ttf','C:/Windows/Fonts/segoeuib.ttf',"
).replace(
    "'Body': [", "'Body': ['C:/Windows/Fonts/georgia.ttf','C:/Windows/Fonts/times.ttf',"
).replace(
    "'BodyB':[", "'BodyB':['C:/Windows/Fonts/georgiab.ttf','C:/Windows/Fonts/timesbd.ttf',"
).replace(
    "'BodyI':[", "'BodyI':['C:/Windows/Fonts/georgiai.ttf','C:/Windows/Fonts/timesi.ttf',"
).replace(
    "'Util': [", "'Util': ['C:/Windows/Fonts/segoeui.ttf','C:/Windows/Fonts/arial.ttf',"
).replace(
    "'UtilB':[", "'UtilB':['C:/Windows/Fonts/segoeuib.ttf','C:/Windows/Fonts/arialbd.ttf',"
).replace(
    "'Mono': ['/usr/share/fonts/truetype/custom/JetBrainsMono[wght].ttf',",
    "'Mono': ['C:/Windows/Fonts/consola.ttf','C:/Windows/Fonts/cour.ttf',"
).replace(
    "'MonoB':[", "'MonoB':['C:/Windows/Fonts/consolab.ttf','C:/Windows/Fonts/courbd.ttf',"
)

# Add SUBMAP so subscripts (R1, R2, f0, etc.) never turn into boxes
OLD_SX = '''SUPMAP={"\\u2070":"0","\\u00b9":"1","\\u00b2":"2","\\u00b3":"3","\\u2074":"4","\\u2075":"5",
        "\\u2076":"6","\\u2077":"7","\\u2078":"8","\\u2079":"9","\\u207b":"-","\\u207a":"+"}
def sx(t):
    """Convert unicode superscript runs to <super> markup (fonts lack those glyphs)."""
    if not isinstance(t,str): return t
    out=[]; i=0
    while i<len(t):
        if t[i] in SUPMAP:
            j=i; run=""
            while j<len(t) and t[j] in SUPMAP: run+=SUPMAP[t[j]]; j+=1
            out.append("<super>%s</super>"%run); i=j
        else:
            out.append(t[i]); i+=1
    return "".join(out)'''

NEW_SX = '''SUPMAP={"\\u2070":"0","\\u00b9":"1","\\u00b2":"2","\\u00b3":"3","\\u2074":"4","\\u2075":"5",
        "\\u2076":"6","\\u2077":"7","\\u2078":"8","\\u2079":"9","\\u207b":"-","\\u207a":"+",
        "\\u207f":"n"}
SUBMAP={"\\u2080":"0","\\u2081":"1","\\u2082":"2","\\u2083":"3","\\u2084":"4","\\u2085":"5",
        "\\u2086":"6","\\u2087":"7","\\u2088":"8","\\u2089":"9","\\u208a":"+","\\u208b":"-",
        "\\u2090":"a","\\u2091":"e","\\u2092":"o","\\u2093":"x","\\u2095":"h","\\u2096":"k",
        "\\u2097":"l","\\u2098":"m","\\u2099":"n","\\u209a":"p","\\u209b":"s","\\u209c":"t",
        "\\u1d62":"i","\\u1d63":"r","\\u1d64":"u","\\u1d65":"v"}
def sx(t):
    if not isinstance(t,str): return t
    out=[]; i=0
    while i<len(t):
        if t[i] in SUPMAP:
            j=i; run=""
            while j<len(t) and t[j] in SUPMAP: run+=SUPMAP[t[j]]; j+=1
            out.append("<super>%s</super>"%run); i=j
        elif t[i] in SUBMAP:
            j=i; run=""
            while j<len(t) and t[j] in SUBMAP: run+=SUBMAP[t[j]]; j+=1
            out.append("<sub>%s</sub>"%run); i=j
        else:
            out.append(t[i]); i+=1
    return "".join(out)'''

if OLD_SX in eng:
    eng = eng.replace(OLD_SX, NEW_SX)

# Fix EQ() using Paragraph instead of XPreformatted so <sub>/<super> render properly
eng = eng.replace(
    "rows=[[XPreformatted(sx(x),st['eq'])] for x in lines]",
    "rows=[[Paragraph(sx(x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')).replace('  ','&nbsp;&nbsp;'),st['eq'])] for x in lines]"
)
eng = eng.replace("FIGSCALE=0.62", "FIGSCALE=0.82")

(ROOT / "engine.py").write_text(eng, encoding="utf-8")

# 2. Patch render.py (Fixes chapter opening header bug)
ren = (ROOT / "render.py").read_text(encoding="utf-8")
ren = ren.replace("o=[NextPageTemplate('open'),\n       Marker(", "o=[Marker(")
ren = ren.replace("out.append(PageBreak())", "out+=[NextPageTemplate('open'),PageBreak()]")
(ROOT / "render.py").write_text(ren, encoding="utf-8")

# 3. Patch lib.py (Fixes broken battery, resistor, capacitor, inductor, switch, and transformer pins)
for p in [ROOT / "lib.py", FIGS / "lib.py"]:
    if p.exists():
        lib_txt = p.read_text(encoding="utf-8")
        # Fix DC supply top gap
        lib_txt = lib_txt.replace(
            "self.wire((x,yy-step*0.75),(x,y+h))",
            "self.wire((x,y),(x,y+h))"
        )
        # Ensure continuous wire through resistor/fuse spans
        lib_txt = lib_txt.replace(
            "self.wire((x,y),(x+b,y)); self.wire((x+b+6,y),(x+span,y))",
            "self.wire((x,y),(x+span,y))"
        ).replace(
            "self.wire((x,y),(x,y+b)); self.wire((x,y+b+6),(x,y+span))",
            "self.wire((x,y),(x,y+span))"
        )
        # Fix switch terminal wire gaps
        lib_txt = lib_txt.replace(
            "self.wire((x,y),(x+0.15,y)); self.wire((x+span-0.15,y),(x+span,y))",
            "self.wire((x,y),(x+1.0,y)); self.wire((x+span-1.0,y),(x+span,y))"
        )
        p.write_text(lib_txt, encoding="utf-8")

# 4. Patch figs.py (Fixes disconnected series resistors/capacitors/inductors & title overlaps)
for p in [ROOT / "figs.py", FIGS / "figs.py"]:
    if p.exists():
        f_txt = p.read_text(encoding="utf-8")
        f_txt = f_txt.replace(
            'def _hd(d,y,s): d.text(0,y,s,size=7,color=ACC)',
            'def _hd(d,y,s): d.text(0,max(y+4,43),s,size=7,color=ACC)'
        )
        # Connect series gaps in c2_kvl, c3_series, c4_cseries, c5_rl, c7, c8
        f_txt = f_txt.replace(
            'd.resistor(22,32,ref="R1",val="100 "+OH); d.resistor(40,32,ref="R2",val="220 "+OH)',
            'd.resistor(22,32,ref="R1",val="100 "+OH); d.wire((32,32),(40,32)); d.resistor(40,32,ref="R2",val="220 "+OH)'
        ).replace(
            'd.resistor(64,20,ref="R3",val="180 "+OH,span=10,vert=True)',
            'd.wire((64,32),(64,30)); d.resistor(64,20,ref="R3",val="180 "+OH,span=10,vert=True)'
        ).replace(
            'd.resistor(18,28,ref="R1",val="100 "+OH); d.resistor(32,28,ref="R2",val="220 "+OH)\n    d.resistor(46,28,ref="R3",val="330 "+OH)',
            'd.resistor(18,28,ref="R1",val="100 "+OH); d.wire((28,28),(32,28)); d.resistor(32,28,ref="R2",val="220 "+OH); d.wire((42,28),(46,28)); d.resistor(46,28,ref="R3",val="330 "+OH)'
        ).replace(
            'd.capacitor(16,28,ref="C1",val="10 "+MU+"F")\n    d.capacitor(30,28,ref="C2",val="10 "+MU+"F")',
            'd.capacitor(16,28,ref="C1",val="10 "+MU+"F"); d.wire((26,28),(30,28)); d.capacitor(30,28,ref="C2",val="10 "+MU+"F")'
        ).replace(
            'd.wire((64,36.4),(74,36.4)', 'd.wire((60,36.4),(74,36.4)'
        ).replace(
            'd.wire((66,34),(76,34)', 'd.wire((62,34),(76,34)'
        ).replace(
            'd.wire((58,34),(66,34))', 'd.wire((54,34),(66,34))'
        ).replace(
            'd.wire((64,32.4),(74,32.4)', 'd.wire((60,32.4),(74,32.4)'
        )
        p.write_text(f_txt, encoding="utf-8")

print("Patched successfully! Running build_all.py...")
subprocess.run([sys.executable, str(ROOT / "build_all.py")], check=True)
print("SUCCESS! Open TruePhase_Electrical_Theory_Textbook.pdf")