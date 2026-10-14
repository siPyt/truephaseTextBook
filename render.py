# -*- coding: utf-8 -*-
"""Renderer: turns authored chapter dicts into Platypus story pages."""
import sys, os
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'figures'))
from engine import *
import engine, figs
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate, Table, TableStyle, KeepTogether, Image
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader

OH="\u03a9"; MU="\u00b5"; TAU="\u03c4"; DEG="\u00b0"; AP="\u2248"; TIMES="\u00d7"

# Map chapter numbers to their field photographs and captions
CHAPTER_PHOTOS = {
    3: (
        ["ch3.jpg", "ch3.jpeg", "panel.jpg", "panel.jpeg", "image_87dbcf2a.jpg"],
        "FIELD PRACTICE · Parallel branch circuits, neutral bus termination, and equipment grounding conductors in a 120/240 V distribution panel.",
        2.35 * inch
    ),
    10: (
        ["ch10.jpg", "ch10.jpeg", "substation.jpg", "substation.jpeg", "high-voltage_power_transformer_at_electrical_substation._high-voltage_power_transformer_and_electrical_substation_infrastructure_surrounded_by_transmission_equipment_and_power_lines..jpg"],
        "FIELD PRACTICE · High-voltage three-phase substation power transformer with high-voltage bushings, forced-air radiator fans, and oil conservator tank.",
        2.55 * inch
    ),
    11: (
        ["motor.jpeg", "motor.jpg", "ch11.jpg", "ch11.jpeg"],
        "FIELD PRACTICE · Industrial induction motor installation, frame cooling ribs, and terminal box connection.",
        2.55 * inch
    ),
    17: (
        ['switchgear.jpg', 'switchgear.jpeg', 'ch17.jpg', 'ch17.jpeg'],
        "FIELD PRACTICE · Industrial three-phase low-voltage switchgear lineup with draw-out air circuit breakers, status indicators, and local metering.",
        3.25 * inch
    ),
    18: (
        ["receptacle.jpeg", "receptacle.jpg", "ch18.jpg", "ch18.jpeg"],
        "FIELD PRACTICE · Branch-circuit receptacle termination, polarized line/neutral conductors, and equipment grounding path.",
        2.55 * inch
    ),
    20: (
        ["ch20.jpg", "ch20.jpeg", "penthouse.jpg", "penthouse.jpeg", "image_68fe44ed.jpg"],
        "FIELD PRACTICE · Clean installation, accurate documentation, and disciplined diagnostic habits build lasting professional competence.",
        2.35 * inch
    ),
}

def photo_block(filenames, caption, max_h=2.5*inch):
    for fname in filenames:
        for folder in (ROOT, ROOT / "figures", ROOT / "images"):
            p = folder / fname
            if p.exists():
                ir = ImageReader(str(p))
                iw, ih = ir.getSize()
                w = TW - 2
                h = w * (float(ih) / float(iw))
                if h > max_h:
                    h = max_h
                    w = h * (float(iw) / float(ih))
                img = Image(str(p), width=w, height=h)
                cap = Paragraph('<font name="Mono" size="7" color="#A8272C">PLATE</font>&nbsp;&nbsp;' + sx(caption), st['cap'])
                t = Table([[img], [cap]], colWidths=[TW])
                t.setStyle(TableStyle([
                    ('ALIGN', (0,0), (0,0), 'CENTER'),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                    ('BACKGROUND', (0,0), (0,0), HexColor('#FFFFFF')),
                    ('BOX', (0,0), (0,0), 0.8, RULE),
                    ('TOPPADDING', (0,0), (0,0), 6),
                    ('BOTTOMPADDING', (0,0), (0,0), 6),
                    ('TOPPADDING', (0,1), (0,1), 4),
                    ('BOTTOMPADDING', (0,1), (0,1), 2),
                    ('LEFTPADDING', (0,0), (-1,-1), 0),
                    ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ]))
                return [Spacer(1, 6), KeepTogether([t]), Spacer(1, 8)]
    return []

def F(name,caption,num,gh=44,gw=94):
    return fig(getattr(figs,name),caption,num,gh=gh,gw=gw)

def chapter_open(ch):
    o=[Marker('ch%d'%ch['n'],'%d. %s'%(ch['n'],ch['title']),0),
       Running('CHAPTER %d \u00b7 %s'%(ch['n'],ch['title'].upper())),
       Spacer(1,22),
       Paragraph('CHAPTER %02d'%ch['n'],st['eyebrow']),
       Rule(ACC,1.6,w=58,pad=8), Spacer(1,8),
       Paragraph(sx(ch['title']),st['ctitle']),
       Paragraph(sx(ch['sub']),st['csub']), Spacer(1,6),
       panel('Why this chapter matters',[ch['why']],accent=ACC,bg=WASH),
       Spacer(1,12), H3('What you will be able to do'),
       bullets(ch['objs']), Spacer(1,10)]
    if ch.get('openfig'):
        o.append(F(ch['openfig'][0],ch['openfig'][1],'Fig. %d.1'%ch['n'],gh=ch['openfig'][2] if len(ch['openfig'])>2 else 44))
    o+=[NextPageTemplate('text'),PageBreak()]
    return o

