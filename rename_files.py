import os
import glob
import re
import pathlib

WHATIF = True
DIR = pathlib.Path("C:/temp/video/_4")

files = [pathlib.Path(p) for p in glob.glob(str(DIR / "**/*.mp4"))]
print(str(DIR / "**/*.mp4"))

for f in files:
    new_name = DIR / f.name
    print(f"Renaming {f} to {new_name}")
    if not WHATIF:
        os.rename(f, new_name)
