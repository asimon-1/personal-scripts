import os
import re
import sys

# Get the base directory. Input file must be in the same directory.
BASE_DIR = os.path.dirname(sys.argv[0])

# Read the input file
with open(BASE_DIR + '\\' + '2017_day_8_input.txt') as f:
    raw = f.read()

# Do some preprocessing and formatting
input_list = [p.replace(',', '').replace('inc', '+=').replace('dec', '-=') for p in raw.split('\n')]
words = [p.split(' ')[0] for p in input_list]  # Assumes that every needed word is modified in the instructions at some point.
words = dict(zip(set(words), [0] * len(set(words))))  # Store word values in a dictionary.
for w in words:
    pattern = "(?<!.){}\s|\s{}\s".format(w, w)  # Look for matches at the beginning of the instruction or in the condition
    regex = re.compile(pattern)
    input_list = [regex.sub(' words[\'{}\']'.format(w), i) for i in input_list]  # Replace the words with their dictionary equivalent

# Split input into conditions and instructions
input_list = [p.split('if') for p in input_list]
conditions = [cond[1].strip() for cond in input_list]
instructions = [cond[0].strip() for cond in input_list]

max_value = 0
for cond, instr in zip(conditions, instructions):
    print("Condition: {}".format(cond))
    if eval(cond):  # Evaluate the condition and execute the corresponding instruction if it passes
        print("Condition Passed, Executing {}".format(instr))
        exec(instr)
        max_value = max(max_value, max(words.values()))  # Keep track of the largest value of all time
print('\n\nExecution Complete.')
print('All Time Maximum: {}'.format(max_value))
print('Current Maximum: {}'.format(max(words.values())))
