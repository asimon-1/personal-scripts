import os
import sys


def rotate(l, n):
    """Rotates list l by n elements"""
    return l[n:] + l[:n]


def reverse(l, n):
    """Reverses the first n elements of a list l"""
    return l[:n][::-1] + l[n:]

# Get the base directory. Input file must be in the same directory.
BASE_DIR = os.path.dirname(sys.argv[0])

# Read the input file
with open(BASE_DIR + '\\' + '2017_day_10_input.txt') as f:
    raw = f.read()

inputs = [int(s) for s in raw.split(',')]

ring_size = 256
skip = 0
total_skipped = 0

ring = [i for i in range(ring_size)]


for length in inputs:
    print(ring)
    ring = reverse(ring, length)
    ring = rotate(ring, length + skip)
    total_skipped += length + skip
    skip += 1

ring = rotate(ring, (total_skipped % len(ring)))
print('\nFinal Ring')
print(ring)
print(ring[0] * ring[1])
