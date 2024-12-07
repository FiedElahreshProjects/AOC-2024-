import sys
import itertools
import operator

def read_input():
    lines_func = [lin.strip() for lin in sys.stdin.readlines()]
    return lines_func
def concat(a, b):
    return int(str(a) + str(b))

operations = ['*', '+', '||']

ops = {
    '+': operator.add,
    '*': operator.mul,
    '||': concat
}

dicto = {}
lines = read_input()
total = 0
for line in lines:
    key_part, values_part = line.split(':')
    dicto[int(key_part.strip())] = [int(v) for v in values_part.split()]


for key in dicto:
    for combo in itertools.product(operations, repeat=len(dicto[key]) - 1):

        result = dicto[key][0]
        for operation, val in zip(combo, dicto[key][1:]):
            result = ops[operation](result, val)

        if result == key:
            print(f"For key {key}, found a combination: {dicto[key]} with {combo}")
            total += key
            break

print(total)

