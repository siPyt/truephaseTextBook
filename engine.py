# -*- coding: utf-8 -*-
"""TruePhase textbook engine: Platypus layout, whitelist-only vector figures."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == 'figures' else Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures'))
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (XPreformatted, BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, Flowable, KeepTogether, NextPageTemplate, PageBreak)
import lib
from lib import D

import os
_CANDS={
 'Disp': ['C:/Windows/Fonts/arialbd.ttf','C:/Windows/Fonts/segoeuib.ttf','C:/Windows/Fonts/arialbd.ttf','C:/Windows/Fonts/segoeuib.ttf','/usr/share/fonts/truetype/custom/Oswald[wght].ttf',
          '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'],
 'Body': ['C:/Windows/Fonts/georgia.ttf','C:/Windows/Fonts/times.ttf','C:/Windows/Fonts/georgia.ttf','C:/Windows/Fonts/times.ttf','/usr/share/fonts/truetype/custom/SourceSerif4[opsz,wght].ttf',
          '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'],
 'BodyB':['C:/Windows/Fonts/georgiab.ttf','C:/Windows/Fonts/timesbd.ttf','C:/Windows/Fonts/georgiab.ttf','C:/Windows/Fonts/timesbd.ttf','/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'],
 'BodyI':['C:/Windows/Fonts/georgiai.ttf','C:/Windows/Fonts/timesi.ttf','C:/Windows/Fonts/georgiai.ttf','C:/Windows/Fonts/timesi.ttf','/usr/share/fonts/truetype/custom/SourceSerif4-Italic[opsz,wght].ttf',
          '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'],
 'Util': ['C:/Windows/Fonts/segoeui.ttf','C:/Windows/Fonts/arial.ttf','C:/Windows/Fonts/segoeui.ttf','C:/Windows/Fonts/arial.ttf','/usr/share/fonts/truetype/custom/DMSans[opsz,wght].ttf',
          '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'],
 'UtilB':['C:/Windows/Fonts/segoeuib.ttf','C:/Windows/Fonts/arialbd.ttf','C:/Windows/Fonts/segoeuib.ttf','C:/Windows/Fonts/arialbd.ttf','/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'],
 'Mono': ['C:/Windows/Fonts/consola.ttf','C:/Windows/Fonts/cour.ttf',
          '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
          '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'],
 'MonoB':['C:/Windows/Fonts/consolab.ttf','C:/Windows/Fonts/courbd.ttf','C:/Windows/Fonts/consolab.ttf','C:/Windows/Fonts/courbd.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
          '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'],
}
for _n,_c in _CANDS.items():
    for _f in _c:
        if os.path.exists(_f):
            pdfmetrics.registerFont(TTFont(_n,_f)); break
    else:
        raise SystemExit('no font for '+_n)
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Body',normal='Body',bold='BodyB',italic='BodyI',boldItalic='BodyI')
registerFontFamily('Util',normal='Util',bold='UtilB',italic='Util',boldItalic='UtilB')
registerFontFamily('Mono',normal='Mono',bold='MonoB',italic='Mono',boldItalic='MonoB')

INK   = HexColor('#15191D')
PAPER = HexColor('#FCFBF8')
RULE  = HexColor('#CFD3D6')
ACC   = HexColor('#A8272C')     # structural accent
MEAS  = HexColor('#1B6B70')     # measurement / instrument
GREY  = HexColor('#5B6368')
WASH  = HexColor('#F2F0EA')
WASH2 = HexColor('#E9EEEF')

PW,PH = letter
LM,RM,TM,BM = 1.0*inch, 0.85*inch, 1.0*inch, 0.85*inch
TW = PW-LM-RM

def S(name,**kw):
    base=dict(fontName='Body',fontSize=10.1,leading=14.6,textColor=INK,
              spaceAfter=6.2,alignment=TA_JUSTIFY)
    base.update(kw); return ParagraphStyle(name,**base)

st={
 'body': S('body'),
 'lead': S('lead',fontSize=11.6,leading=16.4,textColor=HexColor('#2C3338'),spaceAfter=10),
 'h1':   S('h1',fontName='Disp',fontSize=21,leading=24,spaceAfter=3,alignment=0),
 'h2':   S('h2',fontName='Disp',fontSize=13.2,leading=16,textColor=INK,spaceBefore=11,spaceAfter=4,alignment=0),
 'h3':   S('h3',fontName='Util',fontSize=8.6,leading=11,textColor=ACC,spaceBefore=8,spaceAfter=3,alignment=0),
 'eyebrow': S('eyebrow',fontName='Util',fontSize=7.2,leading=9,textColor=ACC,spaceAfter=3,alignment=0),
 'cap':  S('cap',fontName='Util',fontSize=7.4,leading=9.8,textColor=GREY,spaceAfter=0,alignment=0),
 'eq':   S('eq',fontName='Mono',fontSize=9.2,leading=13,textColor=INK,alignment=0,spaceAfter=3),
 'panel':S('panel',fontSize=9.6,leading=13.4,spaceAfter=3.4),
 'panelh':S('panelh',fontName='Util',fontSize=7.8,leading=10,textColor=MEAS,spaceAfter=4,alignment=0),
 'li':   S('li',fontSize=9.9,leading=13.6,spaceAfter=3.6,alignment=0),
 'tb':   S('tb',fontSize=8.8,leading=11.6,spaceAfter=0,alignment=0),
 'tbh':  S('tbh',fontName='Util',fontSize=7.6,leading=10,textColor=white,spaceAfter=0,alignment=0),
 'num':  S('num',fontName='Disp',fontSize=74,leading=66,textColor=ACC,alignment=0),
 'ctitle':S('ctitle',fontName='Disp',fontSize=30,leading=32,alignment=0,spaceAfter=4),
 'csub': S('csub',fontSize=12.4,leading=16.4,textColor=GREY,alignment=0,spaceAfter=8),
 'cover1':S('cover1',fontName='Disp',fontSize=54,leading=54,alignment=0),
 'tocl': S('tocl',fontName='Util',fontSize=9.2,leading=13.2,alignment=0,spaceAfter=0),
}


SUPMAP={"\u2070":"0","\u00b9":"1","\u00b2":"2","\u00b3":"3","\u2074":"4","\u2075":"5",
        "\u2076":"6","\u2077":"7","\u2078":"8","\u2079":"9","\u207b":"-","\u207a":"+",
        "\u207f":"n"}
SUBMAP={"\u2080":"0","\u2081":"1","\u2082":"2","\u2083":"3","\u2084":"4","\u2085":"5",
        "\u2086":"6","\u2087":"7","\u2088":"8","\u2089":"9","\u208a":"+","\u208b":"-",
        "\u2090":"a","\u2091":"e","\u2092":"o","\u2093":"x","\u2095":"h","\u2096":"k",
        "\u2097":"l","\u2098":"m","\u2099":"n","\u209a":"p","\u209b":"s","\u209c":"t",
        "\u1d62":"i","\u1d63":"r","\u1d64":"u","\u1d65":"v"}
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
    return "".join(out)

# ------------------------------------------------------------------ flowables
class Marker(Flowable):
    def __init__(self,key,text,lvl=0):
        self._bk=(key,text,lvl); self.width=0; self.height=0
    def wrap(self,aw,ah): return (0,0)
    def draw(self): pass

class Rule(Flowable):
    def __init__(self,color=ACC,h=1.2,w=None,pad=5):
        self.color=color; self.h=h; self.w=w; self.pad=pad
    def wrap(self,aw,ah):
        self.width=self.w or aw; self.height=self.h+self.pad; return (self.width,self.height)
    def draw(self):
        c=self.canv; c.setStrokeColor(self.color); c.setLineWidth(self.h)
        c.line(0,self.pad,self.width,self.pad)

class Fig(Flowable):
    """Whitelist vector figure. fn(d) draws in grid units, origin bottom-left."""
    def __init__(self,fn,caption,num,gw=82,gh=48,pad=10,fill=HexColor('#FFFFFF')):
        self.fn=fn; self.caption=caption; self.num=num
        self.gw=gw; self.gh=gh; self.pad=pad; self.fill=fill
    def wrap(self,aw,ah):
        self.width=aw
        self.s=(aw-2*self.pad)/float(self.gw*lib.U)
        self.dh=self.gh*lib.U*self.s+2*self.pad
        txt=('<font name="Mono" size="7" color="#A8272C">%s</font>&nbsp;&nbsp;%s'
             %(self.num,self.caption)) if self.num else self.caption
        self._cap=Paragraph(txt,st['cap'])
        self._ch=self._cap.wrap(aw,ah)[1]+4 if self.caption else 0
        self.height=self.dh+self._ch+5
        return (aw,self.height)
    def draw(self):
        c=self.canv; y0=self.height-self.dh
        c.setFillColor(self.fill); c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.rect(0,y0,self.width,self.dh,1,1)
        c.saveState()
        p=c.beginPath(); p.rect(0,y0,self.width,self.dh); c.clipPath(p,stroke=0,fill=0)
        c.translate(self.pad,y0+self.pad)
        self.fn(D(c,self.s))
        c.restoreState()
        if self.caption: self._cap.drawOn(c,0,0)

FIGSCALE=0.82
def fig(fn,caption,num,gh=48,gw=82):
    return Fig(fn,caption,num,gw=gw/FIGSCALE,gh=gh)

# ------------------------------------------------------------------ helpers
def H1(t): return Paragraph(sx(t),st['h1'])
def H2(t): return Paragraph(sx(t),st['h2'])
def H3(t): return Paragraph(sx(t),st['h3'])
def T(t):  return Paragraph(sx(t),st['body'])
def L(t):  return Paragraph(sx(t),st['lead'])
def EY(t): return Paragraph(t,st['eyebrow'])

def bullets(items,marker='\u2022',style='li'):
    rows=[[Paragraph('<font color="#A8272C">%s</font>'%marker,st[style]),
           Paragraph(sx(x),st[style])] for x in items]
    t=Table(rows,colWidths=[12,TW-12])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return t

def numbered(items):
    rows=[[Paragraph('<font name="Mono" size="8" color="#A8272C">%d</font>'%(i+1),st['li']),
           Paragraph(sx(x),st['li'])] for i,x in enumerate(items)]
    t=Table(rows,colWidths=[16,TW-16])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
    return t

def EQ(lines):
    rows=[[Paragraph(sx(x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')).replace('  ','&nbsp;&nbsp;'),st['eq'])] for x in lines]
    t=Table(rows,colWidths=[TW])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WASH),
        ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LINEBEFORE',(0,0),(0,-1),1.6,ACC)]))
    return t

def panel(title,lines,accent=MEAS,bg=WASH2):
    inner=[[Paragraph(title.upper(),st['panelh'])]]
    for x in lines: inner.append([Paragraph(sx(x),st['panel'])])
    t=Table(inner,colWidths=[TW-26])
    t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    out=Table([[t]],colWidths=[TW])
    out.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),13),('RIGHTPADDING',(0,0),(-1,-1),13),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
        ('LINEBEFORE',(0,0),(0,-1),2.2,accent)]))
    return out

def dtable(header,rows,widths=None,accent=INK):
    w=widths or [TW/len(header)]*len(header)
    data=[[Paragraph(sx(h),st['tbh']) for h in header]]
    for r in rows: data.append([Paragraph(sx(str(x)),st['tb']) for x in r])
    t=Table(data,colWidths=w,repeatRows=1,splitByRow=1)
    sty=[('BACKGROUND',(0,0),(-1,0),accent),
         ('VALIGN',(0,0),(-1,-1),'TOP'),
         ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
         ('TOPPADDING',(0,0),(-1,-1),4.5),('BOTTOMPADDING',(0,0),(-1,-1),4.5),
         ('LINEBELOW',(0,1),(-1,-2),0.4,RULE),
         ('LINEBELOW',(0,-1),(-1,-1),0.7,RULE)]
    for i in range(1,len(data)):
        if i%2==0: sty.append(('BACKGROUND',(0,i),(-1,i),HexColor('#F7F6F2')))
    t.setStyle(TableStyle(sty))
    return t

# ------------------------------------------------------------------ document
class Book(BaseDocTemplate):
    def __init__(self,path,**kw):
        BaseDocTemplate.__init__(self,path,pagesize=letter,
            leftMargin=LM,rightMargin=RM,topMargin=TM,bottomMargin=BM,
            title='TruePhase Electrical Theory',
            author='TruePhase Learning Series',
            subject='Electrical theory, machines, electronics, power and field practice',**kw)
        f=Frame(LM,BM,TW,PH-TM-BM,id='text',
                leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.toc=[]
        self.addPageTemplates([
            PageTemplate('plain',[f],onPage=self._plain),
            PageTemplate('text',[f],onPage=self._run),
            PageTemplate('open',[f],onPage=self._open),
        ])
        self.running='ELECTRICAL THEORY'
    def _bg(self,c):
        c.setFillColor(PAPER); c.rect(0,0,PW,PH,0,1)
    def _plain(self,c,d):
        self._bg(c)
    def _foot(self,c,d):
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(LM,BM-16,PW-RM,BM-16)
        c.setFont('Util',7); c.setFillColor(GREY)
        c.drawString(LM,BM-27,'TruePhase Learning Series')
        c.setFont('Mono',7.6); c.setFillColor(INK)
        c.drawRightString(PW-RM,BM-27,str(d.page))
    def _run(self,c,d):
        self._bg(c)
        c.setFont('Util',7); c.setFillColor(GREY)
        c.drawString(LM,PH-TM+22,'TRUEPHASE LEARNING SERIES')
        c.drawRightString(PW-RM,PH-TM+22,self.running[:74].upper())
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(LM,PH-TM+16,PW-RM,PH-TM+16)
        self._foot(c,d)
    def _open(self,c,d):
        self._bg(c); self._foot(c,d)
    def afterFlowable(self,fl):
        if hasattr(fl,'_bk'):
            key,text,lvl=fl._bk
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text,key,level=lvl,closed=(lvl>0))
            self.toc.append((lvl,text,self.page,key))
        if hasattr(fl,'_running'):
            self.running=fl._running

class Running(Flowable):
    def __init__(self,text): self._running=text; self.width=0; self.height=0
    def wrap(self,aw,ah): return (0,0)
    def draw(self): pass

def flatten(seq):
    out=[]
    for x in seq:
        if isinstance(x,(list,tuple)): out.extend(flatten(x))
        else: out.append(x)
    return out
