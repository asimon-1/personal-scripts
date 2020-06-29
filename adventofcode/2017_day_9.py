import os
import re
import sys

# From https://stackoverflow.com/a/4285211
def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == "{":
            stack.append(i)
        elif c == "}" and stack:
            start = stack.pop()
            yield (len(stack) + 1, string[start + 1 : i])


# Get the base directory. Input file must be in the same directory.
BASE_DIR = os.path.dirname(sys.argv[0])

# Read the input file
with open(BASE_DIR + "\\" + "2017_day_9_input.txt") as f:
    raw = f.read()

input_stream = [raw]

# Remove negated characters
pattern = r"!."  # Note that double exclaimation points are removed left-to-right, so !!a means the a is not negated.
regex_negated = re.compile(pattern)
input_stream.append(regex_negated.sub("", input_stream[-1]))

# Remove garbage
pattern = r"<(.*?)>"
regex_garbage = re.compile(pattern)
print(
    "Total Garbage Removed: {}".format(
        len("".join(regex_garbage.findall(input_stream[-1])))
    )
)
input_stream.append(regex_garbage.sub("", input_stream[-1]))

# Remove other characters
pattern = r"[^\{^\}]"
regex_other = re.compile(pattern)
input_stream.append(regex_other.sub("", input_stream[-1]))

# Count groups
input_stream.append(list(parenthetic_contents(input_stream[-1])))
score = sum([i[0] for i in input_stream[-1]])

print("Score: {}".format(score))
