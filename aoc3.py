import re

def process_memory_part2(corrupted_memory):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_enabled = True
    total_sum = 0

    instructions = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", corrupted_memory)

    for instruction in instructions:
        if re.match(do_pattern, instruction):
            mul_enabled = True
        elif re.match(dont_pattern, instruction):
            mul_enabled = False
        elif mul_enabled:
            match = re.match(mul_pattern, instruction)
            if match:
                num1, num2 = map(int, match.groups())
                total_sum += num1 * num2

    return total_sum

file_path = r'C:\Users\Fied\Desktop\aoc3.txt'
with open(file_path, 'r') as file:
    corrupted_memory = file.read()

result = process_memory_part2(corrupted_memory)

print(result)
