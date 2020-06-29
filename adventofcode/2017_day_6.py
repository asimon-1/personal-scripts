# input_list = [0,2,7,0]
input_list = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

configs = []

configs.append(" ".join(str(e) for e in input_list))
print(configs)
for counter in xrange(15000):
    max_index = input_list.index(max(input_list))
    bucket = input_list[max_index]
    input_list[max_index] = 0
    for i in xrange(bucket):
        # print('Adding one to bin {}'.format((max_index+i)%len(input_list)))
        input_list[(max_index + i + 1) % len(input_list)] += 1
    list_str = " ".join(str(e) for e in input_list)
    if list_str in configs:
        loop_size = len(configs) - configs.index(list_str)
        break
    else:
        configs.append(list_str)
        # print(configs)

print("Answer: {}".format(counter + 1))
print("Cycle Length: {}".format(loop_size))
