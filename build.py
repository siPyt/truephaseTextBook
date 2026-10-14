# -*- coding: utf-8 -*-
"""Master Build Pipeline for TruePhase Electrical Theory Textbook.
Runs all patch/upgrade scripts in order, compiles the PDF once, and opens it.
Add any future scripts to the PIPELINE list below.
"""
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF_PATH = ROOT / "TruePhase_Electrical_Theory_Textbook.pdf"

# ------------------------------------------------------------------
# Add or reorder any helper scripts here:
# ------------------------------------------------------------------
PIPELINE = [
    "fix_ansi.py",            # 1. US ANSI/IEEE 315 symbols (zigzag resistors, etc.)
    "add_photos.py",          # 2. Cover photo + base chapter photo engine
    "make_ultimate.py",       # 3. 5 Field Reference Master Tables + header/page fixes
    "fix_all_figs.py",        # 4. 100% pin-locked schematic coordinates
    "enable_auto_images.py",  # 5. Maps motor.jpeg, receptacle.jpeg & ch<N> auto-photos
]

def run_patch_without_rebuild(script_path: Path):
    """Executes a patch script's file updates without triggering redundant PDF builds."""
    code = script_path.read_text(encoding="utf-8")
    # Skip the intermediate build_all.py call inside individual patch scripts
    filtered_lines = [
        line for line in code.splitlines()
        if 'build_all.py' not in line
    ]
    cleaned_code = "\n".join(filtered_lines)
    exec(compile(cleaned_code, str(script_path), "exec"), {"__name__": "__main__", "__file__": str(script_path)})

def main():
    print("=" * 60)
    print(" TRUEPHASE MASTER BUILD PIPELINE")
    print("=" * 60)

    for script_name in PIPELINE:
        script_path = ROOT / script_name
        if script_path.exists():
            print(f"-> Applying {script_name}...")
            run_patch_without_rebuild(script_path)
        else:
            print(f"   [Skipping {script_name} - file not found]")

    print("\n-> Compiling final PDF (build_all.py)...")
    try:
        subprocess.run([sys.executable, str(ROOT / "build_all.py")], check=True)
    except subprocess.CalledProcessError:
        print("\n[!] ERROR: Could not write PDF. Make sure TruePhase_Electrical_Theory_Textbook.pdf is closed in your viewer and run 'python build.py' again.")
        sys.exit(1)

    print(f"\nSUCCESS! Built: {PDF_PATH.name}")
    if sys.platform == "win32" and PDF_PATH.exists():
        os.startfile(str(PDF_PATH))

if __name__ == "__main__":
    main()