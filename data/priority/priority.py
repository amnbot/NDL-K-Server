import json

priority = {}
valid_digits = ['1', '2', '3', '4', '5']

with open('priority.txt') as f:
    line = 1
    count = 0
    currPriority = 0
    while line:
        line = f.readline()
        if len(line) == 2 and line[0] in valid_digits:
            digit = line[0]
            next = f.readline().strip()
            groups = next.split(',')
            priority[digit] = groups
            count +=1

# print(priority)

with open('priority.json', 'w') as p:
    json.dump(priority, p)

with open('priority.json', 'r') as p: 
    data = json.load(p)
    print(data[valid_digits[4]])