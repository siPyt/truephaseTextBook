# -*- coding: utf-8 -*-
"""Whitelist-only schematic primitives.

Every symbol below is an original redrawing of an entry that appears in the
supplied symbol references (320204020 Electrical Symbols & Electronic Symbols,
pages 1-25, and 468998286 Common Electrical Symbols).  Nothing else may be
drawn.  APPROVED lists the canonical names.
"""
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle

INK   = HexColor("#14181C")
GRAPH = HexColor("#243039")
ACC   = HexColor("#B3282D")
MEAS  = HexColor("#1C6E72")
GREY  = HexColor("#5A6269")
WASH  = HexColor("#EFEDE7")

APPROVED = [
 # p1-3 wires & switches
 "wire","junction","terminal","bus","pb_no","pb_nc","spst","spdt","dpst","dpdt",
 "rotary3","relay",
 # p4 sources
 "ac_supply","dc_supply","cc_source",
 # p6-8 resistors
 "resistor","potentiometer","rheostat","preset","thermistor","varistor","ldr",
 "tapped_resistor",
 # p9-10 capacitors
 "capacitor","polarized_cap","electrolytic_cap","variable_cap",
 # p11-12 inductors
 "inductor","iron_core_inductor","ferrite_core_inductor","tapped_inductor",
 "variable_inductor",
 # p12-14 diodes
 "diode","zener","photodiode","led","varactor","schottky","thyristor","cc_diode",
 # p15-18 transistors
 "npn","pnp","jfet_n","jfet_p","mosfet","darlington","phototransistor",
 # p18-20 logic / amplifiers
 "and","or","nand","nor","not","xor","xnor","buffer","tristate","flipflop",
 "amplifier","opamp",
 # p21-23 transformers
 "transformer","iron_core_transformer","center_tapped_transformer",
 "step_up_transformer","step_down_transformer",
 # p23-25 misc
 "buzzer","speaker","lamp","motor","fuse","microphone","crystal","adc","dac",
 "thermocouple",
 # 468998286 sheet
 "ground","antenna",
]
U = 7.0
LW = 0.85

