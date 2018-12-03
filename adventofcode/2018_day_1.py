from itertools import cycle

# Read inputs
with open('2018_day_1_input.txt') as f:
    lines = f.read().splitlines()
inputs = [int(l) for l in lines]

# Part 1 answer
print(sum(inputs))

# Part 2 answer
frequency = 0  # Current frequency
freq_dict = {'0': 1}  # Keeps track of how many times frequencies have been seen
inputs_cycle = cycle(inputs)  # Create circular iterable in case we need to loop more than once

while 2 not in freq_dict.values():  # Check if we've seen a frequency twice
    frequency += next(inputs_cycle)
    frequency_str = str(frequency)  # Create this string only once
    if frequency_str not in freq_dict.keys():
        freq_dict[frequency_str] = 0
    freq_dict[frequency_str] += 1

for key in freq_dict:  # Search for the frequency that appeared more than once
    if freq_dict[key] == 2:
        print(key)
