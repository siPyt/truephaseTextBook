# -*- coding: utf-8 -*-
"""Transforms TruePhase Electrical Theory into the Ultimate Electrician & E/I&C Field Reference.
1. Fixes all 7 remaining schematic/header/blank-page glitches found in the 283-page PDF audit.
2. Auto-detects the Chapter 17 Switchgear photo even if Windows truncated the filename.
3. Adds 5 comprehensive Field & Bench Reference Master Tables to the Reference Section.
"""
import sys, glob, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGS = ROOT / "figures"

# ------------------------------------------------------------------
# 1. Fix symbolkey() in matter.py so Ch 1 Page 1 uses 'open' template (no 'SYMBOL KEY' header bleed)
#    AND remove the blank Page 272 in backmatter(), AND add the Ultimate Field Reference Tables!
# ------------------------------------------------------------------
mat = (ROOT / "matter.py").read_text(encoding="utf-8")

# Fix Symbol Key -> Chapter 1 page template transition
mat = mat.replace(
    "        o+=[Spacer(1,6),F(fn,cap,'',gh=46),Spacer(1,4)]\n    o.append(PageBreak())",
    "        o+=[Spacer(1,6),F(fn,cap,'',gh=46),Spacer(1,4)]\n    o+=[NextPageTemplate('open'),PageBreak()]"
)

# Remove the extra PageBreak() that caused the blank page 272
mat = mat.replace(
    "      [TW*.24,TW*.30,TW*.46])\n\n    o+=[PageBreak()]\n    o+=_ref('Capacitance, inductance and transients',",
    "      [TW*.24,TW*.30,TW*.46])\n\n    o+=_ref('Capacitance, inductance and transients',"
)

ULTIMATE_TABLES = r'''
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
'''

if "North American & industrial voltage systems" not in mat:
    mat = mat.replace(
        "    o+=[PageBreak()]\n    o+=_ref('Measurement checklist',",
        ULTIMATE_TABLES + "\n    o+=[PageBreak()]\n    o+=_ref('Measurement checklist',"
    )

(ROOT / "matter.py").write_text(mat, encoding="utf-8")

# ------------------------------------------------------------------
# 2. Fix the remaining schematic defects in figs.py & lib.py
# ------------------------------------------------------------------
for p in [ROOT / "figs.py", FIGS / "figs.py"]:
    if p.exists():
        ft = p.read_text(encoding="utf-8")
        # Fix Fig 2.3 (c2_bridge): Voltmeter colliding with R3
        old_bridge = '''def c2_bridge(d):
    _hd(d,43,"A NODE PAIR WORTH SOLVING TWICE")
    d.dc_supply(6,16,val="9 V"); d.wire((6,26),(6,36),(26,36))
    d.resistor(26,36,ref="R1",val="1 k"+OH); d.dot(36,36)
    d.wire((36,36),(36,30)); d.resistor(36,20,ref="R2",val="2.2 k"+OH,span=10,vert=True)
    d.wire((36,20),(36,8),(6,8),(6,16))
    d.wire((36,36),(56,36)); d.resistor(56,24,ref="R3",val="4.7 k"+OH,span=10,vert=True)
    d.wire((56,24),(56,8)); d.dot(56,8)
    d.wire((36,28),(48,28),color=MEAS,w=0.6); _meter(d,52,28,"V")
    d.ground(20,8)'''
        new_bridge = '''def c2_bridge(d):
    _hd(d,43,"A NODE PAIR WORTH SOLVING TWICE")
    d.dc_supply(8,14,val="9 V"); d.wire((8,22),(8,36),(24,36))
    d.resistor(24,36,ref="R1",val="1 k"+OH); d.wire((34,36),(38,36)); d.dot(38,36)
    d.wire((38,36),(38,28)); d.resistor(38,18,ref="R2",val="2.2 k"+OH,span=10,vert=True)
    d.wire((38,18),(38,8),(8,8),(8,14)); d.dot(38,8)
    d.wire((38,36),(68,36),(68,28)); d.resistor(68,18,ref="R3",val="4.7 k"+OH,span=10,vert=True)
    d.wire((68,18),(68,8),(38,8)); d.dot(68,8)
    d.dot(38,31); d.dot(68,31)
    d.wire((38,31),(49.8,31),color=MEAS,w=0.7); d.wire((56.2,31),(68,31),color=MEAS,w=0.7)
    _meter(d,53,31,"V")
    d.ground(22,8)'''
        ft = ft.replace(old_bridge, new_bridge)
        # Also catch any variant of c2_bridge
        ft = ft.replace(
            'd.wire((36,28),(48,28),color=MEAS,w=0.6); _meter(d,52,28,"V")',
            'd.wire((36,30),(44,30),color=MEAS,w=0.7); _meter(d,47.2,30,"V"); d.wire((50.4,30),(56,30),color=MEAS,w=0.7)'
        )

        # Fix Fig 7.1 & 7.2: Left-clipped "50 V, 50 Hz" and "2µfL" typo -> "2πfL"
        ft = ft.replace('d.ac_supply(10,24,val="50 V, 50 Hz"); d.wire((10,28),(10,34),(30,34))',
                        'd.ac_supply(16,24,val="50 V, 50 Hz"); d.wire((16,28),(16,34),(30,34))')
        ft = ft.replace('d.wire((62,34),(76,34),(76,8),(10,8),(10,20))',
                        'd.wire((60,34),(76,34),(76,8),(16,8),(16,20))')
        ft = ft.replace('2"+MU+"fL', '2\u03c0fL').replace('2"+MU+"fC', '2\u03c0fC')

        # Fix Fig 9.2 (c9_relay): Connect KA1 relay coil bottom wire cleanly to return
        ft = ft.replace('d.wire((32,30),(32,8),(6,8),(6,16))',
                        'd.wire((34.6,34.4),(34.6,8),(6,8),(6,16))')
        p.write_text(ft, encoding="utf-8")

# ------------------------------------------------------------------
# 3. Ensure Chapter 17 Switchgear photo is detected even with long/truncated filename
# ------------------------------------------------------------------
ren = (ROOT / "render.py").read_text(encoding="utf-8")
sw_matches = [p.name for p in ROOT.glob("industrial_electrical_control_panels*") if p.is_file()]
if sw_matches:
    ren = ren.replace(
        '["switchgear.jpg", "industrial_electrical_control_panels_installed_in_a_commercial_facility._low_voltage_switchgear_and_power_distribution_system_with_circuit_breakers_and_safety_warning_signs._modern_electrical_infrastructure_for_ind.jpg"]',
        str(["switchgear.jpg"] + sw_matches)
    )
(ROOT / "render.py").write_text(ren, encoding="utf-8")

print("Building Ultimate Edition PDF...")
subprocess.run([sys.executable, str(ROOT / "build_all.py")], check=True)
print("SUCCESS! Opening TruePhase_Electrical_Theory_Textbook.pdf...")