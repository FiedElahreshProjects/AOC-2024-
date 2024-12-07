import sys

lines = [line.rstrip('\n') for line in sys.stdin.readlines()]

grid = [list(row) for row in lines]

height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        if grid[y][x] in ['^', '>', 'v', '<']:
            start_x, start_y = x, y
            if grid[y][x] == '^':
                facing = 0  # up
            elif grid[y][x] == '>':
                facing = 1  # right
            elif grid[y][x] == 'v':
                facing = 2  # down
            else:
                facing = 3  # left

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up = (0, - 1), right = (1, 0), down = (0,1), left = (-1, 0)

visited = set()
visited.add((start_x, start_y))

x, y = start_x, start_y

while True:
    dx, dy = direction[facing]
    front_x, front_y = x + dx, y + dy

    if 0 <= front_x < width and 0 <= front_y < height:
        if grid[front_y][front_x] == '#':
            facing = (facing + 1) % 4
        else:
            x, y = front_x, front_y
            visited.add((x, y))

    else:
        break

print(len(visited))



