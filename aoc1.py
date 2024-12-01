import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

result = 0
lis_two = {}

for line in lines:
    parts = line.split()
    if parts[1] in lis_two:
        lis_two[parts[1]] += 1
    else:
        lis_two[parts[1]] = 1

    if parts[0] in lis_two:
        result += int(parts[0]) * lis_two[parts[0]]

print(result)
