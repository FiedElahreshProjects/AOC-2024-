import sys
from math import gcd


def read_input():
    lines_func = [line.rstrip('\n') for line in sys.stdin.readlines()]
    return lines_func


lines = read_input()
grid = [list(row) for row in lines]

height = len(grid)
width = len(grid[0])
ant_dicto = {}

for y in range(height):
    for x in range(width):
        if grid[y][x] != '.':
            if grid[y][x] not in ant_dicto:
                ant_dicto[grid[y][x]] = []
            ant_dicto[grid[y][x]].append((x, y))

anti_nodes = set()

for key in ant_dicto:
    arr = ant_dicto[key]
    for i in range(len(arr)):
        x1, y1 = arr[i]
        for j in range(i + 1, len(arr)):
            x2, y2 = arr[j]

            dx = x2 - x1
            dy = y2 - y1
            step = gcd(dx, dy)
            dx //= step
            dy //= step

            x, y = x1, y1
            while 0 <= x < width and 0 <= y < height:
                anti_nodes.add((x, y))
                x += dx
                y += dy

            x, y = x1, y1
            while 0 <= x < width and 0 <= y < height:
                anti_nodes.add((x, y))
                x -= dx
                y -= dy

for key in ant_dicto:
    if len(ant_dicto[key]) >= 2:
        for pos in ant_dicto[key]:
            anti_nodes.add(pos)

print(len(anti_nodes))
