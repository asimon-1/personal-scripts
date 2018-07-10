with open('2017_day_8_input.txt') as f:
    raw = f.read()

input_list = [p.replace(',','').replace('inc','+=').replace('dec','-=') for p in raw.split('\n')]
words = [p.split(' ')[0] for p in input_list]
words = dict(zip(set(words),[0]*len(set(words))))
for w in words:
    input_list = [i.replace(' {} '.format(w),' words[\'{}\']'.format(w)) for i in input_list]
input_list = [p.split('if') for p in input_list]

conditions = [cond[1].strip() for cond in input_list]
instructions = [cond[0].strip() for cond in input_list]

for i,cond in enumerate(conditions):
    print("Condition: {}".format(cond))
    if eval(cond):
        print("Condition Passed, Executing {}".format(instructions[i]))
        exec(instructions[i])
print('Maximum: {}'.format(words.values()))