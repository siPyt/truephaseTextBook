# -*- coding: utf-8 -*-
"""Keeps existing cover + 4 photos, adds motor.jpeg (Ch 11) and receptacle.jpeg (Ch 18), and builds the PDF."""
import sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ren = (ROOT / "render.py").read_text(encoding="utf-8")

# Find any long/truncated switchgear filename on disk just in case
sw_files = ["switchgear.jpg", "switchgear.jpeg", "ch17.jpg", "ch17.jpeg"] + [
    p.name for p in ROOT.glob("industrial_electrical_control_panels*") if p.is_file()
]

NEW_MAP = f"""CHAPTER_PHOTOS = {{
    3: (
        ["ch3.jpg", "ch3.jpeg", "panel.jpg", "panel.jpeg", "image_87dbcf2a.jpg"],
        "FIELD PRACTICE \u00b7 Parallel branch circuits, neutral bus termination, and equipment grounding conductors in a 120/240 V distribution panel.",
        2.35 * inch
    ),
    10: (
        ["ch10.jpg", "ch10.jpeg", "substation.jpg", "substation.jpeg", "high-voltage_power_transformer_at_electrical_substation._high-voltage_power_transformer_and_electrical_substation_infrastructure_surrounded_by_transmission_equipment_and_power_lines..jpg"],
        "FIELD PRACTICE \u00b7 High-voltage three-phase substation power transformer with high-voltage bushings, forced-air radiator fans, and oil conservator tank.",
        2.55 * inch
    ),
    11: (
        ["motor.jpeg", "motor.jpg", "ch11.jpg", "ch11.jpeg"],
        "FIELD PRACTICE \u00b7 Industrial induction motor installation, frame cooling ribs, and terminal box connection.",
        2.55 * inch
    ),
    17: (
        {sw_files!r},
        "FIELD PRACTICE \u00b7 Industrial three-phase low-voltage switchgear lineup with draw-out air circuit breakers, status indicators, and local metering.",
        3.25 * inch
    ),
    18: (
        ["receptacle.jpeg", "receptacle.jpg", "ch18.jpg", "ch18.jpeg"],
        "FIELD PRACTICE \u00b7 Branch-circuit receptacle termination, polarized line/neutral conductors, and equipment grounding path.",
        2.55 * inch
    ),
    20: (
        ["ch20.jpg", "ch20.jpeg", "penthouse.jpg", "penthouse.jpeg", "image_68fe44ed.jpg"],
        "FIELD PRACTICE \u00b7 Clean installation, accurate documentation, and disciplined diagnostic habits build lasting professional competence.",
        2.35 * inch
    ),
}}"""

start_idx = ren.find("CHAPTER_PHOTOS = {")
end_idx = ren.find("\ndef photo_block(")
if start_idx != -1 and end_idx != -1:
    ren = ren[:start_idx] + NEW_MAP + "\n" + ren[end_idx:]
    (ROOT / "render.py").write_text(ren, encoding="utf-8")
    print("Mapped motor.jpeg -> Ch 11 and receptacle.jpeg -> Ch 18 while keeping all existing images.")
else:
    raise SystemExit("Could not find CHAPTER_PHOTOS block in render.py — run add_photos.py first.")

print("Rebuilding PDF...")
subprocess.run([sys.executable, str(ROOT / "build_all.py")], check=True)
print("Done! Opening TruePhase_Electrical_Theory_Textbook.pdf...")