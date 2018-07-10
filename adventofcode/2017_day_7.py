import numpy as np

#with open('2017_day_7_input.txt') as f:
with open('2017_day_7_input.txt') as f:
    raw = f.read()

input_list = [p.replace(',','') for p in raw.split('\n')]
input_list = [p.split(' ') for p in input_list]
for i,l in enumerate(input_list):
    if '->' in l:
        del input_list[i][l.index('->')]
programs = [p[0] for p in input_list]
weights = [int(p[1].strip('()')) for p in input_list]
children = [p[2:] if len(p)>2 else [] for p in input_list]

class program:
    def __init__(self,name='',parent='',children=[],heritage=[],weight=0,supporting_weight=0):
        self.name = name
        self.parent = parent
        self.children = children
        self.heritage = heritage
        self.weight = weight
        self.supporting_weight = supporting_weight


program_list = [program(name,children=children[i],weight=weights[i]) for i,name in enumerate(programs)]
program_dict = dict(zip(programs,program_list))

for p in program_list:
    for p2 in program_list:
        if p.name in p2.children:
            p.parent = p2.name
    if p.parent == '':
        print('{} is the tree trunk.'.format(p.name))
        trunk = p

for p in program_list:
    current = p
    heritage_list = [current.name]
    while current.parent is not '':
        for p2 in program_list:
            if p2.name == current.parent:
                current = p2
                break
        heritage_list.append(current.name)
    p.heritage = heritage_list

tree_size = max([len(p.heritage) for p in program_list])

for size in xrange(tree_size,0,-1):
    for p2 in program_list:
        if len(p2.heritage) == size:
            p2.supporting_weight = p2.weight
            if p2.children == []:
                pass#p2.supporting_weight = p2.weight
            else:
                p2.supporting_weight += sum([program_dict[p3].supporting_weight for p3 in p2.children])

current = trunk
for size in xrange(tree_size):
    print('Iter {}'.format(size))
    child_weights = [program_dict[p].supporting_weight for p in current.children]
    common = max(set(child_weights), key=child_weights.count)
    for c in [program_dict[p] for p in current.children]:
        if c.supporting_weight != common:
            print('{} supporting_weight = {} when it should have been {}'.format(c.name,c.supporting_weight,common))
            print('If this is the last message, the answer is {}'.format(c.weight-(c.supporting_weight-common)))
            current = c