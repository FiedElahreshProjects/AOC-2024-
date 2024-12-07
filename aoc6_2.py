import sys

lines = [line.rstrip('\n') for line in sys.stdin.readlines()]

grid = [list(row) for row in lines]
height = len(grid)
width = len(grid[0])
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up = (0, - 1), right = (1, 0), down = (0,1), left = (-1, 0)


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

            # Convert the guard's starting position to '.'
            grid[y][x] = '.'

x, y = start_x, start_y
start_dir = facing

def simulate_with_obstruction(ox, oy):
    # Place obstruction at (ox, oy)
    original_char = grid[oy][ox]
    grid[oy][ox] = '#'

    x, y = start_x, start_y
    facing = start_dir
    visited_states = set()
    visited_states.add((x, y, facing))

    while True:
        dx, dy = direction[facing]
        front_x, front_y = x + dx, y + dy

        # Check if front cell is valid
        if 0 <= front_x < width and 0 <= front_y < height:
            # Inside the map
            if grid[front_y][front_x] == '#':
                # Turn right
                facing = (facing + 1) % 4
            else:
                # Move forward
                x, y = front_x, front_y
        else:
            # Guard would leave the map, no loop
            grid[oy][ox] = original_char
            return False

        if (x, y, facing) in visited_states:
            # Loop detected
            grid[oy][ox] = original_char
            return True
        else:
            visited_states.add((x, y, facing))


def solve():
    count = 0
    for oy in range(height):
        for ox in range(width):
            if (ox, oy) != (start_x, start_y) and grid[oy][ox] == '.':
                if simulate_with_obstruction(ox, oy):
                    count += 1
    return count


print(solve())