class D:
    def __init__(self, c, s):
        self.c, self.s = c, s
    def _p(self, x, y): return x*U*self.s, y*U*self.s
    def wire(self, *pts, color=GRAPH, w=LW):
        c=self.c; c.setStrokeColor(color); c.setLineWidth(w*self.s+0.25)
        p=c.beginPath(); x,y=self._p(*pts[0]); p.moveTo(x,y)
        for q in pts[1:]:
            x,y=self._p(*q); p.lineTo(x,y)
        c.drawPath(p)
    def dot(self,x,y,r=0.55,color=GRAPH):
        c=self.c; c.setFillColor(color); X,Y=self._p(x,y); c.circle(X,Y,r*U*self.s,0,1)
    junction=dot
    def circle(self,x,y,r,color=GRAPH,fill=None,w=LW):
        c=self.c; c.setStrokeColor(color); c.setLineWidth(w*self.s+0.25)
        if fill is not None: c.setFillColor(fill)
        X,Y=self._p(x,y); c.circle(X,Y,r*U*self.s,1,fill is not None)
    def rect(self,x,y,w,h,color=GRAPH,fill=None,lw=LW,r=0):
        c=self.c; c.setStrokeColor(color); c.setLineWidth(lw*self.s+0.25)
        if fill is not None: c.setFillColor(fill)
        X,Y=self._p(x,y); c.roundRect(X,Y,w*U*self.s,h*U*self.s,max(r*U*self.s,0.01),1,fill is not None) if r else c.rect(X,Y,w*U*self.s,h*U*self.s,1,fill is not None)
    def text(self,x,y,s,size=6.4,font="Util",color=INK,anchor="start"):
        c=self.c; c.setFillColor(color); c.setFont(font,max(5.2,size*self.s))
        X,Y=self._p(x,y)
        if anchor=="middle": c.drawCentredString(X,Y,s)
        elif anchor=="end": c.drawRightString(X,Y,s)
        else: c.drawString(X,Y,s)
    def arrow(self,x0,y0,x1,y1,color=MEAS,label=None):
        self.wire((x0,y0),(x1,y1),color=color,w=0.7)
        c=self.c; c.setFillColor(color)
        import math
        a=math.atan2(y1-y0,x1-x0); X,Y=self._p(x1,y1); L=1.5*U*self.s; w=0.75*U*self.s
        p=c.beginPath(); p.moveTo(X,Y)
        p.lineTo(X-L*math.cos(a)+w*math.sin(a), Y-L*math.sin(a)-w*math.cos(a))
        p.lineTo(X-L*math.cos(a)-w*math.sin(a), Y-L*math.sin(a)+w*math.cos(a))
        p.close(); c.drawPath(p,0,1)
        if label: self.text((x0+x1)/2,(y0+y1)/2+1.1,label,size=6.0,color=color,anchor="middle")

    # ---------------- passive two-terminal, horizontal, span 10 units
    def resistor(self,x,y,ref=None,val=None,span=10,vert=False):
        b=(span-6)/2.0
        if vert:
            self.wire((x,y),(x,y+span))
            self.rect(x-1.6,y+b,3.2,6,fill=white)
            if ref: self.text(x+2.6,y+b+4.2,ref,color=ACC)
            if val: self.text(x+2.6,y+b+1.4,val,font="Mono",size=6.2)
        else:
            self.wire((x,y),(x+span,y))
            self.rect(x+b,y-1.6,6,3.2,fill=white)
            if ref: self.text(x+span/2,y+2.4,ref,color=ACC,anchor="middle")
            if val: self.text(x+span/2,y-4.4,val,font="Mono",size=6.2,anchor="middle")
    def tapped_resistor(self,x,y,span=10):
        self.resistor(x,y,span=span)
        self.wire((x+span/2,y+1.6),(x+span/2,y+5)); self.dot(x+span/2,y+1.6,0.4)
    def potentiometer(self,x,y,span=10,ref=None):
        self.resistor(x,y,span=span,ref=ref)
        self.arrow(x+span/2,y+6.2,x+span/2,y+2.0,color=GRAPH)
    def rheostat(self,x,y,span=10,ref=None):
        self.resistor(x,y,span=span,ref=ref)
        self.arrow(x+span/2-3,y+5.6,x+span/2+2.4,y+2.0,color=GRAPH)
    preset=rheostat
    def thermistor(self,x,y,span=10,ref=None,vert=False):
        if vert:
            self.resistor(x,y,span=span,ref=ref,vert=True)
            self.wire((x-2.6,y+1.4),(x-2.6,y+3.0),(x+2.6,y+span-1.4),w=0.6)
            self.text(x+3.2,y+span-1.0,"t",size=5.8,color=GREY)
        else:
            self.resistor(x,y,span=span,ref=ref)
            self.wire((x+1.4,y-2.6),(x+3.0,y-2.6),(x+span-1.4,y+2.6),w=0.6)
            self.text(x+span-1.0,y+2.9,"t",size=5.8,color=GREY)
    def varistor(self,x,y,span=10,ref=None):
        self.resistor(x,y,span=span,ref=ref)
        self.wire((x+1.4,y-2.6),(x+3.2,y-2.6),(x+span-1.4,y+2.6),w=0.6)
        self.text(x+span-1.2,y+2.9,"U",size=5.8,color=GREY)
    def ldr(self,x,y,span=10,ref=None):
        self.resistor(x,y,span=span,ref=ref)
        for k in (0,1):
            self.arrow(x+3.0+2.4*k,y+6.4,x+4.4+2.4*k,y+2.4,color=GREY)
        self.circle(x+span/2,y,5.2,color=GREY,w=0.5)
    def capacitor(self,x,y,ref=None,val=None,span=10,vert=False,polar=False,var=False):
        g=0.9
        if vert:
            self.wire((x,y),(x,y+span/2-g)); self.wire((x,y+span/2+g),(x,y+span))
            self.wire((x-3,y+span/2-g),(x+3,y+span/2-g),w=1.5)
            if polar:
                import math
                self.c.setStrokeColor(GRAPH); self.c.setLineWidth(1.5*self.s+0.25)
                X,Y=self._p(x,y+span/2+g); self.c.arc(X-3*U*self.s,Y-1.6*U*self.s,X+3*U*self.s,Y+1.6*U*self.s,200,140)
                self.text(x+3.6,y+span/2+2.2,"+",size=6.6,color=ACC)
            else:
                self.wire((x-3,y+span/2+g),(x+3,y+span/2+g),w=1.5)
            if ref: self.text(x+4.2,y+span/2+3.6,ref,color=ACC)
            if val: self.text(x+4.2,y+span/2-5.2,val,font="Mono",size=6.2)
        else:
            self.wire((x,y),(x+span/2-g,y)); self.wire((x+span/2+g,y),(x+span,y))
            self.wire((x+span/2-g,y-3),(x+span/2-g,y+3),w=1.5)
            if polar:
                self.c.setStrokeColor(GRAPH); self.c.setLineWidth(1.5*self.s+0.25)
                X,Y=self._p(x+span/2+g,y); self.c.arc(X-1.6*U*self.s,Y-3*U*self.s,X+1.6*U*self.s,Y+3*U*self.s,110,140)
                self.text(x+span/2+2.6,y+3.4,"+",size=6.6,color=ACC)
            else:
                self.wire((x+span/2+g,y-3),(x+span/2+g,y+3),w=1.5)
            if var: self.arrow(x+span/2-4,y-4.4,x+span/2+4,y+4.4,color=GRAPH)
            if ref: self.text(x+span/2,y+4.6,ref,color=ACC,anchor="middle")
            if val: self.text(x+span/2,y-6.4,val,font="Mono",size=6.2,anchor="middle")
    def polarized_cap(self,x,y,**k): self.capacitor(x,y,polar=True,**k)
    electrolytic_cap=polarized_cap
    def variable_cap(self,x,y,**k): self.capacitor(x,y,var=True,**k)
    def inductor(self,x,y,span=10,ref=None,val=None,core=None,vert=False):
        n=4; b=(span-8)/2.0; r=1.0
        c=self.c; c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25)
        if vert:
            self.wire((x,y),(x,y+b))
            for i in range(n):
                X,Y=self._p(x,y+b+r+2*r*i); c.arc(X-r*U*self.s,Y-r*U*self.s,X+r*U*self.s,Y+r*U*self.s,-90,180)
            self.wire((x,y+b+8*r),(x,y+span))
            if ref: self.text(x+3.0,y+span/2+1.2,ref,color=ACC)
            if val: self.text(x+3.0,y+span/2-2.0,val,font="Mono",size=6.2)
            if core: self.wire((x+2.0,y+b),(x+2.0,y+b+8*r),w=1.4 if core=="iron" else 0.8)
        else:
            self.wire((x,y),(x+b,y))
            for i in range(n):
                X,Y=self._p(x+b+r+2*r*i,y); c.arc(X-r*U*self.s,Y-r*U*self.s,X+r*U*self.s,Y+r*U*self.s,0,180)
            self.wire((x+b+8*r,y),(x+span,y))
            if core: self.wire((x+b,y+2.2),(x+b+8*r,y+2.2),w=1.4 if core=="iron" else 0.8)
            if ref: self.text(x+span/2,y+(4.4 if core else 2.8),ref,color=ACC,anchor="middle")
            if val: self.text(x+span/2,y-4.6,val,font="Mono",size=6.2,anchor="middle")
    def iron_core_inductor(self,x,y,**k): self.inductor(x,y,core="iron",**k)
    def ferrite_core_inductor(self,x,y,**k): self.inductor(x,y,core="ferrite",**k)
    def tapped_inductor(self,x,y,span=10,**k):
        self.inductor(x,y,span=span,**k); self.wire((x+span/2,y),(x+span/2,y-4.4))
    def variable_inductor(self,x,y,span=10,**k):
        self.inductor(x,y,span=span,**k); self.arrow(x+2,y-3.6,x+span-2,y+3.6,color=GRAPH)
    # ---------------- sources
    def dc_supply(self,x,y,ref=None,val=None,n=2,h=8):
        """Battery / DC supply, vertical, + at top."""
        step=h/(2.0*n); yy=y
        self.wire((x,y),(x,y+step*0.6)); yy=y+step*0.6
        for i in range(n):
            self.wire((x-3.0,yy),(x+3.0,yy),w=1.6); yy+=step*0.75
            self.wire((x-1.5,yy),(x+1.5,yy),w=1.6); yy+=step*0.75
        self.wire((x,y),(x,y+h))
        self.text(x+4.0,y+h-1.6,"+",size=7.2,color=ACC)
        self.text(x+4.0,y+0.6,"\u2212",size=7.2,color=GREY)
        if ref: self.text(x-4.2,y+h-1.6,ref,color=ACC,anchor="end")
        if val: self.text(x-4.2,y+0.6,val,font="Mono",size=6.2,anchor="end")
    def ac_supply(self,x,y,r=3.4,ref=None,val=None):
        self.circle(x,y,r,fill=white)
        c=self.c; c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25)
        X,Y=self._p(x,y); rr=r*U*self.s
        p=c.beginPath(); p.moveTo(X-rr*0.62,Y)
        import math
        for i in range(1,41):
            t=i/40.0; p.lineTo(X-rr*0.62+1.24*rr*t, Y+rr*0.42*math.sin(2*math.pi*t))
        c.drawPath(p)
        if ref: self.text(x,y+r+1.6,ref,color=ACC,anchor="middle")
        if val: self.text(x,y-r-4.0,val,font="Mono",size=6.2,anchor="middle")
    def cc_source(self,x,y,r=3.4,ref=None,val=None):
        self.circle(x,y,r,fill=white)
        self.wire((x,y-r),(x,y+r),w=1.3)
        self.arrow(x-r*0.0,y-r-2.6,x,y-r-0.2,color=GRAPH)
        if ref: self.text(x,y+r+1.6,ref,color=ACC,anchor="middle")
        if val: self.text(x+r+1.2,y-1.0,val,font="Mono",size=6.2)
    # ---------------- switches, protection, loads
    def terminal(self,x,y,label=None):
        self.circle(x,y,0.85,fill=white,w=0.8)
        if label: self.text(x,y+2.0,label,size=6.0,color=GREY,anchor="middle")
    def bus(self,x0,x1,y,label=None):
        self.wire((x0,y),(x1,y),w=2.4)
        if label: self.text(x0,y+2.0,label,size=6.0,color=GREY)
    def spst(self,x,y,span=8,closed=False,ref=None):
        self.terminal(x+1.0,y); self.terminal(x+span-1.0,y)
        self.wire((x,y),(x+1.0,y)); self.wire((x+span-1.0,y),(x+span,y))
        self.wire((x+1.0,y),(x+span-1.0,y) if closed else (x+span-1.8,y+3.4))
        if ref: self.text(x+span/2,y+4.6,ref,color=ACC,anchor="middle")
    def spdt(self,x,y,span=8,ref=None):
        self.terminal(x+1.0,y); self.terminal(x+span-1.0,y+2.4); self.terminal(x+span-1.0,y-2.4)
        self.wire((x,y),(x+0.15,y))
        self.wire((x+span-1.0,y+2.4),(x+span,y+2.4)); self.wire((x+span-1.0,y-2.4),(x+span,y-2.4))
        self.wire((x+1.0,y),(x+span-1.4,y+2.2))
        if ref: self.text(x+span/2,y+5.0,ref,color=ACC,anchor="middle")
    def dpst(self,x,y,span=8,ref=None,gap=5.0):
        self.spst(x,y,span); self.spst(x,y+gap,span)
        self.wire((x+span-1.8,y+3.4),(x+span-1.8,y+gap+3.4),w=0.5,color=GREY)
        if ref: self.text(x+span/2,y+gap+5.0,ref,color=ACC,anchor="middle")
    def dpdt(self,x,y,span=8,ref=None,gap=7.0):
        self.spdt(x,y,span); self.spdt(x,y+gap,span)
        self.wire((x+span-1.4,y+2.2),(x+span-1.4,y+gap+2.2),w=0.5,color=GREY)
        if ref: self.text(x+span/2,y+gap+5.2,ref,color=ACC,anchor="middle")
    def rotary3(self,x,y,ref=None):
        self.terminal(x,y)
        for k,dy in enumerate((3.4,0,-3.4)):
            self.terminal(x+7,y+dy); self.wire((x+7,y+dy),(x+9,y+dy))
        self.wire((x,y),(x+6.2,y+3.1))
        if ref: self.text(x+4.5,y+5.4,ref,color=ACC,anchor="middle")
    def pb_no(self,x,y,span=8,ref=None):
        self.terminal(x+1.0,y); self.terminal(x+span-1.0,y)
        self.wire((x,y),(x+1.0,y)); self.wire((x+span-1.0,y),(x+span,y))
        self.wire((x+1.0,y+2.6),(x+span-1.0,y+2.6))
        self.wire((x+span/2,y+2.6),(x+span/2,y+5.2))
        self.wire((x+span/2-1.8,y+5.2),(x+span/2+1.8,y+5.2),w=1.5)
        if ref: self.text(x+span/2,y+6.4,ref,color=ACC,anchor="middle")
    def pb_nc(self,x,y,span=8,ref=None):
        self.terminal(x+1.0,y); self.terminal(x+span-1.0,y)
        self.wire((x,y),(x+1.0,y)); self.wire((x+span-1.0,y),(x+span,y))
        self.wire((x+1.0,y),(x+span-1.0,y))
        self.wire((x+span/2,y),(x+span/2,y+5.2))
        self.wire((x+span/2-1.8,y+5.2),(x+span/2+1.8,y+5.2),w=1.5)
        if ref: self.text(x+span/2,y+6.4,ref,color=ACC,anchor="middle")
    def relay(self,x,y,ref=None):
        self.rect(x,y,7,5,fill=WASH)
        for i in range(4):
            X=x+0.9+1.5*i; self.wire((X,y+0.9),(X,y+4.1),w=1.2)
        self.wire((x+7,y+2.5),(x+9.6,y+2.5),w=0.5,color=GREY)
        self.spst(x+9.6,y+2.5,7.0)
        if ref: self.text(x+3.5,y+5.8,ref,color=ACC,anchor="middle")
    def fuse(self,x,y,span=10,ref=None,val=None,vert=False):
        b=(span-6)/2.0
        if vert:
            self.wire((x,y),(x,y+span))
            self.rect(x-1.8,y+b,3.6,6,fill=white)
            self.wire((x,y+b),(x,y+b+6))
            if ref: self.text(x+3.2,y+span/2+2.0,ref,color=ACC)
            if val: self.text(x+3.2,y+span/2-4.0,val,font="Mono",size=6.2)
        else:
            self.wire((x,y),(x+span,y))
            self.rect(x+b,y-1.8,6,3.6,fill=white)
            self.wire((x+b,y),(x+b+6,y))
            if ref: self.text(x+span/2,y+2.8,ref,color=ACC,anchor="middle")
            if val: self.text(x+span/2,y-5.0,val,font="Mono",size=6.2,anchor="middle")
    def lamp(self,x,y,r=3.2,ref=None,val=None):
        self.circle(x,y,r,fill=white)
        k=r*0.70
        self.wire((x-k,y-k),(x+k,y+k)); self.wire((x-k,y+k),(x+k,y-k))
        if ref: self.text(x,y+r+1.6,ref,color=ACC,anchor="middle")
        if val: self.text(x,y-r-4.0,val,font="Mono",size=6.2,anchor="middle")
    def motor(self,x,y,r=3.6,ref=None,val=None):
        self.circle(x,y,r,fill=white)
        self.text(x,y-1.2,"M",size=7.4,font="Disp",anchor="middle")
        if ref: self.text(x,y+r+1.6,ref,color=ACC,anchor="middle")
        if val: self.text(x,y-r-4.0,val,font="Mono",size=6.2,anchor="middle")
    def buzzer(self,x,y,ref=None):
        c=self.c; self.rect(x,y,5,3.4,fill=white)
        self.wire((x+5,y),(x+7.2,y),(x+7.2,y+3.4),(x+5,y+3.4))
        if ref: self.text(x+2.5,y+4.2,ref,color=ACC,anchor="middle")
    def speaker(self,x,y,ref=None):
        self.rect(x,y,2.4,5.0,fill=white)
        self.wire((x+2.4,y+0.4),(x+6.4,y-1.6),(x+6.4,y+6.6),(x+2.4,y+4.6))
        if ref: self.text(x+3.0,y+7.4,ref,color=ACC,anchor="middle")
    def microphone(self,x,y,ref=None):
        self.circle(x,y,2.6,fill=white); self.wire((x-2.6,y-2.6),(x+2.6,y-2.6),w=1.4)
        if ref: self.text(x,y+3.4,ref,color=ACC,anchor="middle")
    def crystal(self,x,y,span=10,ref=None):
        b=(span-4)/2.0
        self.wire((x,y),(x+b,y)); self.wire((x+span-b,y),(x+span,y))
        self.wire((x+b,y-3),(x+b,y+3),w=1.5); self.wire((x+span-b,y-3),(x+span-b,y+3),w=1.5)
        self.rect(x+b+0.8,y-2.2,2.4,4.4,fill=white)
        if ref: self.text(x+span/2,y+4.0,ref,color=ACC,anchor="middle")
    def thermocouple(self,x,y,ref=None):
        self.wire((x,y+2.2),(x+5,y)); self.wire((x,y-2.2),(x+5,y)); self.wire((x+5,y),(x+9,y))
        if ref: self.text(x+4.5,y+3.2,ref,color=ACC,anchor="middle")
    def ground(self,x,y,label=None):
        self.wire((x,y),(x,y-2.2))
        for i,w in enumerate((4.0,2.6,1.3)):
            self.wire((x-w/2,y-2.2-1.5*i),(x+w/2,y-2.2-1.5*i),w=1.3)
        if label: self.text(x+3.2,y-4.4,label,size=6.0,color=GREY)
    def antenna(self,x,y,label=None):
        self.wire((x,y),(x,y+5)); self.wire((x-3,y+8),(x,y+5),(x+3,y+8))
        if label: self.text(x,y+9.2,label,size=6.0,color=GREY,anchor="middle")
    # ---------------- semiconductors
    def diode(self,x,y,span=10,ref=None,kind="pn",vert=False,flip=False):
        b=(span-4)/2.0
        c=self.c; c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25)
        if vert:
            self.wire((x,y),(x,y+b)); self.wire((x,y+span-b),(x,y+span))
            X,Y=self._p(x,y+b); s=U*self.s
            p=c.beginPath()
            if not flip:
                p.moveTo(X-2.6*s,Y); p.lineTo(X+2.6*s,Y); p.lineTo(X,Y+4*s); p.close()
                c.setFillColor(GRAPH); c.drawPath(p,1,1)
                self.wire((x-2.6,y+b+4),(x+2.6,y+b+4),w=1.6)
            else:
                p.moveTo(X-2.6*s,Y+4*s); p.lineTo(X+2.6*s,Y+4*s); p.lineTo(X,Y); p.close()
                c.setFillColor(GRAPH); c.drawPath(p,1,1)
                self.wire((x-2.6,y+b),(x+2.6,y+b),w=1.6)
            if ref: self.text(x+3.4,y+b+1.6,ref,color=ACC)
            return
        self.wire((x,y),(x+b,y)); self.wire((x+span-b,y),(x+span,y))
        X,Y=self._p(x+b,y); s=U*self.s
        p=c.beginPath(); p.moveTo(X,Y-2.6*s); p.lineTo(X,Y+2.6*s); p.lineTo(X+4*s,Y); p.close()
        c.setFillColor(GRAPH); c.drawPath(p,1,1)
        bx=x+b+4
        if kind=="pn": self.wire((bx,y-2.6),(bx,y+2.6),w=1.6)
        elif kind=="zener":
            self.wire((bx,y-2.6),(bx,y+2.6),w=1.6); self.wire((bx,y+2.6),(bx-1.4,y+3.8),w=1.6)
            self.wire((bx,y-2.6),(bx+1.4,y-3.8),w=1.6)
        elif kind=="schottky":
            self.wire((bx-1.3,y+1.6),(bx-1.3,y+2.6),(bx,y+2.6),(bx,y-2.6),(bx+1.3,y-2.6),(bx+1.3,y-1.6),w=1.5)
        elif kind=="cc":
            self.wire((bx,y-2.6),(bx,y+2.6),w=1.6)
            self.wire((bx+1.0,y-2.6),(bx+1.0,y+2.6),w=1.0)
        elif kind=="varactor":
            self.wire((bx,y-2.6),(bx,y+2.6),w=1.6)
            self.wire((bx+1.2,y-2.6),(bx+1.2,y+2.6),w=1.6)
        if kind in ("led","photo"):
            self.wire((bx,y-2.6),(bx,y+2.6),w=1.6)
            for k in (0,1):
                if kind=="led": self.arrow(x+b+1.4+1.8*k,y+3.4,x+b+2.8+1.8*k,y+6.4,color=GREY)
                else: self.arrow(x+b+2.8+1.8*k,y+6.4,x+b+1.4+1.8*k,y+3.4,color=GREY)
        if ref: self.text(x+span/2,y+(7.4 if kind in ("led","photo") else 3.6),ref,color=ACC,anchor="middle")
    def zener(self,x,y,**k): self.diode(x,y,kind="zener",**k)
    def schottky(self,x,y,**k): self.diode(x,y,kind="schottky",**k)
    def led(self,x,y,**k): self.diode(x,y,kind="led",**k)
    def photodiode(self,x,y,**k): self.diode(x,y,kind="photo",**k)
    def varactor(self,x,y,**k): self.diode(x,y,kind="varactor",**k)
    def cc_diode(self,x,y,**k): self.diode(x,y,kind="cc",**k)
    def thyristor(self,x,y,span=10,ref=None):
        self.diode(x,y,span=span)
        b=(span-4)/2.0
        self.wire((x+b+4,y),(x+b+5.6,y-4.0))
        self.text(x+b+6.0,y-5.4,"G",size=5.8,color=GREY)
        if ref: self.text(x+span/2,y+3.6,ref,color=ACC,anchor="middle")
    def npn(self,x,y,ref=None,pnp=False):
        """Bipolar transistor, base at left, collector top, emitter bottom."""
        self.wire((x,y),(x+3.4,y))
        self.wire((x+3.4,y-3.4),(x+3.4,y+3.4),w=1.8)
        self.wire((x+3.4,y+1.8),(x+7.6,y+5.4)); self.wire((x+7.6,y+5.4),(x+7.6,y+8.2))
        self.wire((x+3.4,y-1.8),(x+7.6,y-5.4)); self.wire((x+7.6,y-5.4),(x+7.6,y-8.2))
        if pnp: self.arrow(x+6.0,y-4.2,x+4.0,y-2.5,color=GRAPH)
        else:   self.arrow(x+5.2,y-3.4,x+7.2,y-5.1,color=GRAPH)
        self.circle(x+4.6,y,6.4,color=GREY,w=0.5)
        self.text(x-0.6,y+1.2,"B",size=5.8,color=GREY,anchor="end")
        self.text(x+8.4,y+7.6,"C",size=5.8,color=GREY)
        self.text(x+8.4,y-8.2,"E",size=5.8,color=GREY)
        if ref: self.text(x+4.6,y+8.0,ref,color=ACC,anchor="middle")
    def pnp(self,x,y,**k): self.npn(x,y,pnp=True,**k)
    def darlington(self,x,y,ref=None):
        self.npn(x,y); self.npn(x+11,y-1.0)
        self.wire((x+7.6,y+8.2),(x+18.6,y+7.2))
        if ref: self.text(x+9,y+10.0,ref,color=ACC,anchor="middle")
    def phototransistor(self,x,y,ref=None):
        self.npn(x,y,ref=ref)
        for k in (0,1): self.arrow(x-4.4+1.8*k,y+7.0,x-2.4+1.8*k,y+3.4,color=GREY)
    def jfet_n(self,x,y,ref=None,p=False):
        self.wire((x,y),(x+3.4,y))
        self.wire((x+3.4,y-4.0),(x+3.4,y+4.0),w=1.8)
        self.wire((x+3.4,y+3.0),(x+7.4,y+3.0),(x+7.4,y+7.4))
        self.wire((x+3.4,y-3.0),(x+7.4,y-3.0),(x+7.4,y-7.4))
        self.arrow(x+0.4,y,x+3.0,y,color=GRAPH) if not p else self.arrow(x+3.0,y,x+0.6,y,color=GRAPH)
        self.circle(x+4.4,y,6.2,color=GREY,w=0.5)
        self.text(x-0.6,y+1.2,"G",size=5.8,color=GREY,anchor="end")
        self.text(x+8.2,y+6.8,"D",size=5.8,color=GREY)
        self.text(x+8.2,y-7.4,"S",size=5.8,color=GREY)
        if ref: self.text(x+4.4,y+7.6,ref,color=ACC,anchor="middle")
    def jfet_p(self,x,y,**k): self.jfet_n(x,y,p=True,**k)
    def mosfet(self,x,y,ref=None,dep=False):
        self.wire((x,y),(x+2.6,y)); self.wire((x+2.6,y-4.2),(x+2.6,y+4.2),w=1.5)
        if dep:
            self.wire((x+4.4,y-4.2),(x+4.4,y+4.2),w=1.8)
        else:
            for dy in (-3.2,0,3.2): self.wire((x+4.4,y+dy-1.1),(x+4.4,y+dy+1.1),w=1.8)
        self.wire((x+4.4,y+3.2),(x+8.4,y+3.2),(x+8.4,y+7.4))
        self.wire((x+4.4,y-3.2),(x+8.4,y-3.2),(x+8.4,y-7.4))
        self.wire((x+4.4,y),(x+8.4,y),(x+8.4,y-3.2))
        self.arrow(x+6.4,y,x+4.9,y,color=GRAPH)
        self.circle(x+5.4,y,6.4,color=GREY,w=0.5)
        self.text(x-0.6,y+1.2,"G",size=5.8,color=GREY,anchor="end")
        self.text(x+9.2,y+6.8,"D",size=5.8,color=GREY)
        self.text(x+9.2,y-7.4,"S",size=5.8,color=GREY)
        if ref: self.text(x+5.4,y+7.8,ref,color=ACC,anchor="middle")
    # ---------------- logic & amplifiers
    def _gatebody(self,x,y,kind):
        c=self.c; s=U*self.s; c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25); c.setFillColor(white)
        X,Y=self._p(x,y)
        p=c.beginPath()
        if kind in ("and","nand"):
            p.moveTo(X,Y); p.lineTo(X,Y+8*s); p.lineTo(X+4*s,Y+8*s)
            p.curveTo(X+9*s,Y+8*s,X+9*s,Y,X+4*s,Y); p.close()
        else:
            p.moveTo(X,Y)
            p.curveTo(X+2.5*s,Y+4*s,X+2.5*s,Y+4*s,X,Y+8*s)
            p.curveTo(X+5*s,Y+8*s,X+8.4*s,Y+5.6*s,X+9.6*s,Y+4*s)
            p.curveTo(X+8.4*s,Y+2.4*s,X+5*s,Y,X,Y); p.close()
        c.drawPath(p,1,1)
    def gate(self,x,y,kind="and",ref=None,labels=("A","B")):
        inv = kind in ("nand","nor","not","xnor")
        base = {"nand":"and","nor":"or","xnor":"or","xor":"or","not":"not"}.get(kind,kind)
        if kind in ("not","buffer","tristate"):
            c=self.c; s=U*self.s; X,Y=self._p(x,y)
            c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25); c.setFillColor(white)
            p=c.beginPath(); p.moveTo(X,Y); p.lineTo(X,Y+8*s); p.lineTo(X+8*s,Y+4*s); p.close()
            c.drawPath(p,1,1)
            self.wire((x-3,y+4),(x,y+4)); w_end=x+8
            if kind=="not":
                self.circle(x+9.0,y+4,1.0,fill=white); w_end=x+10.0
            self.wire((w_end,y+4),(w_end+3,y+4))
            if kind=="tristate": self.wire((x+4,y+7.0),(x+4,y+10.0))
            if ref: self.text(x+4,y+9.4 if kind!="tristate" else y+11.0,ref,color=ACC,anchor="middle")
            return
        self._gatebody(x,y,base)
        w=9.6 if base=="or" else 9.0
        self.wire((x-3,y+5.8),(x+(0.9 if base=="or" else 0),y+5.8))
        self.wire((x-3,y+2.2),(x+(0.9 if base=="or" else 0),y+2.2))
        if labels:
            self.text(x-3.6,y+5.2,labels[0],size=5.8,color=GREY,anchor="end")
            self.text(x-3.6,y+1.6,labels[1],size=5.8,color=GREY,anchor="end")
        end=x+w
        if kind=="xor" or kind=="xnor":
            c=self.c; s=U*self.s; X,Y=self._p(x-1.6,y)
            c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25)
            p=c.beginPath(); p.moveTo(X,Y); p.curveTo(X+2.5*s,Y+4*s,X+2.5*s,Y+4*s,X,Y+8*s); c.drawPath(p)
        if inv:
            self.circle(end+1.0,y+4,1.0,fill=white); end+=2.0
        self.wire((end,y+4),(end+3,y+4))
        if ref: self.text(x+4.5,y+9.4,ref,color=ACC,anchor="middle")
    def flipflop(self,x,y,ref=None,pins=(("S","Q"),("CLK",""),("R","Q\u0305"))):
        self.rect(x,y,12,12,fill=white)
        for i,(l,r) in enumerate(pins):
            yy=y+10.0-4.4*i
            if l:
                self.wire((x-3,yy),(x,yy)); self.text(x+1.0,yy-1.2,l,size=5.8,color=GREY)
            if r:
                self.wire((x+12,yy),(x+15,yy)); self.text(x+11.0,yy-1.2,r,size=5.8,color=GREY,anchor="end")
        if ref: self.text(x+6,y+12.8,ref,color=ACC,anchor="middle")
    def amplifier(self,x,y,ref=None,opamp=False):
        c=self.c; s=U*self.s; X,Y=self._p(x,y)
        c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25); c.setFillColor(white)
        p=c.beginPath(); p.moveTo(X,Y); p.lineTo(X,Y+11*s); p.lineTo(X+11*s,Y+5.5*s); p.close()
        c.drawPath(p,1,1)
        if opamp:
            self.wire((x-3,y+8.0),(x,y+8.0)); self.wire((x-3,y+3.0),(x,y+3.0))
            self.text(x+1.4,y+7.2,"\u2212",size=7.0,color=GREY)
            self.text(x+1.4,y+2.2,"+",size=7.0,color=GREY)
            self.wire((x+4.0,y+9.2),(x+4.0,y+12.4)); self.text(x+4.8,y+11.6,"V+",size=5.6,color=GREY)
            self.wire((x+4.0,y+1.8),(x+4.0,y-1.4)); self.text(x+4.8,y-2.4,"V\u2212",size=5.6,color=GREY)
        else:
            self.wire((x-3,y+5.5),(x,y+5.5))
        self.wire((x+11,y+5.5),(x+14,y+5.5))
        if ref: self.text(x+5.5,y+12.8 if not opamp else y+13.6,ref,color=ACC,anchor="middle")
    def opamp(self,x,y,**k): self.amplifier(x,y,opamp=True,**k)
    # ---------------- transformers
    def transformer(self,x,y,core=None,ref=None,ct=False,ratio=None,np=4,ns=4):
        r=1.0
        c=self.c; c.setStrokeColor(GRAPH); c.setLineWidth(LW*self.s+0.25)
        top=y+max(np,ns)*2*r
        self.wire((x,top+2.0),(x,top)); self.wire((x,y),(x,y-2.0))
        for i in range(np):
            X,Y=self._p(x,y+r+2*r*i); c.arc(X-r*U*self.s,Y-r*U*self.s,X+r*U*self.s,Y+r*U*self.s,-90,180)
        x2=x+6.0
        self.wire((x2,top+2.0),(x2,top)); self.wire((x2,y),(x2,y-2.0))
        for i in range(ns):
            X,Y=self._p(x2,y+r+2*r*i); c.arc(X-r*U*self.s,Y-r*U*self.s,X+r*U*self.s,Y+r*U*self.s,90,180)
        if core=="iron":
            self.wire((x+2.4,y-0.4),(x+2.4,top+0.4),w=1.4)
            self.wire((x+3.6,y-0.4),(x+3.6,top+0.4),w=1.4)
        if ct:
            self.wire((x2,y+max(np,ns)*r),(x2+4.0,y+max(np,ns)*r))
        if ref: self.text(x+3.0,top+3.0,ref,color=ACC,anchor="middle")
        if ratio: self.text(x+3.0,y-5.0,ratio,font="Mono",size=6.2,anchor="middle")
    def iron_core_transformer(self,x,y,**k): self.transformer(x,y,core="iron",**k)
    def center_tapped_transformer(self,x,y,**k): self.transformer(x,y,core="iron",ct=True,**k)
    def step_up_transformer(self,x,y,**k): self.transformer(x,y,core="iron",np=3,ns=6,**k)
    def step_down_transformer(self,x,y,**k): self.transformer(x,y,core="iron",np=6,ns=3,**k)
    # ---------------- converters
    def adc(self,x,y,ref="ADC"):
        self.rect(x,y,11,8,fill=white)
        self.wire((x-3,y+4),(x,y+4))
        for i in range(3): self.wire((x+11,y+1.6+2.4*i),(x+14,y+1.6+2.4*i))
        self.text(x+5.5,y+3.4,ref,size=6.2,anchor="middle")
    def dac(self,x,y,ref="DAC"):
        self.rect(x,y,11,8,fill=white)
        for i in range(3): self.wire((x-3,y+1.6+2.4*i),(x,y+1.6+2.4*i))
        self.wire((x+11,y+4),(x+14,y+4))
        self.text(x+5.5,y+3.4,ref,size=6.2,anchor="middle")
