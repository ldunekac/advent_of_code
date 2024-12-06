import sys
import copy
from alive_progress import alive_bar


def guard_stuck_in_loop(grid):
    pos_row, pos_col, direction = start_location(grid)

    states = set()

    while True:
        grid[pos_row][pos_col] = "X"

        direction_row, direction_col = direction
        next_row, next_col = pos_row + direction_row, pos_col + direction_col
        # check if we made it in a loop
        if (next_row, next_col, direction) in states:
            return True
        states.add((next_row, next_col, direction))
        # Check if we are still in the puzzle
        if next_row < 0 or next_row >= len(grid):
            return False
        elif next_col < 0 or next_col >= len(grid[0]):
            return False
        
        # Check to see if an object was hit 
        if grid[next_row][next_col] == "#":
            # rotate
            if direction == (-1, 0): # UP
                direction = (0, 1)
            elif direction == (0, 1): # RIGHT
                direction = (1, 0)
            elif direction == (1, 0): # DOWN
                direction = (0, -1)
            elif direction == (0, -1): # LEFT
                direction = (-1, 0) 
            continue
        else:
            # Move to the next position
            pos_row, pos_col = next_row, next_col


def solution2(grid):
    total = 0
    with alive_bar(len(grid) * len(grid[0])) as bar:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "#" or val == "^":
                    continue
                else:
                    new_grid = copy.deepcopy(grid)
                    new_grid[i][j] = "#"
                    if guard_stuck_in_loop(new_grid):
                        total += 1
                bar()
    return total



def count_locations(grid):
    print("In count_locations")
    
    return sum(sum(1 for a in x if a == "X") for x in grid)

def start_location(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "^":
                return i, j, (-1, 0)

def solution1(grid):
    pos_row, pos_col, direction = start_location(grid)

    while True:
        grid[pos_row][pos_col] = "X"

        direction_row, direction_col = direction
        next_row, next_col = pos_row + direction_row, pos_col + direction_col
        # Check if we are still in the puzzle
        if next_row < 0 or next_row >= len(grid):
            return count_locations(grid)
        elif next_col < 0 or next_col >= len(grid[0]):
            return count_locations(grid)
        
        # Check to see if an object was hit 
        if grid[next_row][next_col] == "#":
            # rotate
            if direction == (-1, 0): # UP
                direction = (0, 1)
            elif direction == (0, 1): # RIGHT
                direction = (1, 0)
            elif direction == (1, 0): # DOWN
                direction = (0, -1)
            elif direction == (0, -1): # LEFT
                direction = (-1, 0) 
            continue
        else:
            # Move to the next position
            pos_row, pos_col = next_row, next_col

def parse_input(file_name):
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            grid.append([x for x in line.strip()])
    return grid

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()