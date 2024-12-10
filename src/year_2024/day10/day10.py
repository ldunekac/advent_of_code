import sys



def number_of_paths_at_point(i, j, grid):
    stack = [[(i, j,0)]]

    total = 0
    while len(stack) > 0:
        potentail_path = stack.pop(0)
        # print(potentail_path)
        if len(potentail_path) == 10:
            total += 1
            continue

        current_i, current_j, num = potentail_path[-1]
        # print(f"{current_i=}, {current_j=}, {num=} ")

        if current_i - 1 >= 0 and grid[current_i - 1][current_j] == num + 1:
            stack.append(potentail_path[:] + [(current_i - 1, current_j, num + 1)])

        if current_i + 1 < len(grid) and grid[current_i + 1][current_j] == num + 1:
            stack.append(potentail_path[:] + [(current_i + 1, current_j, num + 1)])

        if current_j - 1 >= 0 and grid[current_i][current_j - 1] == num + 1:
            stack.append(potentail_path[:] + [(current_i, current_j - 1, num + 1)])

        if current_j + 1 < len(grid[0]) and grid[current_i][current_j + 1] == num + 1:
            stack.append(potentail_path[:] + [(current_i, current_j + 1, num + 1)])

    # print(total)

    return total

def solution2(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                total += number_of_paths_at_point(i, j, grid)
    return total



def number_of_ends_at_point(i, j, grid):
    stack = [[(i, j,0)]]

    nine_positions = set()
    while len(stack) > 0:
        potentail_path = stack.pop(0)
        # print(potentail_path)
        if len(potentail_path) == 10:
            nine_positions.add(potentail_path[-1])
            continue

        current_i, current_j, num = potentail_path[-1]
        # print(f"{current_i=}, {current_j=}, {num=} ")

        if current_i - 1 >= 0 and grid[current_i - 1][current_j] == num + 1:
            stack.append(potentail_path[:] + [(current_i - 1, current_j, num + 1)])

        if current_i + 1 < len(grid) and grid[current_i + 1][current_j] == num + 1:
            stack.append(potentail_path[:] + [(current_i + 1, current_j, num + 1)])

        if current_j - 1 >= 0 and grid[current_i][current_j - 1] == num + 1:
            stack.append(potentail_path[:] + [(current_i, current_j - 1, num + 1)])

        if current_j + 1 < len(grid[0]) and grid[current_i][current_j + 1] == num + 1:
            stack.append(potentail_path[:] + [(current_i, current_j + 1, num + 1)])

    # print(len(nine_positions))

    return len(nine_positions)


def solution1(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                total += number_of_ends_at_point(i, j, grid)
    return total

def parse_input(file_name):
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            grid.append([int(x) for x in line.strip()])
    return grid

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()