def render_section(ch,s,counter):
    out=[]
    if s.get('h2'): out.append(H2(s['h2']))
    for p in s.get('paras',[]): out.append(T(p))
    if s.get('bullets'): out+= [H3(s.get('bh','Key points')) if s.get('bh') else Spacer(1,2), bullets(s['bullets']), Spacer(1,4)]
    if s.get('eq'): out+=[Spacer(1,2),EQ(s['eq']),Spacer(1,6)]
    if s.get('numbered'): out+=[numbered(s['numbered']),Spacer(1,4)]
    if s.get('table'):
        h,rows,w=s['table']
        out+=[Spacer(1,3),dtable(h,rows,w),Spacer(1,8)]
    if s.get('panel'): out+=[Spacer(1,2),panel(s['panel'][0],s['panel'][1]),Spacer(1,8)]
    if s.get('fig'):
        counter[0]+=1
        name,cap=s['fig'][0],s['fig'][1]
        gh=s['fig'][2] if len(s['fig'])>2 else 46
        out+=[Spacer(1,4),F(name,cap,'Fig. %d.%d'%(ch['n'],counter[0]),gh=gh),Spacer(1,8)]
    for p in s.get('after',[]): out.append(T(p))
    return out

def render_examples(ch):
    out=[H2('Worked examples'),
         T('Work each example with a pencil before reading the solution. Sketch the circuit, '
           'mark the reference node, and write the governing law before substituting numbers.')]
    if ch['n'] in CHAPTER_PHOTOS:
        fnames, cap, max_h = CHAPTER_PHOTOS[ch['n']]
        out += photo_block(fnames, cap, max_h)
    for i,ex in enumerate(ch['examples']):
        rows=[[Paragraph('<font name="Util" size="7.6" color="#A8272C">EXAMPLE %d.%d</font>&nbsp;&nbsp;'
               '<font name="Util" size="8.6">%s</font>'%(ch['n'],i+1,sx(ex['title'])),st['panel'])]]
        rows.append([Paragraph('<b>Given.</b> '+sx(ex['given']),st['panel'])])
        rows.append([Paragraph('<b>Find.</b> '+sx(ex['find']),st['panel'])])
        body=[]
        for lab,expr in ex['steps']:
            body.append('<font name="Util" size="8">%s</font><br/><font name="Mono" size="8.6">%s</font>'%(sx(lab),sx(expr)))
        for b in body: rows.append([Paragraph(b,st['panel'])])
        rows.append([Paragraph('<b>Check.</b> '+sx(ex['check']),st['panel'])])
        t=Table(rows,colWidths=[TW-26])
        t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
            ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]))
        box=Table([[t]],colWidths=[TW])
        box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WASH),
            ('LEFTPADDING',(0,0),(-1,-1),13),('RIGHTPADDING',(0,0),(-1,-1),13),
            ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),10),
            ('LINEBEFORE',(0,0),(0,-1),2.2,ACC)]))
        out+=[Spacer(1,6),box,Spacer(1,6)]
    return out

def render_lab(ch):
    lab=ch['lab']
    out=[PageBreak(),H2('Practical activity: '+lab['title']),
         panel('Aim',[lab['aim']]),Spacer(1,8),
         H3('Equipment'),bullets(lab['gear']),Spacer(1,8),
         H3('Procedure'),numbered(lab['steps']),Spacer(1,8)]
    if lab.get('fig'):
        out+=[F(lab['fig'][0],lab['fig'][1],'Fig. %d.L'%ch['n'],gh=lab['fig'][2] if len(lab['fig'])>2 else 44),Spacer(1,8)]
    out+=[H3('Results table'),dtable(lab['thdr'],lab['trows'],lab.get('tw')),Spacer(1,10),
          H3('Discussion'),numbered(lab['questions']),Spacer(1,8),
          panel('Safe-work reminders',lab['safety'],accent=ACC,bg=WASH)]
    return out

def render_trouble(ch):
    out=[PageBreak(),H2('Troubleshooting guide'),
         T('Faults are found by narrowing the circuit, not by replacing parts. Each row below '
           'pairs an observed symptom with the measurement that separates the likely causes.')]
    out+=[Spacer(1,4),dtable(['Symptom','Likely cause','Decisive test','Correct action'],
          ch['trouble'],[TW*.24,TW*.25,TW*.27,TW*.24]),Spacer(1,10)]
    if ch.get('tfig'):
        out+=[F(ch['tfig'][0],ch['tfig'][1],'Fig. %d.T'%ch['n'],gh=ch['tfig'][2] if len(ch['tfig'])>2 else 46),Spacer(1,8)]
    return out

def render_close(ch):
    out=[panel('Field habits that prevent callbacks',ch['habits']),Spacer(1,10),
         H2('Exercises'),
         T('Answer from first principles. Selected answers follow; the reasoning matters more than the number.'),
         Spacer(1,3),numbered(ch['exercises']),Spacer(1,10),
         KeepTogether([H3('Selected answers'),dtable(['#','Answer','Reason'],ch['answers'],[TW*.07,TW*.26,TW*.67])]),
         PageBreak(),H2('Chapter summary'),bullets(ch['summary']),Spacer(1,8),
         H3('Equations introduced in this chapter'),
         dtable(['Relationship','Expression','When it applies'],ch['formulas'],[TW*.28,TW*.3,TW*.42]),
         Spacer(1,10)]
    if ch.get('vocab'):
        out+=[H3('Vocabulary check'),dtable(['Term','Meaning in this chapter'],ch['vocab'],[TW*.26,TW*.74]),Spacer(1,8)]
    if ch.get('bridge'):
        out+=[Spacer(1,4),panel('Looking ahead',[ch['bridge']],accent=MEAS)]
    out+=[NextPageTemplate('open'),PageBreak()]
    return out

def render_chapter(ch):
    counter=[1 if ch.get('openfig') else 0]
    story=chapter_open(ch)
    for s in ch['secs']: story+=render_section(ch,s,counter)
    story+=render_examples(ch)
    story+=render_lab(ch)
    story+=render_trouble(ch)
    story+=render_close(ch)
    return story
