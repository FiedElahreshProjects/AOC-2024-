import sys

# dictonary of all elements, with the key being the element, and the value being all the elements are should be after it

lines = [line.strip() for line in sys.stdin.readlines()]


# Find the index of the blank line
blank_line_index = None
for i, line in enumerate(lines):
    if line == '':
        blank_line_index = i
        break

rules_lines = lines[:blank_line_index]
rules = []
rules_dicto = {}
for r_line in rules_lines:
    x_str, y_str = r_line.split('|')
    x, y = int(x_str), int(y_str)
    rules.append((x, y))

updates_lines = lines[blank_line_index+1:]
updates = []

for u_line in updates_lines:
    if u_line:  # ensure it's not an empty line, parsing input
        pages = [int(x) for x in u_line.split(',')]
        updates.append(pages)

for rule in rules: # Creating dicto i stated above
    if rule[0] not in rules_dicto:
        rules_dicto[rule[0]] = set()
    rules_dicto[rule[0]].add(rule[1])

total = 0

for update in updates:
    position = {value: index for index, value in enumerate(update)}
    valid = True
    for key in rules_dicto:
        if key in position:
            for val in rules_dicto[key]:
                if val in position:
                    if position[key] > position[val]:
                        valid = False
                        break

        if not valid:
            break

    if valid:
        middle_page = update[len(update) // 2]
        total += middle_page

print(total)




