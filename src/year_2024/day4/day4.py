import sys


def mas_found(i,j, grid):
    if not grid[i][j] == "A":
        return False
    elif i-1 < 0 or i+1 >= len(grid):
        return False
    elif j-1 < 0 or j+1 >= len(grid[0]):
        return False

    ans = (grid[i+1][j+1] == "S" or grid[i+1][j+1] == "M") and \
        (grid[i-1][j-1] == "S" or grid[i-1][j-1] == "M") and \
        (not grid[i+1][j+1] == grid[i-1][j-1]) and \
        (grid[i+1][j-1] == "S" or grid[i+1][j-1] == "M") and \
        (grid[i-1][j+1] == "S" or grid[i-1][j+1] == "M") and \
        (not grid[i-1][j+1] == grid[i+1][j-1])

    return ans


def solution2(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += 1 if mas_found(i,j, grid) else 0
    return total


def check_xmas_direction(i, j, direction_i, direction_j, grid):
    if not grid[i][j] == "X":
        return False
    for multi, mas in enumerate("MAS"):
        i_index = i + ((multi + 1) * direction_i)
        j_index = j + ((multi + 1) * direction_j)
        if i_index < 0 or i_index >= len(grid):
            return False
        elif j_index < 0 or j_index >= len(grid[0]):
            return False
        elif not grid[i_index][j_index] == mas:
            return False
    return True




def xmas_found(i,j, grid):
    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    total = 0
    for dir_i, dir_j in directions:
        if check_xmas_direction(i, j, dir_i, dir_j, grid):
            total += 1
    return total


def solution1(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += xmas_found(i,j, grid)
    return total

    print(grid)
    return total

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