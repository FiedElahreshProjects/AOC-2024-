import sys

def read_input():
    lines_func = [line.rstrip('\n') for line in sys.stdin.readlines()]
    return lines_func

lines = read_input()
grid = [list(row) for row in lines]

height = len(grid)
width = len(grid[0])
ant_dicto = {}

for x in range(height):
    for y in range(width):
        if grid[x][y] != '.':
            if grid[x][y] not in ant_dicto:
                ant_dicto[grid[x][y]] = []
            ant_dicto[grid[x][y]].append((y, x))

anti_nodes = set()
for key in ant_dicto:
    arr = ant_dicto[key]
    for i in range(len(arr)):
        x_one, y_one = arr[i]
        for j in range(i + 1, len(arr)):
            x_two, y_two = arr[j]
            slope = (x_two - x_one, y_two - y_one)
            a_one = (x_one - slope[0], y_one - slope[1])
            a_two = (x_two + slope[0], y_two + slope[1])
            if 0 <= a_one[0] < width and 0 <= a_one[1] < height:
                anti_nodes.add(a_one)
            if 0 <= a_two[0] < width and 0 <= a_two[1] < height:
                anti_nodes.add(a_two)

print(len(anti_nodes))



