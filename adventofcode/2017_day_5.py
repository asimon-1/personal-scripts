with open("2017_day_5_input.txt", "r") as f:
    input_list = f.read()
input_list = input_list.split("\n")[0:-1]
for i, x in enumerate(input_list):
    input_list[i] = int(x)

# input_list = [0, 3, 0, 1, -3]

pos = 0
for counter in xrange(int(1e8)):
    newpos = pos + input_list[pos]
    if input_list[pos] > 2:
        input_list[pos] -= 1
    else:
        input_list[pos] += 1
    if newpos in range(len(input_list)):
        pos = newpos
        # print(input_list,pos)
        continue
    else:
        break
print(counter + 1)
