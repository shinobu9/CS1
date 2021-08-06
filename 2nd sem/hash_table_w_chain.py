def my_hash(basis, module, line):
    output = 0
    length = len(line)
    line = line[::-1]
    for i in range(length):
        output += ( ord(line[i]) * ( basis ** i ) ) #% module
    return output % module

def insert(table, key, value):
    new_hash = my_hash(91, 100, key)
    new_chunk = [str(new_hash), str(key), str(value)]
    chunk_set = False
    for chunk in table[new_hash % 10]:
        if chunk[1] == new_chunk[1]:
            chunk[2] = new_chunk[2]
            chunk_set = True
            break
    if chunk_set == False:
        table[new_hash % 10].append(new_chunk)

def search(table, key):
    output = 0
    basis = 91
    module = 100
    length = len(key)
    line = key[::-1]
    for i in range(length):
        output += ( ord(line[i]) * ( basis ** i ) ) #% module
    output = output % module
    branch_num = output % len(table)
    for chunk in table[branch_num]:
        if key == chunk[1]:
            return chunk[2]
    return('KeyError')
        
def remove(table, key):
    output = 0
    basis = 91
    module = 100
    length = len(key)
    line = key[::-1]
    for i in range(length):
        output += ( ord(line[i]) * ( basis ** i ) ) #% module
    output = output % module
    branch_num = output % len(table)
    for chunk in table[branch_num]:
        if key == chunk[1]:
            val = chunk[2]
            table[branch_num].remove(chunk)
            return val
    return('KeyError')

table = [[] for i in range(10)]
n = int(input())
for i in range(n):
    key, value = input().split()
    insert(table, key, value)

for i in range(10):
    if table[i] != []:
        print(i)
        for item in table[i]:
            print(' '.join(item))

print(search(table, 'MARIYA'))

remove(table, 'MARIYA')

for i in range(10):
    if table[i] != []:
        print(i)
        for item in table[i]:
            print(' '.join(item))