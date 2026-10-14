# -*- coding: utf-8 -*-
"""ANSI / IEEE 315 Standard Vector Schematic Primitives."""
import math
from reportlab.lib.colors import HexColor, white

INK   = HexColor("#14181C")
GRAPH = HexColor("#182026")
ACC   = HexColor("#A8272C")
MEAS  = HexColor("#1B6B70")
GREY  = HexColor("#525A60")
WASH  = HexColor("#F2F0EA")

U = 7.0
LW = 1.25

class D:
    def __init__(self, c, s):
        self.c, self.s = c, s

    def _p(self, x, y):
        return x * U * self.s, y * U * self.s

    def wire(self, *pts, color=GRAPH, w=LW, dash=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(w * self.s + 0.35)
        c.setLineCap(1)
        c.setLineJoin(1)
        if dash:
            c.setDash(dash[0] * self.s, dash[1] * self.s)
        p = c.beginPath()
        x, y = self._p(*pts[0])
        p.moveTo(x, y)
        for q in pts[1:]:
            x, y = self._p(*q)
            p.lineTo(x, y)
        c.drawPath(p, stroke=1, fill=0)
        c.restoreState()

    def dot(self, x, y, r=0.6, color=GRAPH):
        c = self.c
        c.saveState()
        c.setFillColor(color)
        X, Y = self._p(x, y)
        c.circle(X, Y, r * U * self.s, stroke=0, fill=1)
        c.restoreState()
    junction = dot

    def circle(self, x, y, r, color=GRAPH, fill=None, w=LW):
        c = self.c
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(w * self.s + 0.35)
        if fill is not None:
            c.setFillColor(fill)
        X, Y = self._p(x, y)
        c.circle(X, Y, r * U * self.s, stroke=1, fill=(fill is not None))
        c.restoreState()

    def rect(self, x, y, w, h, color=GRAPH, fill=None, lw=LW):
        c = self.c
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(lw * self.s + 0.35)
        c.setLineJoin(0)
        if fill is not None:
            c.setFillColor(fill)
        X, Y = self._p(x, y)
        c.rect(X, Y, w * U * self.s, h * U * self.s, stroke=1, fill=(fill is not None))
        c.restoreState()

    def poly(self, pts, color=GRAPH, fill=None, lw=LW, close=True):
        c = self.c
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(lw * self.s + 0.35)
        c.setLineJoin(1)
        if fill is not None:
            c.setFillColor(fill)
        p = c.beginPath()
        x0, y0 = self._p(*pts[0])
        p.moveTo(x0, y0)
        for pt in pts[1:]:
            px, py = self._p(*pt)
            p.lineTo(px, py)
        if close:
            p.close()
        c.drawPath(p, stroke=1, fill=(fill is not None))
        c.restoreState()

    def text(self, x, y, s, size=6.6, font="Util", color=INK, anchor="start"):
        c = self.c
        c.saveState()
        c.setFillColor(color)
        c.setFont(font, max(5.8, size * self.s))
        X, Y = self._p(x, y)
        if anchor == "middle":
            c.drawCentredString(X, Y, s)
        elif anchor == "end":
            c.drawRightString(X, Y, s)
        else:
            c.drawString(X, Y, s)
        c.restoreState()

    def arrow(self, x0, y0, x1, y1, color=MEAS, label=None):
        self.wire((x0, y0), (x1, y1), color=color, w=1.0)
        a = math.atan2(y1 - y0, x1 - x0)
        L, w = 1.5, 0.65
        p1 = (x1 - L * math.cos(a) + w * math.sin(a), y1 - L * math.sin(a) - w * math.cos(a))
        p2 = (x1 - L * math.cos(a) - w * math.sin(a), y1 - L * math.sin(a) + w * math.cos(a))
        self.poly([(x1, y1), p1, p2], color=color, fill=color, lw=0.4)
        if label:
            self.text((x0 + x1) / 2.0, (y0 + y1) / 2.0 + 1.4, label, size=6.4, color=color, anchor="middle")

    # ---------------- ANSI / IEEE 315 ZIGZAG RESISTOR
    def resistor(self, x, y, ref=None, val=None, span=10, vert=False):
        """Standard IEEE 315 6-peak (3-cycle) Zigzag Resistor."""
        rw = 6.0
        b = (span - rw) / 2.0
        amp = 1.35
        step = rw / 12.0  # 12 quarter-steps = 3 full peaks up, 3 down
        if vert:
            pts = [
                (x, y),
                (x, y + b),
                (x + amp, y + b + 1 * step),
                (x - amp, y + b + 3 * step),
                (x + amp, y + b + 5 * step),
                (x - amp, y + b + 7 * step),
                (x + amp, y + b + 9 * step),
                (x - amp, y + b + 11 * step),
                (x, y + b + 12 * step),
                (x, y + span),
            ]
            self.wire(*pts)
            if ref: self.text(x + 2.2, y + span / 2.0 + 0.8, ref, color=ACC, size=6.5)
            if val: self.text(x + 2.2, y + span / 2.0 - 1.8, val, font="Mono", size=6.2)
        else:
            pts = [
                (x, y),
                (x + b, y),
                (x + b + 1 * step, y + amp),
                (x + b + 3 * step, y - amp),
                (x + b + 5 * step, y + amp),
                (x + b + 7 * step, y - amp),
                (x + b + 9 * step, y + amp),
                (x + b + 11 * step, y - amp),
                (x + b + 12 * step, y),
                (x + span, y),
            ]
            self.wire(*pts)
            if ref: self.text(x + span / 2.0, y + 2.3, ref, color=ACC, anchor="middle", size=6.5)
            if val: self.text(x + span / 2.0, y - 3.9, val, font="Mono", size=6.2, anchor="middle")

    def tapped_resistor(self, x, y, span=10):
        self.resistor(x, y, span=span)
        self.wire((x + span / 2.0, y + 1.35), (x + span / 2.0, y + 4.5))

    def potentiometer(self, x, y, span=10, ref=None):
        self.resistor(x, y, span=span)
        self.arrow(x + span / 2.0, y + 5.0, x + span / 2.0, y + 1.4, color=GRAPH)
        if ref: self.text(x + span / 2.0 + 2.4, y + 3.2, ref, color=ACC, size=6.5)

    def rheostat(self, x, y, span=10, ref=None):
        self.resistor(x, y, span=span)
        self.arrow(x + span / 2.0 - 2.6, y - 2.8, x + span / 2.0 + 2.6, y + 2.8, color=GRAPH)
        if ref: self.text(x + span / 2.0 - 2.2, y + 2.6, ref, color=ACC, size=6.5)
    preset = rheostat

    def thermistor(self, x, y, span=10, ref=None, vert=False):
        if vert:
            self.resistor(x, y, span=span, ref=ref, vert=True)
            self.wire((x - 2.2, y + 1.8), (x - 2.2, y + 2.8), (x + 2.2, y + span - 1.8), w=0.9)
            self.text(x - 3.8, y + 1.4, "t°", size=5.8, color=GREY)
        else:
            self.resistor(x, y, span=span, ref=ref)
            self.wire((x + 2.2, y - 2.2), (x + 3.2, y - 2.2), (x + span - 2.2, y + 2.2), w=0.9)
            self.text(x + 1.6, y - 4.2, "t°", size=5.8, color=GREY)

    def varistor(self, x, y, span=10, ref=None):
        self.resistor(x, y, span=span, ref=ref)
        self.wire((x + 2.2, y - 2.2), (x + 3.2, y - 2.2), (x + span - 2.2, y + 2.2), w=0.9)
        self.text(x + 1.6, y - 4.2, "V", size=5.8, color=GREY)

    def ldr(self, x, y, span=10, ref=None):
        self.resistor(x, y, span=span)
        self.arrow(x + 2.2, y + 5.0, x + 3.8, y + 2.0, color=GRAPH)
        self.arrow(x + 4.2, y + 5.0, x + 5.8, y + 2.0, color=GRAPH)
        if ref: self.text(x + span / 2.0, y - 4.2, ref, color=ACC, anchor="middle", size=6.5)

    # ---------------- ANSI / IEEE 315 CAPACITOR (Flat + Curved Polarized)
    def capacitor(self, x, y, ref=None, val=None, span=10, vert=False, polar=False, var=False):
        g, pw = 0.8, 2.6
        if vert:
            self.wire((x, y), (x, y + span / 2.0 - g))
            self.wire((x, y + span / 2.0 + g), (x, y + span))
            self.wire((x - pw, y + span / 2.0 + g), (x + pw, y + span / 2.0 + g), w=1.6)
            if polar:
                c = self.c
                c.saveState()
                c.setStrokeColor(GRAPH)
                c.setLineWidth(1.6 * self.s + 0.35)
                X, Y = self._p(x, y + span / 2.0 - g - 1.1)
                c.arc(X - pw * U * self.s, Y - 1.1 * U * self.s, X + pw * U * self.s, Y + 1.1 * U * self.s, 22, 136)
                c.restoreState()
                self.text(x - 3.6, y + span / 2.0 + 1.4, "+", size=7.0, color=ACC)
            else:
                self.wire((x - pw, y + span / 2.0 - g), (x + pw, y + span / 2.0 - g), w=1.6)
            if ref: self.text(x + 3.4, y + span / 2.0 + 1.2, ref, color=ACC, size=6.5)
            if val: self.text(x + 3.4, y + span / 2.0 - 2.2, val, font="Mono", size=6.2)
        else:
            self.wire((x, y), (x + span / 2.0 - g, y))
            self.wire((x + span / 2.0 + g, y), (x + span, y))
            self.wire((x + span / 2.0 - g, y - pw), (x + span / 2.0 - g, y + pw), w=1.6)
            if polar:
                c = self.c
                c.saveState()
                c.setStrokeColor(GRAPH)
                c.setLineWidth(1.6 * self.s + 0.35)
                X, Y = self._p(x + span / 2.0 + g + 1.1, y)
                c.arc(X - 1.1 * U * self.s, Y - pw * U * self.s, X + 1.1 * U * self.s, Y + pw * U * self.s, 112, 136)
                c.restoreState()
                self.text(x + span / 2.0 - 2.8, y + 2.8, "+", size=7.0, color=ACC)
            else:
                self.wire((x + span / 2.0 + g, y - pw), (x + span / 2.0 + g, y + pw), w=1.6)
            if var: self.arrow(x + span / 2.0 - 3.0, y - 3.2, x + span / 2.0 + 3.0, y + 3.2, color=GRAPH)
            if ref: self.text(x + span / 2.0, y + 3.6, ref, color=ACC, anchor="middle", size=6.5)
            if val: self.text(x + span / 2.0, y - 4.8, val, font="Mono", size=6.2, anchor="middle")
    def polarized_cap(self, x, y, **k): self.capacitor(x, y, polar=True, **k)
    electrolytic_cap = polarized_cap
    def variable_cap(self, x, y, **k): self.capacitor(x, y, var=True, **k)

    # ---------------- ANSI / IEEE 315 INDUCTOR (4 Crisp Loops)
    def inductor(self, x, y, span=10, ref=None, val=None, core=None, vert=False):
        n, r = 4, 0.9
        coil_len = 2 * n * r
        b = (span - coil_len) / 2.0
        c = self.c
        c.saveState()
        c.setStrokeColor(GRAPH)
        c.setLineWidth(LW * self.s + 0.35)
        if vert:
            self.wire((x, y), (x, y + b))
            for i in range(n):
                X, Y = self._p(x, y + b + r + 2 * r * i)
                c.arc(X - r * U * self.s, Y - r * U * self.s, X + r * U * self.s, Y + r * U * self.s, -90, 180)
            self.wire((x, y + b + coil_len), (x, y + span))
            if core == "iron":
                self.wire((x - 1.5, y + b), (x - 1.5, y + b + coil_len), w=1.2)
                self.wire((x - 2.3, y + b), (x - 2.3, y + b + coil_len), w=1.2)
            elif core == "ferrite":
                self.wire((x - 1.6, y + b), (x - 1.6, y + b + coil_len), w=1.2, dash=(3, 2))
            if ref: self.text(x + 2.4, y + span / 2.0 + 1.0, ref, color=ACC, size=6.5)
            if val: self.text(x + 2.4, y + span / 2.0 - 2.0, val, font="Mono", size=6.2)
        else:
            self.wire((x, y), (x + b, y))
            for i in range(n):
                X, Y = self._p(x + b + r + 2 * r * i, y)
                c.arc(X - r * U * self.s, Y - r * U * self.s, X + r * U * self.s, Y + r * U * self.s, 0, 180)
            self.wire((x + b + coil_len, y), (x + span, y))
            if core == "iron":
                self.wire((x + b, y + 1.5), (x + b + coil_len, y + 1.5), w=1.2)
                self.wire((x + b, y + 2.3), (x + b + coil_len, y + 2.3), w=1.2)
            elif core == "ferrite":
                self.wire((x + b, y + 1.6), (x + b + coil_len, y + 1.6), w=1.2, dash=(3, 2))
            if ref: self.text(x + span / 2.0, y + (3.4 if core else 2.4), ref, color=ACC, anchor="middle", size=6.5)
            if val: self.text(x + span / 2.0, y - 3.8, val, font="Mono", size=6.2, anchor="middle")
        c.restoreState()

    def iron_core_inductor(self, x, y, **k): self.inductor(x, y, core="iron", **k)
    def ferrite_core_inductor(self, x, y, **k): self.inductor(x, y, core="ferrite", **k)
    def tapped_inductor(self, x, y, span=10, **k):
        self.inductor(x, y, span=span, **k); self.wire((x + span / 2.0, y), (x + span / 2.0, y - 4.0))
    def variable_inductor(self, x, y, span=10, **k):
        self.inductor(x, y, span=span, **k); self.arrow(x + 2, y - 3.2, x + span - 2, y + 3.2, color=GRAPH)

    def coil_block(self, x, y, span=10, ref=None, val=None, vert=True):
        """Relay / Contactor Coil."""
        self.iron_core_inductor(x, y, span=span, ref=ref, val=val, vert=vert)

    # ---------------- ANSI / IEEE 315 Multi-Cell DC Battery & AC Sources
    def dc_supply(self, x, y, ref=None, val=None, n=2, h=10):
        """Standard 2-cell (4-plate) DC Battery Stack, exact span (x,y) to (x,y+h)."""
        core_h = 3.6
        y_bot = y + (h - core_h) / 2.0
        y_top = y_bot + core_h
        self.wire((x, y), (x, y_bot))
        self.wire((x, y_top), (x, y + h))
        dy = core_h / 3.0
        for i in range(4):
            py = y_bot + i * dy
            if i % 2 == 0:
                self.wire((x - 1.5, py), (x + 1.5, py), w=2.2) # Negative short thick
            else:
                self.wire((x - 3.2, py), (x + 3.2, py), w=1.1) # Positive long thin
        self.text(x + 3.8, y_top - 0.3, "+", size=7.0, color=ACC)
        self.text(x + 3.8, y_bot - 0.8, "−", size=7.0, color=GREY)
        if ref: self.text(x - 4.0, y + h / 2.0 + 1.0, ref, color=ACC, anchor="end", size=6.5)
        if val: self.text(x - 4.0, y + h / 2.0 - 0.8, val, font="Mono", size=6.2, anchor="end")

    def ac_supply(self, x, y, r=3.5, ref=None, val=None):
        self.wire((x, y - 4.0), (x, y + 4.0))
        self.circle(x, y, r, fill=white)
        c = self.c
        c.saveState()
        c.setStrokeColor(GRAPH)
        c.setLineWidth(LW * self.s + 0.35)
        X, Y = self._p(x, y)
        rr = r * U * self.s
        p = c.beginPath()
        p.moveTo(X - rr * 0.58, Y)
        for i in range(1, 33):
            t = i / 32.0
            p.lineTo(X - rr * 0.58 + 1.16 * rr * t, Y + rr * 0.38 * math.sin(2 * math.pi * t))
        c.drawPath(p)
        c.restoreState()
        if ref: self.text(x, y + r + 1.4, ref, color=ACC, anchor="middle", size=6.5)
        if val: self.text(x - r - 1.2, y - 0.8, val, font="Mono", size=6.2, anchor="end")

    def cc_source(self, x, y, r=3.5, ref=None, val=None):
        self.wire((x, y - 4.0), (x, y + 4.0))
        self.circle(x, y, r, fill=white)
        self.arrow(x, y - r * 0.65, x, y + r * 0.65, color=GRAPH)
        if ref: self.text(x, y + r + 1.4, ref, color=ACC, anchor="middle", size=6.5)

    # ---------------- ANSI / IEEE 315 Switches, Pushbuttons, Relays & Fuse
    def terminal(self, x, y, label=None):
        self.circle(x, y, 0.65, fill=white, w=0.95)
        if label: self.text(x, y + 1.8, label, size=6.0, color=GREY, anchor="middle")

    def bus(self, x0, x1, y, label=None):
        self.wire((x0, y), (x1, y), w=2.5)
        if label: self.text(x0, y + 1.6, label, size=6.2, color=GREY)

    def spst(self, x, y, span=8, closed=False, ref=None):
        b = 1.6
        self.wire((x, y), (x + b, y))
        self.wire((x + span - b, y), (x + span, y))
        self.wire((x + b, y), (x + span - b, y) if closed else (x + span - b - 0.3, y + 2.4))
        self.terminal(x + b, y)
        self.terminal(x + span - b, y)
        if ref: self.text(x + span / 2.0, y + 3.6, ref, color=ACC, anchor="middle", size=6.5)

    def spdt(self, x, y, span=8, ref=None):
        b = 1.6
        self.wire((x, y), (x + b, y))
        self.wire((x + span - b, y + 2.4), (x + span, y + 2.4))
        self.wire((x + span - b, y - 2.4), (x + span, y - 2.4))
        self.wire((x + b, y), (x + span - b - 0.2, y + 2.2))
        self.terminal(x + b, y)
        self.terminal(x + span - b, y + 2.4)
        self.terminal(x + span - b, y - 2.4)
        if ref: self.text(x + span / 2.0, y + 4.2, ref, color=ACC, anchor="middle", size=6.5)

    def dpst(self, x, y, span=8, ref=None, gap=4.8):
        self.spst(x, y, span)
        self.spst(x, y + gap, span)
        self.wire((x + span / 2.0, y + 1.2), (x + span / 2.0, y + gap + 1.2), w=0.65, color=GREY, dash=(2, 2))
        if ref: self.text(x + span / 2.0, y + gap + 3.6, ref, color=ACC, anchor="middle", size=6.5)

    def dpdt(self, x, y, span=8, ref=None, gap=6.4):
        self.spdt(x, y, span)
        self.spdt(x, y + gap, span)
        self.wire((x + span / 2.0, y + 1.2), (x + span / 2.0, y + gap + 1.2), w=0.65, color=GREY, dash=(2, 2))
        if ref: self.text(x + span / 2.0, y + gap + 4.2, ref, color=ACC, anchor="middle", size=6.5)

    def rotary3(self, x, y, ref=None):
        self.wire((x, y), (x + 1.8, y))
        self.wire((x + 1.8, y), (x + 6.0, y + 2.2))
        self.terminal(x + 1.8, y)
        for dy in (2.4, 0, -2.4):
            self.wire((x + 6.4, y + dy), (x + 8.5, y + dy))
            self.terminal(x + 6.4, y + dy)
        if ref: self.text(x + 4.5, y + 4.4, ref, color=ACC, anchor="middle", size=6.5)

    def pb_no(self, x, y, span=8, ref=None):
        b = 1.6
        self.wire((x, y), (x + b, y))
        self.wire((x + span - b, y), (x + span, y))
        self.terminal(x + b, y)
        self.terminal(x + span - b, y)
        self.wire((x + b - 0.3, y + 2.0), (x + span - b + 0.3, y + 2.0), w=1.4)
        self.wire((x + span / 2.0, y + 2.0), (x + span / 2.0, y + 4.0))
        if ref: self.text(x + span / 2.0, y + 4.8, ref, color=ACC, anchor="middle", size=6.5)

    def pb_nc(self, x, y, span=8, ref=None):
        b = 1.6
        self.wire((x, y), (x + b, y))
        self.wire((x + span - b, y), (x + span, y))
        self.wire((x + b - 0.3, y - 0.8), (x + span - b + 0.3, y - 0.8), w=1.4)
        self.terminal(x + b, y)
        self.terminal(x + span - b, y)
        self.wire((x + span / 2.0, y - 0.8), (x + span / 2.0, y + 3.4))
        if ref: self.text(x + span / 2.0, y + 4.4, ref, color=ACC, anchor="middle", size=6.5)

    def relay(self, x, y, ref=None):
        """Relay coil linked to SPST contact."""
        self.rect(x, y + 0.4, 5.2, 3.6, fill=white)
        self.wire((x, y + 0.4), (x + 5.2, y + 4.0), w=0.8) # Standard coil slash
        self.wire((x + 5.2, y + 2.2), (x + 8.6, y + 2.2), w=0.65, color=GREY, dash=(2.2, 1.8))
        self.spst(x + 8.6, y + 2.2, 7.4)
        if ref: self.text(x + 2.6, y + 4.8, ref, color=ACC, anchor="middle", size=6.5)

    def fuse(self, x, y, span=10, ref=None, val=None, vert=False):
        """ANSI / IEEE 315 S-Curve Fuse (distinct from zigzag resistor)."""
        b = (span - 5.6) / 2.0
        c = self.c
        c.saveState()
        c.setStrokeColor(GRAPH)
        c.setLineWidth(LW * self.s + 0.35)
        if vert:
            self.wire((x, y), (x, y + b))
            self.wire((x, y + span - b), (x, y + span))
            X0, Y0 = self._p(x, y + b)
            X1, Y1 = self._p(x, y + span - b)
            s = U * self.s
            p = c.beginPath()
            p.moveTo(X0, Y0)
            p.curveTo(X0 - 2.2 * s, Y0 + 1.8 * s, X1 + 2.2 * s, Y1 - 1.8 * s, X1, Y1)
            c.drawPath(p, stroke=1, fill=0)
            self.terminal(x, y + b)
            self.terminal(x, y + span - b)
            if ref: self.text(x + 2.2, y + span / 2.0 + 0.8, ref, color=ACC, size=6.5)
            if val: self.text(x + 2.2, y + span / 2.0 - 1.8, val, font="Mono", size=6.2)
        else:
            self.wire((x, y), (x + b, y))
            self.wire((x + span - b, y), (x + span, y))
            X0, Y0 = self._p(x + b, y)
            X1, Y1 = self._p(x + span - b, y)
            s = U * self.s
            p = c.beginPath()
            p.moveTo(X0, Y0)
            p.curveTo(X0 + 1.8 * s, Y0 + 2.2 * s, X1 - 1.8 * s, Y1 - 2.2 * s, X1, Y1)
            c.drawPath(p, stroke=1, fill=0)
            self.terminal(x + b, y)
            self.terminal(x + span - b, y)
            if ref: self.text(x + span / 2.0, y + 2.3, ref, color=ACC, anchor="middle", size=6.5)
            if val: self.text(x + span / 2.0, y - 3.9, val, font="Mono", size=6.2, anchor="middle")
        c.restoreState()

    def lamp(self, x, y, r=3.0, ref=None, val=None):
        self.circle(x, y, r, fill=white)
        k = r * 0.707
        self.wire((x - k, y - k), (x + k, y + k))
        self.wire((x - k, y + k), (x + k, y - k))
        if ref: self.text(x, y + r + 1.4, ref, color=ACC, anchor="middle", size=6.5)
        if val: self.text(x, y - r - 3.4, val, font="Mono", size=6.2, anchor="middle")

    def motor(self, x, y, r=3.4, ref=None, val=None, sym="M"):
        self.circle(x, y, r, fill=white)
        self.text(x, y - 1.2, sym, size=7.4, font="Disp", anchor="middle")
        if ref: self.text(x, y + r + 1.4, ref, color=ACC, anchor="middle", size=6.5)
        if val: self.text(x, y - r - 3.4, val, font="Mono", size=6.2, anchor="middle")

    def buzzer(self, x, y, ref=None):
        self.rect(x, y, 4.4, 3.0, fill=white)
        self.wire((x + 1.0, y), (x + 1.0, y - 1.2))
        self.wire((x + 3.4, y), (x + 3.4, y - 1.2))
        if ref: self.text(x + 2.2, y + 3.8, ref, color=ACC, anchor="middle", size=6.5)

    def speaker(self, x, y, ref=None):
        self.rect(x, y, 2.2, 3.6, fill=white)
        self.poly([(x + 2.2, y + 3.6), (x + 5.2, y + 5.4), (x + 5.2, y - 1.8), (x + 2.2, y)], fill=white)
        if ref: self.text(x + 2.6, y + 6.2, ref, color=ACC, anchor="middle", size=6.5)

    def thermocouple(self, x, y, ref=None):
        self.wire((x, y), (x + 4.5, y + 1.8), (x + 9.0, y + 1.8))
        self.wire((x, y), (x + 4.5, y - 1.8), (x + 9.0, y - 1.8))
        self.dot(x, y, 0.55)
        if ref: self.text(x + 2.5, y + 3.0, ref, color=ACC, anchor="middle", size=6.5)

    def ground(self, x, y, label=None):
        self.wire((x, y), (x, y - 2.0))
        for i, w in enumerate((3.8, 2.4, 1.1)):
            self.wire((x - w / 2.0, y - 2.0 - 1.0 * i), (x + w / 2.0, y - 2.0 - 1.0 * i), w=1.3)
        if label: self.text(x + 2.6, y - 3.6, label, size=6.2, color=GREY)

    # ---------------- ANSI / IEEE 315 Semiconductors (Solid Filled Diode Triangles)
    def diode(self, x, y, span=10, ref=None, kind="pn", vert=False, flip=False):
        b = (span - 3.4) / 2.0
        hw = 1.9
        if vert:
            self.wire((x, y), (x, y + span))
            if not flip:
                by = y + b + 3.4
                self.poly([(x - hw, y + b), (x + hw, y + b), (x, by)], fill=GRAPH)
                self.wire((x - hw, by), (x + hw, by), w=1.5)
                if kind == "zener":
                    self.wire((x - hw, by), (x - hw - 0.8, by + 0.8), w=1.4)
                    self.wire((x + hw, by), (x + hw + 0.8, by - 0.8), w=1.4)
            else:
                by = y + b
                self.poly([(x - hw, y + b + 3.4), (x + hw, y + b + 3.4), (x, by)], fill=GRAPH)
                self.wire((x - hw, by), (x + hw, by), w=1.5)
                if kind == "zener":
                    self.wire((x - hw, by), (x - hw - 0.8, by + 0.8), w=1.4)
                    self.wire((x + hw, by), (x + hw + 0.8, by - 0.8), w=1.4)
            if ref: self.text(x + 2.8, y + span / 2.0 - 0.5, ref, color=ACC, size=6.5)
            return

        bx = x + b + 3.4
        self.wire((x, y), (x + span, y))
        self.poly([(x + b, y - hw), (x + b, y + hw), (bx, y)], fill=GRAPH)
        self.wire((bx, y - hw), (bx, y + hw), w=1.5)
        if kind == "zener":
            self.wire((bx, y + hw), (bx - 0.8, y + hw + 0.8), w=1.4)
            self.wire((bx, y - hw), (bx + 0.8, y - hw - 0.8), w=1.4)
        elif kind in ("led", "photo"):
            for k in (0, 1):
                if kind == "led":
                    self.arrow(x + b + 1.0 + 1.6 * k, y + 2.4, x + b + 2.4 + 1.6 * k, y + 4.8, color=GRAPH)
                else:
                    self.arrow(x + b + 2.4 + 1.6 * k, y + 4.8, x + b + 1.0 + 1.6 * k, y + 2.4, color=GRAPH)
        if ref: self.text(x + span / 2.0, y + (5.4 if kind in ("led", "photo") else 2.8), ref, color=ACC, anchor="middle", size=6.5)

    def zener(self, x, y, **k): self.diode(x, y, kind="zener", **k)
    def led(self, x, y, **k): self.diode(x, y, kind="led", **k)

    def npn(self, x, y, ref=None, pnp=False):
        self.circle(x + 4.2, y, 4.8, color=GRAPH, fill=white, w=0.85)
        self.wire((x, y), (x + 2.8, y))
        self.wire((x + 2.8, y - 2.6), (x + 2.8, y + 2.6), w=1.7)
        self.wire((x + 2.8, y + 1.2), (x + 6.0, y + 3.8), (x + 6.0, y + 6.0))
        self.wire((x + 2.8, y - 1.2), (x + 6.0, y - 3.8), (x + 6.0, y - 6.0))
        if pnp: self.arrow(x + 5.2, y - 3.15, x + 3.3, y - 1.6, color=GRAPH)
        else: self.arrow(x + 3.4, y - 1.7, x + 5.5, y - 3.4, color=GRAPH)
        if ref: self.text(x + 0.5, y + 5.2, ref, color=ACC, size=6.5)
    def pnp(self, x, y, **k): self.npn(x, y, pnp=True, **k)

    def mosfet(self, x, y, ref=None, dep=False):
        self.circle(x + 4.4, y, 4.8, color=GRAPH, fill=white, w=0.85)
        self.wire((x, y), (x + 2.4, y))
        self.wire((x + 2.4, y - 2.6), (x + 2.4, y + 2.6), w=1.3)
        for dy in (-2.0, 0, 2.0):
            self.wire((x + 3.5, y + dy - 0.65), (x + 3.5, y + dy + 0.65), w=1.6)
        self.wire((x + 3.5, y + 2.0), (x + 6.0, y + 2.0), (x + 6.0, y + 6.0))
        self.wire((x + 3.5, y - 2.0), (x + 6.0, y - 2.0), (x + 6.0, y - 6.0))
        self.wire((x + 3.5, y), (x + 6.0, y), (x + 6.0, y - 2.0))
        self.arrow(x + 5.5, y, x + 3.8, y, color=GRAPH)
        if ref: self.text(x + 0.5, y + 5.2, ref, color=ACC, size=6.5)

    # ---------------- ANSI / IEEE 315 Distinctive-Shape Logic Gates
    def _gatebody(self, x, y, kind):
        c = self.c
        c.saveState()
        s = U * self.s
        c.setStrokeColor(GRAPH)
        c.setLineWidth(LW * self.s + 0.35)
        c.setFillColor(white)
        X, Y = self._p(x, y)
        p = c.beginPath()
        if kind in ("and", "nand"):
            p.moveTo(X, Y); p.lineTo(X, Y + 8 * s); p.lineTo(X + 4.2 * s, Y + 8 * s)
            p.curveTo(X + 9.2 * s, Y + 8 * s, X + 9.2 * s, Y, X + 4.2 * s, Y); p.close()
        else:
            p.moveTo(X, Y)
            p.curveTo(X + 2.4 * s, Y + 4 * s, X + 2.4 * s, Y + 4 * s, X, Y + 8 * s)
            p.curveTo(X + 5 * s, Y + 8 * s, X + 8.2 * s, Y + 5.6 * s, X + 9.4 * s, Y + 4 * s)
            p.curveTo(X + 8.2 * s, Y + 2.4 * s, X + 5 * s, Y, X, Y); p.close()
        c.drawPath(p, 1, 1)
        c.restoreState()

    def gate(self, x, y, kind="and", ref=None, labels=("A", "B")):
        inv = kind in ("nand", "nor", "not", "xnor")
        base = {"nand": "and", "nor": "or", "xnor": "or", "xor": "or", "not": "not"}.get(kind, kind)
        if kind in ("not", "buffer", "tristate"):
            self.poly([(x, y), (x, y + 8.0), (x + 7.5, y + 4.0)], fill=white)
            self.wire((x - 3.0, y + 4.0), (x, y + 4.0))
            w_end = x + 7.5
            if kind == "not":
                self.circle(x + 8.4, y + 4.0, 0.9, fill=white); w_end = x + 9.3
            self.wire((w_end, y + 4.0), (x + 12.0, y + 4.0))
            if kind == "tristate": self.wire((x + 3.8, y + 6.0), (x + 3.8, y + 9.2))
            if ref: self.text(x + 3.8, y + (9.2 if kind != "tristate" else 10.2), ref, color=ACC, anchor="middle", size=6.5)
            return
        self._gatebody(x, y, base)
        w = 9.4 if base == "or" else 8.0
        self.wire((x - 3.0, y + 6.0), (x + (1.1 if base == "or" else 0), y + 6.0))
        self.wire((x - 3.0, y + 2.0), (x + (1.1 if base == "or" else 0), y + 2.0))
        if labels:
            self.text(x - 3.4, y + 5.4, labels[0], size=5.8, color=GREY, anchor="end")
            self.text(x - 3.4, y + 1.4, labels[1], size=5.8, color=GREY, anchor="end")
        end = x + w
        if kind in ("xor", "xnor"):
            c = self.c; c.saveState(); s = U * self.s; X, Y = self._p(x - 1.4, y)
            c.setStrokeColor(GRAPH); c.setLineWidth(LW * self.s + 0.35)
            p = c.beginPath(); p.moveTo(X, Y); p.curveTo(X + 2.4 * s, Y + 4 * s, X + 2.4 * s, Y + 4 * s, X, Y + 8 * s); c.drawPath(p)
            c.restoreState()
        if inv:
            self.circle(end + 0.9, y + 4.0, 0.9, fill=white); end += 1.8
        self.wire((end, y + 4.0), (x + 12.0, y + 4.0))
        if ref: self.text(x + 4.2, y + 9.2, ref, color=ACC, anchor="middle", size=6.5)

    def flipflop(self, x, y, ref=None, pins=(("S", "Q"), ("CLK", ""), ("R", "Q̅"))):
        self.rect(x, y, 11.0, 11.0, fill=white)
        for i, (l, r) in enumerate(pins):
            yy = y + 9.0 - 3.5 * i
            if l:
                self.wire((x - 3.0, yy), (x, yy))
                self.text(x + 1.0, yy - 0.9, l, size=5.8, color=GREY)
            if r:
                self.wire((x + 11.0, yy), (x + 14.0, yy))
                self.text(x + 10.0, yy - 0.9, r, size=5.8, color=GREY, anchor="end")
        if ref: self.text(x + 5.5, y + 12.0, ref, color=ACC, anchor="middle", size=6.5)

    def opamp(self, x, y, ref=None):
        self.poly([(x, y), (x, y + 11.0), (x + 11.0, y + 5.5)], fill=white)
        self.wire((x - 3.0, y + 8.0), (x, y + 8.0))
        self.wire((x - 3.0, y + 3.0), (x, y + 3.0))
        self.text(x + 1.2, y + 7.3, "−", size=7.0, color=GREY)
        self.text(x + 1.2, y + 2.3, "+", size=7.0, color=GREY)
        self.wire((x + 11.0, y + 5.5), (x + 14.0, y + 5.5))
        if ref: self.text(x + 4.5, y + 11.4, ref, color=ACC, anchor="middle", size=6.5)
    amplifier = opamp

    def transformer(self, x, y, core="iron", ref=None, ct=False, ratio=None):
        h = 8.0
        r = h / 8.0
        c = self.c
        c.saveState()
        c.setStrokeColor(GRAPH)
        c.setLineWidth(LW * self.s + 0.35)
        for i in range(4):
            X, Y = self._p(x, y + r + 2 * r * i)
            c.arc(X - r * U * self.s, Y - r * U * self.s, X + r * U * self.s, Y + r * U * self.s, -90, 180)
        x2 = x + 8.0
        for i in range(4):
            X, Y = self._p(x2, y + r + 2 * r * i)
            c.arc(X - r * U * self.s, Y - r * U * self.s, X + r * U * self.s, Y + r * U * self.s, 90, 180)
        c.restoreState()
        if core == "iron":
            self.wire((x + 3.5, y), (x + 3.5, y + h), w=1.2)
            self.wire((x + 4.5, y), (x + 4.5, y + h), w=1.2)
        if ct:
            self.wire((x2, y + h / 2.0), (x2 + 4.0, y + h / 2.0))
            self.dot(x2, y + h / 2.0, 0.45)
        if ref: self.text(x + 4.0, y + h + 1.4, ref, color=ACC, anchor="middle", size=6.5)
        if ratio: self.text(x + 4.0, y - 3.2, ratio, font="Mono", size=6.2, anchor="middle")

    def iron_core_transformer(self, x, y, **k): self.transformer(x, y, core="iron", **k)
    def center_tapped_transformer(self, x, y, **k): self.transformer(x, y, core="iron", ct=True, **k)
    def step_up_transformer(self, x, y, **k): self.transformer(x, y, core="iron", **k)
    def step_down_transformer(self, x, y, **k): self.transformer(x, y, core="iron", **k)

    def adc(self, x, y, ref="ADC"):
        self.rect(x, y, 10.0, 7.6, fill=white)
        self.wire((x - 3.0, y + 3.8), (x, y + 3.8))
        for i in range(3):
            self.wire((x + 10.0, y + 1.6 + 2.2 * i), (x + 13.0, y + 1.6 + 2.2 * i))
        self.text(x + 5.0, y + 3.0, ref, size=6.4, anchor="middle")

    def dac(self, x, y, ref="DAC"):
        self.rect(x, y, 10.0, 7.6, fill=white)
        for i in range(3):
            self.wire((x - 3.0, y + 1.6 + 2.2 * i), (x, y + 1.6 + 2.2 * i))
        self.wire((x + 10.0, y + 3.8), (x + 13.0, y + 3.8))
        self.text(x + 5.0, y + 3.0, ref, size=6.4, anchor="middle")
