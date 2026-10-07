# Loaded by start.bat (IPYTHONDIR): makes %ask available in every notebook.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
get_ipython().run_line_magic("load_ext", "tutor")
