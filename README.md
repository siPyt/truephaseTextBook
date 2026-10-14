# TruePhase Electrical Theory textbook source

This archive contains the Python source used to generate the supplied textbook PDF.

## Build

From this directory, with Python 3 and ReportLab available:

```bash
python3 build_all.py
```

The build writes `TruePhase_Electrical_Theory_Textbook.pdf` in the current directory.

## Contents

- `engine.py` - ReportLab document engine, styles, page templates, tables, equation blocks, and vector-figure flowable
- `render.py` - chapter renderer
- `matter.py` - cover, contents, symbol key, reference section, glossary, and checklists
- `c01.py` through `c20.py` - authored chapter data
- `figures/figs.py` - vector figure definitions
- `figures/lib.py` - drawing primitives used by the figure definitions
- `build_all.py` - complete build entry point

The build uses the current compact-figure setting from the delivered revision.
