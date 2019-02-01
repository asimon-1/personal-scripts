import os
import glob
import re

DIR = "os.path.join(os.getcwd(), "Test")"

files = glob.glob(os.path.join(DIR, "*"))

pattern = r"(.*\\)\S+\. (.+\.pdf)"
regex = re.compile(pattern)

for f in files:
    print(f)
    match = regex.search(f)
    if match:
        new_name = match.group(1) + match.group(2)
        os.rename(f, match.group(1) + match.group(2))