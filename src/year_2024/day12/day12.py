import sys


def get_area_sides(section):
    area = len(section)
    perimeter = area * 4

    edges = []

    mini = None
    maxi = None
    minj = None
    maxj = None
    for val in section:
        i, j = val
        if mini is None:
            mini = i
        else:
            mini = min(mini, i)
        if maxi is None:
            maxi = i
        else:
            maxi = max(maxi, i)

        if minj is None:
            minj = j
        else:
            minj = min(minj, j)
        if maxj is None:
            maxj = j
        else:
            maxj = max(maxj, j)

        if not (i - 1, j) in section:
            edges.append((i, j, 0))
        if not (i + 1, j) in section:
            edges.append((i, j, 1))
        if not (i , j - 1) in section:
            edges.append((i, j, 2))
        if not (i, j + 1) in section:
            edges.append((i, j, 3))

    num_edges = 0
    for i in range(mini, maxi + 1):
        row = [(x, y, val) for x, y, val in edges if x == i and val == 0]
        in_group = False
        for j in range(minj, maxj + 1):
            if not in_group and (i, j, 0) in row:
                in_group = True
            if in_group and (i, j, 0) not in row:
                in_group = False
                num_edges += 1
        if in_group:
            num_edges += 1

    for i in range(mini, maxi + 1):
        row = [(x, y, val) for x, y, val in edges if x == i and val == 1]

        in_group = False
        for j in range(minj, maxj + 1):
            if not in_group and (i, j, 1) in row:
                in_group = True
            if in_group and (i, j, 1) not in row:
                in_group = False
                num_edges += 1
        if in_group:
            num_edges += 1

    for j in range(minj, maxj + 1):
        col = [(x, y, val) for x, y, val in edges if y == j and val == 2]

        in_group = False
        for i in range(mini, maxi + 1):
            if not in_group and (i, j, 2) in col:
                in_group = True
            if in_group and (i, j, 2) not in col:
                in_group = False
                num_edges += 1
        if in_group:
            num_edges += 1

    for j in range(minj, maxj + 1):
        col = [(x, y, val) for x, y, val in edges if y == j and val == 3]

        in_group = False
        for i in range(mini, maxi + 1):
            if not in_group and (i, j, 3) in col:
                in_group = True
            if in_group and (i, j, 3) not in col:
                in_group = False
                num_edges += 1
        if in_group:
            num_edges += 1

    return area, num_edges


def solution2(grid):
    total = 0
    sections = get_sections(grid)
    for section in sections:
        area, edges = get_area_sides(section)
        total += area * edges
    return total


def parse_section(i, j, grid):
    val = grid[i][j]
    section = set()
    remaining_parse = [(i,j)]

    while len(remaining_parse) > 0:
        next_val =remaining_parse.pop()
        section.add(next_val)
        i, j = next_val
        if (i - 1 >= 0) and ((i - 1, j) not in section) and (grid[i - 1][j] == val):
            remaining_parse.append((i - 1, j))
        if (i + 1 < len(grid)) and ((i + 1, j) not in section) and (grid[i + 1][j] == val):
            remaining_parse.append((i + 1, j))
        if (j - 1 >= 0) and ((i, j - 1) not in section) and (grid[i][j - 1] == val):
            remaining_parse.append((i, j - 1))
        if (j + 1 < len(grid[0])) and ((i, j + 1) not in section) and (grid[i][j + 1] == val):
            remaining_parse.append((i, j + 1))

    return section

def get_sections(grid):
    seen = set()
    sections = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if not (i, j) in seen:
                new_section = parse_section(i, j, grid)
                sections.append(new_section)
                seen.update(new_section)
    return sections


def get_area_perimeter(section):
    area = len(section)
    perimeter = area * 4

    for i, j in section:
        if (i - 1, j) in section:
            perimeter -= 1
        if (i + 1, j) in section:
            perimeter -= 1
        if (i , j - 1) in section:
            perimeter -= 1
        if (i, j + 1) in section:
            perimeter -= 1

    return area, perimeter

def solution1(grid):
    total = 0
    sections = get_sections(grid)
    for section in sections:
        area, perimeter = get_area_perimeter(section)
        total += area * perimeter
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