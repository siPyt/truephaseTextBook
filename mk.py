# -*- coding: utf-8 -*-
"""Builder helper: assembles a chapter dict from compact authored parts."""
from render import OH,MU,TAU,DEG,AP,TIMES

def mkch(n,title,sub,why,objs,openfig,secs,examples,lab,trouble,tfig,habits,
         exercises,answers,summary,formulas,vocab,bridge):
    return dict(n=n,title=title,sub=sub,why=why,objs=objs,openfig=openfig,secs=secs,
        examples=examples,lab=lab,trouble=trouble,tfig=tfig,habits=habits,
        exercises=exercises,answers=answers,summary=summary,formulas=formulas,
        vocab=vocab,bridge=bridge)

def lab(title,aim,gear,steps,fig,thdr,trows,questions,safety):
    return dict(title=title,aim=aim,gear=gear,steps=steps,fig=fig,thdr=thdr,
                trows=trows,questions=questions,safety=safety)

def ex(title,given,find,steps,check):
    return dict(title=title,given=given,find=find,steps=steps,check=check)

BLANK6=[["","","","",""] for _ in range(6)]
