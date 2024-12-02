import sys

def is_safe(line):
    """Check if a sequence is safe according to the original rules."""
    differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    # Check if all differences are either increasing or decreasing within the valid range
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return is_increasing or is_decreasing


# Read input
input_data = sys.stdin.read()
lines = input_data.splitlines()

safe_count = 0

for line in lines:
    # Convert the line into a list of integers
    line = list(map(int, line.split()))

    # Check if the line is safe as is
    if is_safe(line):
        safe_count += 1
    else:
        # Simulate removing each level and check if it becomes safe
        for i in range(len(line)):
            modified_line = line[:i] + line[i + 1:]  # Remove the ith level
            if is_safe(modified_line):
                safe_count += 1
                break  # No need to check further levels for this line

print(safe_count)
