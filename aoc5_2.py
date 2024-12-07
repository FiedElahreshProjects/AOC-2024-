import sys
from collections import defaultdict, deque

lines = [line.strip() for line in sys.stdin.readlines()]

# Find the index of the blank line separating rules from updates
blank_line_index = None
for i, line in enumerate(lines):
    if line == '':
        blank_line_index = i
        break

rules_lines = lines[:blank_line_index]
rules = []
for r_line in rules_lines:
    x_str, y_str = r_line.split('|')
    x, y = int(x_str), int(y_str)
    rules.append((x, y))

updates_lines = lines[blank_line_index+1:]
updates = []
for u_line in updates_lines:
    if u_line:
        pages = [int(x) for x in u_line.split(',')]
        updates.append(pages)

rules_dicto = {}
for (X, Y) in rules:
    if X not in rules_dicto:
        rules_dicto[X] = set()
    rules_dicto[X].add(Y)

total_correct = 0
total_corrected = 0

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
        total_correct += middle_page
    else:
        update_set = set(update)
        adj = defaultdict(list)
        indegree = {p: 0 for p in update}

        for X in rules_dicto:
            if X in update_set:
                for Y in rules_dicto[X]:
                    if Y in update_set:
                        adj[X].append(Y)

        for node in adj:
            for neigh in adj[node]:
                indegree[neigh] += 1

        q = deque([p for p in update if indegree[p] == 0])
        sorted_update = []
        while q:
            node = q.popleft()
            sorted_update.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        middle_page = sorted_update[len(sorted_update) // 2]
        total_corrected += middle_page

print(total_correct)

print(total_corrected)
