import os
import re
import sys

# Get the base directory. Input file must be in the same directory.
BASE_DIR = os.path.dirname(sys.argv[0])

# Read the input file
with open(BASE_DIR + '\\' + '2017_day_9_input_test.txt') as f:
    raw = f.read()

input_stream = [raw]

# Remove negated characters
pattern = r"!." # Note that double exclaimation points are removed left-to-right, so !!a means the a is not negated.
regex_negated = re.compile(pattern)
input_stream.append(regex_negated.sub('', input_stream[-1]))

# Remove garbage
pattern = r"<.*?>"
regex_garbage = re.compile(pattern)
input_stream.append(regex_garbage.sub('', input_stream[-1]))

# Remove other characters
pattern = r"[^\{^\}]"
regex_other = re.compile(pattern)
input_stream.append(regex_other.sub('', input_stream[-1]))

# Count groups
pattern = r"\{.*?\}"
regex_group = re.compile(pattern)
# How do I grab all of the outer groups?

print(raw)
for i in input_stream: print(i)
