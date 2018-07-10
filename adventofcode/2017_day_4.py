with open('2017_day_4_input.txt','r') as f:
    input_list = f.read()

input_list = input_list.split('\n')

count = 0
for phrase in input_list[0:-1]:
    current_phrase = phrase.split(' ')
    for i,word in enumerate(current_phrase):
        current_phrase[i] = ''.join(sorted(word))
    if len(set(current_phrase)) == len(current_phrase) and len(current_phrase)>1:
        count += 1
        print('Valid phrase: {}'.format(phrase))
    else:
        print('Invalid phrase: {}'.format(phrase))
print(count)
        
    