# -*- coding: utf-8 -*-
"""Front and back matter."""
import sys; from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'figures'))
from engine import *
from render import F, OH, MU, TAU, DEG, AP, TIMES
import figs
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate, Table, TableStyle
from reportlab.lib.colors import HexColor, white

CHTITLES=[
 (1,"Charge, voltage, current and energy"),(2,"Kirchhoff's laws and circuit analysis"),
 (3,"Series, parallel and divider networks"),(4,"Capacitance and transient response"),
 (5,"Inductance and magnetic energy storage"),(6,"Alternating quantities and their measurement"),
 (7,"Impedance, phase and power factor"),(8,"Resonance and filters"),
 (9,"Magnetism and electromagnetic induction"),(10,"Transformers"),
 (11,"Rotating machines"),(12,"Diodes and rectification"),
 (13,"Transistors as switches and amplifiers"),(14,"Operational amplifiers"),
 (15,"Digital logic and signals"),(16,"Power supplies and regulation"),
 (17,"Three-phase systems"),(18,"Safety, fault paths and protection"),
 (19,"Control, sensing and signal conversion"),(20,"Diagnosis, design review and lasting habits")]

def cover():
    return [NextPageTemplate('plain'),
     Spacer(1,36),
     Paragraph('TRUEPHASE LEARNING SERIES',st['eyebrow']),
     Rule(ACC,2.0,w=92,pad=12), Spacer(1,14),
     Paragraph('Electrical<br/>Theory',st['cover1']), Spacer(1,18),
     Paragraph('A working textbook of circuits, fields, machines, electronics, '
               'power and field practice',st['lead']),
     Spacer(1,10),
     Paragraph('Twenty chapters with worked examples, measurement activities, '
               'troubleshooting tables, exercises and a complete reference section. '
               'Every schematic in this book is drawn from one approved symbol set.',st['body']),
     Spacer(1,22),
     (lambda: next((Table([[__import__('reportlab.platypus',fromlist=['Image']).Image(str(p), width=TW, height=TW*(9.0/16.0))]], colWidths=[TW], style=[('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),('BOX',(0,0),(-1,-1),1.5,ACC)]) for n in ('cover.jpg','cover.png','image_833c0317.jpg') for p in (ROOT/n, ROOT/'figures'/n, ROOT/'images'/n) if p.exists()), F('legend_a','The conductor and termination symbols used throughout this book.','',gh=46)))(),
     PageBreak(),
     Spacer(1,40), Paragraph('About this book',st['h1']),
     Rule(ACC,1.4,w=58,pad=10),
     T('This book develops electrical theory in the order that makes it usable. Each chapter '
       'states a model, derives the relationships that follow from it, shows the model applied '
       'to a worked problem, then puts an instrument on a real circuit to test whether the '
       'model held. Where a model breaks down, the chapter says so.'),
     T('The progression runs from charge and current, through the conservation laws and network '
       'analysis, into energy storage and the transient and alternating behaviour that follows '
       'from it. Magnetism leads to transformers and rotating machines. Semiconductors lead to '
       'rectification, amplification, logic and regulated supplies. The last chapters address '
       'three-phase distribution, safety and fault clearance, control and sensing, and the '
       'diagnostic method that ties the whole subject together.'),
     H3('How each chapter is built'),
     bullets(['An opening statement of why the material matters and what you will be able to do.',
       'Explanatory sections with equations set out and their conditions of validity stated.',
       'Worked examples showing the full reasoning, not only the arithmetic.',
       'A practical activity with equipment list, procedure, results table and discussion.',
       'A troubleshooting table pairing symptoms with the measurement that identifies the cause.',
       'Exercises with selected answers, a summary, an equation list and a vocabulary check.']),
     H3('A note on codes and standards'),
     T('Numerical requirements in electrical work are set by codes that are revised on a cycle. '
       'Where this book gives a limit, a disconnection time or a permitted method, treat it as '
       'illustrating the method rather than as the authority. The authority is the edition of '
       'the code in force where the work is carried out. The physics in this book does not '
       'change between editions; the numbers sometimes do.'),
     panel('Safety',['The practical activities in this book are specified at low voltage wherever '
       'the principle allows it, because a principle demonstrated at 12 V is the same principle '
       'at 400 V with none of the risk. Where mains voltage is unavoidable, the activity says so '
       'and states the precautions. Do not substitute a higher voltage for convenience.',
       'Isolate, lock off and prove dead before working on any circuit. Prove the test instrument '
       'on a known source before and after use.'],accent=ACC,bg=WASH),
     PageBreak()]

def contents():
    rows=[]
    for n,t in CHTITLES:
        rows.append([Paragraph('<font name="Mono" size="8.6" color="#A8272C">%02d</font>'%n,st['tocl']),
                     Paragraph(sx(t),st['tocl'])])
    rows.append([Paragraph('<font name="Mono" size="8.6" color="#1B6B70">R</font>',st['tocl']),
                 Paragraph('Reference section: equations, units, symbols, checklists, glossary',st['tocl'])])
    t=Table(rows,colWidths=[TW*.07,TW*.93])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
      ('TOPPADDING',(0,0),(-1,-1),4.5),('BOTTOMPADDING',(0,0),(-1,-1),4.5),
      ('LINEBELOW',(0,0),(-1,-2),0.4,RULE)]))
    return [Spacer(1,34),Paragraph('Contents',st['h1']),Rule(ACC,1.4,w=58,pad=10),
      T('Chapter starts are linked in the PDF bookmarks panel. Each chapter is self-contained '
        'but assumes the chapters before it.'),
      Spacer(1,8),t,PageBreak()]

def symbolkey():
    o=[NextPageTemplate('text'),
       Marker('symkey','Symbol key',0), Running('SYMBOL KEY'),
       Spacer(1,20), Paragraph('The symbol set used in this book',st['h1']),
       Rule(ACC,1.4,w=58,pad=10),
       T('Every schematic in this book is drawn from the set below and from nothing else. The '
         'symbols follow the conventions of the referenced symbol standards, redrawn as vector '
         'line work so that they reproduce at any size. Learn this page and every diagram in the '
         'book becomes readable.')]
    for fn,cap in [('legend_a','Conductors, joints and terminations.'),
                   ('legend_b','Switching and control devices.'),
                   ('legend_c','Sources, loads and protection.'),
                   ('legend_d','Passive components and semiconductors.'),
                   ('legend_e','Logic, amplifiers, machines and instruments.')]:
        o+=[Spacer(1,6),F(fn,cap,'',gh=46),Spacer(1,4)]
    o+=[NextPageTemplate('open'),PageBreak()]
    return o

def _ref(title,intro,header,rows,widths=None,running='REFERENCE SECTION'):
    return [H2(title),T(intro),Spacer(1,4),dtable(header,rows,widths),Spacer(1,10)]

def backmatter():
    o=[NextPageTemplate('text'),Marker('ref','Reference section',0),
       Running('REFERENCE SECTION'),
       Spacer(1,20),Paragraph('Reference section',st['h1']),Rule(MEAS,1.4,w=58,pad=10),
       T('Everything in this section appears somewhere in the chapters. It is gathered here so '
         'that it can be used without searching. The equation list is ordered by subject, and '
         'every entry states the conditions under which it applies.'),
       Spacer(1,8)]

    o+=_ref('Fundamental relationships',
      'The relationships that follow directly from the definitions of charge, current, voltage '
      'and energy. These hold for any circuit at any instant.',
      ['Quantity','Expression','Conditions'],
      [['Current','I = Q / t','Steady current; otherwise the instantaneous rate of charge flow'],
       ['Voltage','V = W / Q','Energy per unit charge between two points'],
       ['Resistance','R = V / I','Defines resistance; constant only for a linear element'],
       ["Ohm's law",'V = I R','Linear resistive element at constant temperature'],
       ['Power','P = V I','Any element, instantaneous values'],
       ['Power, resistive','P = I\u00b2 R = V\u00b2 / R','Resistive element only'],
       ['Energy','E = P t','Constant power over the interval t'],
       ['Resistivity','R = \u03c1 L / A','Uniform conductor of length L and area A'],
       ['Temperature effect','R\u209c = R\u2080(1 + \u03b1 \u0394T)','Over a modest temperature range']],
      [TW*.26,TW*.28,TW*.46])

    o+=_ref('Network analysis',
      'The conservation laws and the standard network reductions derived from them.',
      ['Relationship','Expression','When it applies'],
      [['Current law','\u03a3 I_in = \u03a3 I_out','At any node, at every instant'],
       ['Voltage law','\u03a3 V = 0','Around any closed loop'],
       ['Series resistance','R = R\u2081 + R\u2082 + ...','Elements carrying the same current'],
       ['Parallel resistance','1/R = 1/R\u2081 + 1/R\u2082 + ...','Elements across the same voltage'],
       ['Two in parallel','R = R\u2081R\u2082/(R\u2081+R\u2082)','Convenient form for exactly two'],
       ['Voltage divider','V\u2082 = V R\u2082/(R\u2081+R\u2082)','Series pair, negligible load current'],
       ['Current divider','I\u2081 = I R\u2082/(R\u2081+R\u2082)','Two parallel branches'],
       ['Star to delta','R_d = 3 R_s','Balanced three-element conversion only']],
      [TW*.24,TW*.30,TW*.46])

    o+=_ref('Capacitance, inductance and transients',
      'Energy storage and the exponential response that follows from it. Time constants assume a '
      'single storage element and a single resistance.',
      ['Relationship','Expression','When it applies'],
      [['Charge stored','Q = C V','Any capacitor at any instant'],
       ['Capacitor energy','E = \u00bd C V\u00b2','Energy stored in the electric field'],
       ['Capacitors in parallel','C = C\u2081 + C\u2082 + ...','Same voltage across each'],
       ['Capacitors in series','1/C = 1/C\u2081 + 1/C\u2082 + ...','Same charge on each'],
       ['Resistive-capacitive constant','\u03c4 = R C','Single resistance and capacitance'],
       ['Charging','v = V(1 - e^(-t/\u03c4))','Step applied to an initially discharged capacitor'],
       ['Discharging','v = V e^(-t/\u03c4)','No source, initial voltage V'],
       ['Induced voltage','e = -L (di/dt)','Self-inductance opposing current change'],
       ['Inductor energy','E = \u00bd L I\u00b2','Energy stored in the magnetic field'],
       ['Resistive-inductive constant','\u03c4 = L / R','Single inductance and resistance'],
       ['Practical settling','5\u03c4','Within one per cent of the final value']],
      [TW*.26,TW*.28,TW*.46])

    o+=_ref('Alternating quantities, impedance and power',
      'Sinusoidal steady state. Root-mean-square values are assumed unless stated otherwise, and '
      'the form factors given apply to sine waves only.',
      ['Relationship','Expression','When it applies'],
      [['Period and frequency','T = 1 / f','Any periodic waveform'],
       ['Angular frequency','\u03c9 = 2\u03c0 f','Sinusoidal quantities'],
       ['Root-mean-square value','V_rms = V_pk / \u221a2','Sine waves only'],
       ['Average value','V_av = 0.637 V_pk','Rectified sine, half cycle'],
       ['Inductive reactance','X_L = 2\u03c0 f L','Ideal inductor'],
       ['Capacitive reactance','X_C = 1/(2\u03c0 f C)','Ideal capacitor'],
       ['Series impedance','Z = \u221a(R\u00b2 + X\u00b2)','Series resistance and net reactance'],
       ['Phase angle','\u03c6 = arctan(X / R)','Series circuit'],
       ['Power factor','pf = cos \u03c6 = P / S','Sinusoidal conditions'],
       ['True power','P = V I cos \u03c6','Power converted to another form'],
       ['Apparent power','S = V I','Determines conductor and supply rating'],
       ['Reactive power','Q = V I sin \u03c6','Power exchanged with storage elements']],
      [TW*.26,TW*.28,TW*.46])

    o+=_ref('Resonance and filters',
      'The frequency at which reactances cancel, and the single-stage filter relationships.',
      ['Relationship','Expression','When it applies'],
      [['Resonant frequency','f\u2080 = 1/(2\u03c0 \u221a(L C))','Series or parallel, lightly damped'],
       ['Condition at resonance','X_L = X_C','Definition of resonance'],
       ['Series resonance impedance','Z = R','Reactances cancel, current is maximum'],
       ['Quality factor','Q = 2\u03c0 f\u2080 L / R','Series resonant circuit'],
       ['Bandwidth','BW = f\u2080 / Q','Between the half-power points'],
       ['Voltage magnification','V_L = Q V_in','Across either reactive element at resonance'],
       ['Filter cut-off','f_c = 1/(2\u03c0 R C)','Single-stage resistive-capacitive filter'],
       ['Half-power point','0.707 of maximum','Defines the cut-off frequency']],
      [TW*.26,TW*.28,TW*.46])

    o+=_ref('Magnetism, transformers and machines',
      'Magnetic circuit quantities and the machine relationships that follow from them.',
      ['Relationship','Expression','When it applies'],
      [['Magnetomotive force','F = N I','Coil of N turns carrying current I'],
       ['Flux density','B = \u03a6 / A','Uniform flux through area A'],
       ['Induced voltage','e = -N (d\u03a6/dt)','Faraday, flux linking N turns'],
       ['Force on a conductor','F = B I L','Conductor perpendicular to the field'],
       ['Turns ratio','V\u2081/V\u2082 = N\u2081/N\u2082','Ideal transformer, no losses'],
       ['Current ratio','I\u2081/I\u2082 = N\u2082/N\u2081','Ideal transformer, power conserved'],
       ['Impedance ratio','Z\u2081/Z\u2082 = (N\u2081/N\u2082)\u00b2','Impedance referred across a transformer'],
       ['Synchronous speed','n_s = 120 f / p','Alternating machine, p poles, speed in rev/min'],
       ['Slip','s = (n_s - n)/n_s','Induction machine running below synchronous speed'],
       ['Efficiency','\u03b7 = P_out / P_in','Any machine, consistent units']],
      [TW*.26,TW*.28,TW*.46])

    o+=[PageBreak()]
    o+=_ref('Electronics and conversion',
      'Semiconductor, amplifier, logic and converter relationships.',
      ['Relationship','Expression','When it applies'],
      [['Diode forward drop','\u2248 0.7 V silicon, 0.3 V germanium','Conducting, order of magnitude'],
       ['Half-wave ripple frequency','f_r = f','One pulse per supply cycle'],
       ['Full-wave ripple frequency','f_r = 2 f','Bridge or centre-tapped rectifier'],
       ['Reservoir capacitor ripple','V_r \u2248 I / (f_r C)','Light ripple approximation'],
       ['Transistor current gain','\u03b2 = I_C / I_B','Active region, common emitter'],
       ['Saturation condition','I_B > I_C / \u03b2','Transistor used as a switch'],
       ['Inverting amplifier gain','A = -R_f / R_in','Ideal operational amplifier'],
       ['Non-inverting gain','A = 1 + R_f / R_g','Ideal operational amplifier'],
       ['Converter steps','2\u207f','Converter of n bits'],
       ['Quantisation step','V_range / 2\u207f','Uniform converter'],
       ['Regulator dissipation','P = (V_in - V_out) I','Series linear regulator']],
      [TW*.26,TW*.30,TW*.44])

    o+=_ref('Three-phase systems',
      'Balanced three-phase relationships. All voltages and currents are root-mean-square values.',
      ['Relationship','Expression','When it applies'],
      [['Star voltage relation','V_line = \u221a3 V_phase','Balanced star connection'],
       ['Star current relation','I_line = I_phase','Balanced star connection'],
       ['Delta voltage relation','V_line = V_phase','Balanced delta connection'],
       ['Delta current relation','I_line = \u221a3 I_phase','Balanced delta connection'],
       ['Three-phase power','P = \u221a3 V_L I_L cos \u03c6','Balanced load, either connection'],
       ['Apparent power','S = \u221a3 V_L I_L','Balanced load'],
       ['Neutral current','zero','Balanced linear load in star']],
      [TW*.26,TW*.28,TW*.46])

    o+=_ref('Safety and fault clearance',
      'Relationships used in assessing protection and shock risk.',
      ['Relationship','Expression','When it applies'],
      [['Body current','I = V_contact / Z_body','Order-of-magnitude shock assessment'],
       ['Earth fault loop current','I_f = V / Z_loop','Fault current available to operate the device'],
       ['Joint resistance from loss','R = V_lost / I','Measured across a joint while on load'],
       ['Power lost in a joint','P = I\u00b2 R','Assessing whether a joint will overheat'],
       ['Permitted voltage drop','V_drop = percentage \u00d7 V_supply','Conductor adequacy over the route'],
       ['Starting current','I_start = k \u00d7 I_FL','Sizing protection for motors and transformers']],
      [TW*.26,TW*.30,TW*.44])

    o+=[PageBreak()]
    o+=_ref('SI units and prefixes',
      'The units used throughout the book and the prefixes applied to them. Writing the unit '
      'beside every number is the cheapest error check available.',
      ['Quantity','Symbol','Unit','Unit symbol'],
      [['Charge','Q','coulomb','C'],['Current','I','ampere','A'],
       ['Voltage','V','volt','V'],['Resistance','R','ohm',OH],
       ['Conductance','G','siemens','S'],['Capacitance','C','farad','F'],
       ['Inductance','L','henry','H'],['Reactance','X','ohm',OH],
       ['Impedance','Z','ohm',OH],['Frequency','f','hertz','Hz'],
       ['Power, true','P','watt','W'],['Power, apparent','S','volt-ampere','VA'],
       ['Power, reactive','Q','volt-ampere reactive','var'],
       ['Energy','E','joule','J'],['Magnetic flux','\u03a6','weber','Wb'],
       ['Flux density','B','tesla','T'],['Temperature','T','kelvin or degree Celsius','K, '+DEG+'C']],
      [TW*.30,TW*.14,TW*.34,TW*.22])

    o+=_ref('Prefixes',
      'Prefixes in common electrical use, with the multiplier each represents.',
      ['Prefix','Symbol','Multiplier','Typical electrical use'],
      [['giga','G','10\u2079','Gigahertz clock and radio frequencies'],
       ['mega','M','10\u2076','Megohm insulation resistance'],
       ['kilo','k','10\u00b3','Kilovolt distribution, kilohm resistors'],
       ['unity','\u2014','1','Volts, amperes, ohms'],
       ['milli','m','10\u207b\u00b3','Milliampere shock thresholds, millihenry coils'],
       ['micro',MU,'10\u207b\u2076','Microfarad capacitors, microvolt signals'],
       ['nano','n','10\u207b\u2079','Nanofarad film capacitors, nanosecond delays'],
       ['pico','p','10\u207b\u00b9\u00b2','Picofarad stray capacitance']],
      [TW*.18,TW*.14,TW*.20,TW*.48])

    o+=_ref('Reading a value from a number and a prefix',
      'The commonest arithmetic errors in electrical work are prefix errors, not algebra errors. '
      'These conversions are worth being able to do without hesitation.',
      ['Written','Means','In base units','Common context'],
      [['4k7','4.7 k'+OH,'4700 '+OH,'Resistor marking without a decimal point'],
       ['100n','100 nF','0.0000001 F','Film capacitor marking'],
       ['470'+MU,'470 '+MU+'F','0.00047 F','Electrolytic reservoir capacitor'],
       ['2M2','2.2 M'+OH,'2200000 '+OH,'High-value bias resistor'],
       ['15mH','15 millihenry','0.015 H','Small choke or filter inductor'],
       ['30mA','30 milliampere','0.03 A','Residual current device rating'],
       ['400V','400 volt','400 V','Three-phase line voltage'],
       ['1.5kW','1.5 kilowatt','1500 W','Small motor rating']],
      [TW*.14,TW*.22,TW*.24,TW*.40])


    o+=[PageBreak()]
    o+=_ref('North American & industrial voltage systems',
      'Standard nominal system voltages, phase configurations, and typical conductor identification used in commercial and industrial installations.',
      ['System','Configuration','Line-to-Line','Line-to-Neutral','Typical Phase Identification'],
      [['120/240 V','1\u03c6, 3-wire center-tapped','240 V','120 V','Black (L1), Red (L2), White (N), Green (EGC)'],
       ['208Y/120 V','3\u03c6, 4-wire wye','208 V','120 V','Black (A), Red (B), Blue (C), White (N), Green (EGC)'],
       ['240/120 V High-Leg','3\u03c6, 4-wire delta','240 V','120 V (A,C) / 208 V (B)','Black (A), Orange High-Leg (B), Blue (C), White (N)'],
       ['480Y/277 V','3\u03c6, 4-wire wye','480 V','277 V','Brown (A), Orange (B), Yellow (C), Grey (N), Green (EGC)'],
       ['480 V Delta','3\u03c6, 3-wire ungrounded/corner','480 V','\u2014','Brown (A), Orange (B), Yellow (C), Green (EGC)'],
       ['24 V DC Control','Class 2 / PELV / SELV','24 V DC','0 V common','Blue (+24 V DC), White/Blue or Blue/White (0 V DC Common)'],
       ['120 V AC Control','Control transformer secondary','120 V AC','120 V to X2','Red (ungrounded hot), White (grounded X2 common)']],
      [TW*.18,TW*.22,TW*.13,TW*.16,TW*.31])

    o+=_ref('Copper conductor sizing, DC resistance and reference ampacity',
      ' representative copper conductor data at 75 \u00b0C termination rating (THWN / XHHW) and uncoated DC resistance per 1000 ft (305 m) at 20 \u00b0C. Always verify against the current code table and derating rules.',
      ['Size (AWG / kcmil)','Area (mm\u00b2)','DC Resistance (\u03a9 / 1000 ft)','60 \u00b0C Rating (A)','75 \u00b0C Rating (A)','90 \u00b0C Rating (A)','Typical Field Application'],
      [['18 AWG','0.82','6.51','\u2014','7 A (control)','14 A','Panelboard PLC I/O and 4\u201320 mA signal wiring'],
       ['16 AWG','1.31','4.09','\u2014','10 A (control)','18 A','Control circuits, solenoid valves, pushbuttons'],
       ['14 AWG','2.08','2.57','15 A','20 A (15 A max OCPD)','25 A','15 A lighting and control branch circuits'],
       ['12 AWG','3.31','1.62','20 A','25 A (20 A max OCPD)','30 A','20 A general receptacle and plant branch circuits'],
       ['10 AWG','5.26','1.02','30 A','35 A (30 A max OCPD)','40 A','30 A small motors, heaters, long 20 A home runs'],
       ['8 AWG','8.37','0.641','40 A','50 A','55 A','40\u201350 A feeders, welders, 15\u201325 HP 480 V motors'],
       ['6 AWG','13.3','0.403','55 A','65 A','75 A','60 A subpanels, 30 HP 480 V motor branches'],
       ['4 AWG','21.2','0.253','70 A','85 A','95 A','80\u201390 A feeders, 40\u201350 HP 480 V motors'],
       ['2 AWG','33.6','0.159','95 A','115 A','130 A','100\u2013115 A distribution feeders'],
       ['1/0 AWG','53.5','0.100','125 A','150 A','170 A','150 A feeders, 100 HP 480 V motor branches'],
       ['2/0 AWG','67.4','0.0795','145 A','175 A','195 A','175\u2013200 A main services and MCC feeders'],
       ['4/0 AWG','107.2','0.0500','195 A','230 A','260 A','225 A bus feeders, transformer secondaries'],
       ['250 kcmil','127','0.0431','215 A','255 A','290 A','250 A industrial sub-feeders'],
       ['500 kcmil','253','0.0216','320 A','380 A','430 A','400 A parallel switchgear and transformer feeds']],
      [TW*.15,TW*.09,TW*.17,TW*.11,TW*.14,TW*.11,TW*.23])

    o+=[PageBreak()]
    o+=_ref('Three-phase squirrel-cage motor reference currents and starter sizing',
      'Typical full-load currents (FLA) for design estimation of standard 4-pole (1800 rev/min synchronous) three-phase induction motors. Use nameplate FLA for overload relay setting and these table values for branch conductor and short-circuit protection sizing.',
      ['Horsepower (HP)','Approx. kW','208 V FLA (A)','230 V FLA (A)','460 V FLA (A)','NEMA Starter Size (460 V)','Min. 75 \u00b0C Wire (460 V, 125%)'],
      [['1 HP','0.75 kW','4.6 A','4.2 A','2.1 A','Size 00 / 0','14 AWG (2.6 A)'],
       ['2 HP','1.5 kW','7.5 A','6.8 A','3.4 A','Size 0','14 AWG (4.3 A)'],
       ['3 HP','2.2 kW','10.6 A','9.6 A','4.8 A','Size 0','14 AWG (6.0 A)'],
       ['5 HP','3.7 kW','16.7 A','15.2 A','7.6 A','Size 0','14 AWG (9.5 A)'],
       ['7.5 HP','5.5 kW','24.2 A','22 A','11 A','Size 1','14 AWG (13.8 A)'],
       ['10 HP','7.5 kW','30.8 A','28 A','14 A','Size 1','12 AWG (17.5 A)'],
       ['15 HP','11 kW','46.2 A','42 A','21 A','Size 2','10 AWG (26.3 A)'],
       ['20 HP','15 kW','59.4 A','54 A','27 A','Size 2','10 AWG (33.8 A)'],
       ['25 HP','18.5 kW','74.8 A','68 A','34 A','Size 2','8 AWG (42.5 A)'],
       ['30 HP','22 kW','88 A','80 A','40 A','Size 3','8 AWG (50.0 A)'],
       ['40 HP','30 kW','114 A','104 A','52 A','Size 3','6 AWG (65.0 A)'],
       ['50 HP','37 kW','143 A','130 A','65 A','Size 3','4 AWG (81.3 A)'],
       ['75 HP','55 kW','211 A','192 A','96 A','Size 4','1 AWG (120 A)'],
       ['100 HP','75 kW','273 A','248 A','124 A','Size 4','2/0 AWG (155 A)']],
      [TW*.14,TW*.11,TW*.12,TW*.12,TW*.12,TW*.18,TW*.21])

    o+=_ref('Industrial instrumentation: 4\u201320 mA loop scaling and temperature sensors',
      'Standard 4\u201320 mA analog loop checkpoints, 250 \u03a9 precision shunt conversions, and Pt100 RTD resistance vs. temperature reference.',
      ['Percent of Span','Loop Current (mA)','Drop across 250 \u03a9','12-Bit ADC Count (0\u20134095)','Pt100 RTD Temp (\u00b0C)','Pt100 Resistance (\u03a9)','Diagnostic Meaning'],
      [['< 3.8 mA Fault','0.0 \u2013 3.8 mA','0.00 \u2013 0.95 V','0','Open / Burnout','\u2014','Broken wire, blown fuse, or dead transmitter'],
       ['0.0 % (LRV)','4.00 mA','1.000 V','819 (or 0 scaled)','0 \u00b0C','100.00 \u03a9','Live zero: confirms loop continuity at 0 %'],
       ['25.0 %','8.00 mA','2.000 V','1638 (1024 scaled)','25 \u00b0C','109.73 \u03a9','Quarter scale checkpoint'],
       ['50.0 %','12.00 mA','3.000 V','2457 (2048 scaled)','50 \u00b0C','119.40 \u03a9','Mid-scale calibration checkpoint'],
       ['75.0 %','16.00 mA','4.000 V','3276 (3072 scaled)','100 \u00b0C','138.51 \u03a9','Three-quarter scale checkpoint'],
       ['100.0 % (URV)','20.00 mA','5.000 V','4095','200 \u00b0C','175.86 \u03a9','Full scale output'],
       ['> 20.5 mA Fault','20.5 \u2013 24 mA','> 5.125 V','4095 (clipped)','Short / Overrange','\u2014','Sensor upscale burnout or shorted loop']],
      [TW*.14,TW*.15,TW*.13,TW*.18,TW*.13,TW*.13,TW*.14])

    o+=[PageBreak()]
    o+=_ref('Resistor color code and conduit bending field multipliers',
      'Standard EIA resistor color bands alongside conduit offset multipliers and shrinkage per inch of offset depth.',
      ['Color Band','Digit','Multiplier','Tolerance','Conduit Bend Angle','Offset Multiplier (Csc)','Shrinkage per Inch of Depth'],
      [['Black / Brown','0 / 1','\u00d71 / \u00d710','\u2014 / \u00b11 %','10\u00b0 offset','\u00d7 6.0','1/16 in (0.063 in)'],
       ['Red / Orange','2 / 3','\u00d7100 / \u00d71 k','\u00b12 % / \u2014','22.5\u00b0 offset','\u00d7 2.6','3/16 in (0.188 in)'],
       ['Yellow / Green','4 / 5','\u00d710 k / \u00d7100 k','\u2014 / \u00b10.5 %','30\u00b0 offset (standard)','\u00d7 2.0','1/4 in (0.250 in)'],
       ['Blue / Violet','6 / 7','\u00d71 M / \u00d710 M','\u00b10.25 % / \u00b10.1 %','45\u00b0 offset','\u00d7 1.414','3/8 in (0.375 in)'],
       ['Grey / White','8 / 9','\u00d7100 M / \u00d71 G','\u2014','60\u00b0 offset','\u00d7 1.155','1/2 in (0.500 in)'],
       ['Gold / Silver','\u2014','\u00d70.1 / \u00d70.01','\u00b15 % / \u00b110 %','3-Point Saddle (45\u00b0\u201322.5\u00b0)','Center = 2\u00d7H, Side = 2.5\u00d7H','3/16 in per in of height']],
      [TW*.16,TW*.09,TW*.15,TW*.14,TW*.18,TW*.14,TW*.14])

    o+=[PageBreak()]
    o+=_ref('Measurement checklist',
      'Applied before every measurement. The sequence prevents the two commonest errors: '
      'measuring the wrong quantity, and disturbing the circuit by measuring it.',
      ['Stage','Check','Why it matters'],
      [['Before','Identify the quantity you actually need','Voltage, current and resistance answer different questions'],
       ['Before','Write the expected value','Any reading looks plausible without a prediction'],
       ['Before','Select the function and range','Wrong function can damage the instrument or the circuit'],
       ['Before','Prove the instrument on a known source','An instrument that reads zero may be faulty, not the circuit'],
       ['Before','Inspect leads and probes','Damaged insulation is the commonest instrument hazard'],
       ['During','Identify the reference point','A voltage without a reference is meaningless'],
       ['During','Consider the loading effect','A low-impedance meter changes a high-impedance circuit'],
       ['During','Measure under the relevant load','Many faults appear only when current flows'],
       ['After','Compare with the expected value','Disagreement is information, not an inconvenience'],
       ['After','Prove the instrument again','Confirms it was working during the measurement'],
       ['After','Record the reading','A measurement not recorded will be taken again']],
      [TW*.14,TW*.36,TW*.50])

    o+=_ref('Safe isolation sequence',
      'The sequence is not negotiable and the order is the point. Each step depends on the one '
      'before it being complete.',
      ['Step','Action','Reason'],
      [['1','Identify the circuit and its source','Isolating the wrong circuit is worse than not isolating'],
       ['2','Obtain permission to isolate','Other people may depend on the circuit'],
       ['3','Isolate at the correct point','Switching the load off is not isolation'],
       ['4','Secure the isolation, lock off, retain the key','Prevents re-energising by another person'],
       ['5','Post a warning notice','Tells others why the circuit is off'],
       ['6','Prove the test instrument on a known source','Establishes the instrument works now'],
       ['7','Test all conductor combinations','A single test can miss a live conductor'],
       ['8','Re-prove the instrument','Confirms it still worked during the test'],
       ['9','Address stored energy','Capacitors and standing charge remain after isolation'],
       ['10','Begin work','Only now is the circuit safe to work on']],
      [TW*.08,TW*.38,TW*.54])

    o+=[PageBreak()]
    o+=_ref('Glossary A to I',
      'Terms as used in this book. Where general usage is looser, the definition here is the one '
      'intended in these chapters.',
      ['Term','Meaning'],
      [['Admittance','The reciprocal of impedance.'],
       ['Alternating current','Current that reverses direction periodically.'],
       ['Ampere','The unit of current, one coulomb per second.'],
       ['Apparent power','The product of root-mean-square voltage and current, in volt-amperes.'],
       ['Bandwidth','The frequency span between the half-power points of a resonant circuit.'],
       ['Capacitance','The charge stored per unit voltage applied.'],
       ['Conductance','The reciprocal of resistance.'],
       ['Coulomb','The unit of charge.'],
       ['Cut-off frequency','The frequency at which a filter output falls to 0.707 of its maximum.'],
       ['Derating','Reducing a conductor\u2019s permitted current for its installed conditions.'],
       ['Dielectric','The insulating material between capacitor plates.'],
       ['Differential','The width of the switching band in an on-off controller.'],
       ['Duty cycle','The fraction of a period for which a switched output is on.'],
       ['Eddy current','Circulating current induced in a conducting core, causing loss.'],
       ['Efficiency','Output power divided by input power.'],
       ['Electromotive force','The voltage generated by a source, before internal loss.'],
       ['Error','In control, the set point minus the process variable.'],
       ['Farad','The unit of capacitance.'],
       ['Flux density','Magnetic flux per unit area, in tesla.'],
       ['Form factor','The ratio of root-mean-square to average value of a waveform.'],
       ['Henry','The unit of inductance.'],
       ['Hysteresis','Lagging of a magnetic or control response behind its cause.'],
       ['Impedance','The total opposition to alternating current, combining resistance and reactance.'],
       ['Inductance','The property producing a voltage in opposition to a change of current.'],
       ['Inrush current','The brief high current drawn when a load is first energised.'],
       ['Insulation resistance','The resistance of insulation between conductors or to earth.']],
      [TW*.24,TW*.76])

    o+=[PageBreak()]
    o+=_ref('Glossary J to R',None if False else
      'Continued. Cross-references are to the chapter in which the term is developed.',
      ['Term','Meaning'],
      [['Joule','The unit of energy.'],
       ['Kirchhoff\u2019s current law','The sum of currents into a node equals the sum leaving it.'],
       ['Kirchhoff\u2019s voltage law','The sum of voltages around a closed loop is zero.'],
       ['Load','The element or circuit that converts supplied electrical energy.'],
       ['Magnetomotive force','The product of turns and current driving flux in a magnetic circuit.'],
       ['Node','A junction at which two or more circuit elements meet.'],
       ['Offset','In control, the steady error left by proportional-only action.'],
       ['Ohm','The unit of resistance.'],
       ['Open circuit','A break in a path, carrying no current.'],
       ['Overcurrent device','A fuse or circuit breaker interrupting excessive current.'],
       ['Peak value','The maximum instantaneous value of a waveform.'],
       ['Permeability','The ease with which a material carries magnetic flux.'],
       ['Phase angle','The angular difference between voltage and current waveforms.'],
       ['Power factor','The cosine of the phase angle; true power divided by apparent power.'],
       ['Process variable','The measured value of the quantity under control.'],
       ['Protective conductor','A conductor provided to carry fault current safely to earth.'],
       ['Quality factor','A measure of the sharpness of resonance.'],
       ['Quantisation step','The input change corresponding to one converter count.'],
       ['Reactance','The opposition to alternating current offered by inductance or capacitance.'],
       ['Reactive power','Power exchanged with storage elements, in volt-amperes reactive.'],
       ['Rectification','Conversion of alternating to unidirectional current.'],
       ['Residual current device','A device operating on an imbalance between live and neutral current.'],
       ['Resistivity','The resistance of unit length and unit area of a material.'],
       ['Resonance','The condition in which inductive and capacitive reactance cancel.'],
       ['Ripple','The residual alternating component on a rectified and smoothed supply.'],
       ['Root-mean-square','The equivalent steady value producing the same heating effect.']],
      [TW*.24,TW*.76])

    o+=[PageBreak()]
    o+=_ref('Glossary S to Z',
      'Continued.',
      ['Term','Meaning'],
      [['Saturation','The condition in which a core carries little additional flux, or a transistor is fully on.'],
       ['Series','Elements connected so that the same current passes through each.'],
       ['Set point','The value a controlled quantity is required to reach.'],
       ['Short circuit','An unintended low-resistance path carrying excessive current.'],
       ['Slip','The fractional difference between synchronous and actual rotor speed.'],
       ['Star connection','A three-phase arrangement with one end of each winding at a common point.'],
       ['Delta connection','A three-phase arrangement with the windings connected end to end in a loop.'],
       ['Synchronous speed','The rotational speed of the rotating field in an alternating machine.'],
       ['Tesla','The unit of magnetic flux density.'],
       ['Thermistor','A resistor whose resistance varies strongly with temperature.'],
       ['Thermocouple','A junction of dissimilar metals producing a temperature-dependent voltage.'],
       ['Time constant','The product of resistance and capacitance, or inductance over resistance.'],
       ['Transducer','A device converting one physical quantity into another.'],
       ['Transformer','A device transferring energy between windings by mutual induction.'],
       ['Transient','The temporary response of a circuit between two steady states.'],
       ['True power','Power actually converted to another form, in watts.'],
       ['Turns ratio','The ratio of primary to secondary turns in a transformer.'],
       ['Volt','The unit of potential difference, one joule per coulomb.'],
       ['Voltage drop','The voltage lost along a conductor carrying current.'],
       ['Watt','The unit of power, one joule per second.'],
       ['Weber','The unit of magnetic flux.']],
      [TW*.24,TW*.76])

    o+=_ref('Where to go next',
      'Suggested routes through the material for different purposes, using chapters already in '
      'this book.',
      ['Purpose','Route','Focus'],
      [['Grounding in fundamentals','Chapters 1 to 4','Models, conservation laws, networks and transients'],
       ['Alternating current competence','Chapters 6 to 8','Waveforms, impedance, power factor, resonance'],
       ['Machines and power','Chapters 9 to 11 and 17','Magnetism, transformers, motors, three-phase'],
       ['Electronics','Chapters 12 to 16','Diodes, transistors, amplifiers, logic, supplies'],
       ['Field practice','Chapters 18 to 20','Safety, fault paths, control, diagnosis'],
       ['Measurement discipline','The practical activity in every chapter','Prediction, measurement, explanation']],
      [TW*.28,TW*.30,TW*.42])

    o+=[panel('A closing note',
      ['The method in the final chapter is the most portable thing in this book. Equations can be '
       'looked up and code limits change between editions, but the habit of writing the expected '
       'value before taking the measurement, of dividing the circuit rather than guessing at it, '
       'and of recording what was found, will serve on every circuit you ever meet.'],accent=MEAS)]
    return o
