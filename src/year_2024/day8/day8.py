import sys
import time
from alive_progress import alive_bar

def solution2(grid):
    frequencies = dict()
    
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if not val == ".":
                l = frequencies.get(val, [])
                l.append((i,j))
                frequencies[val] = l
    
    high_spots = []
    for key, positions in frequencies.items():
        for i, position in enumerate(positions):
            for j, other in enumerate(positions[i+1:]):
                row_diff = position[0] - other[0]
                col_diff = position[1] - other[1]
                locs = []
                one = position
                locs.append(position)
                while True:
                    one = one[0] + row_diff, one[1] + col_diff
                    locs.append(one)
                    if one[0] < 0 or one[0] >= len(grid):
                        break
                    elif one[1] < 0 or one[1] >= len(grid[0]):
                        break
                one = position
                
                while True:
                    one = one[0] - row_diff, one[1] - col_diff
                    locs.append(one)
                    if one[0] < 0 or one[0] >= len(grid):
                        break
                    elif one[1] < 0 or one[1] >= len(grid[0]):
                        break
                #freq_spots = [x for x in locs if not x in [position, other]]
                high_spots.extend(locs)

    count = 0
    for row_i, column_i in set(high_spots):
        if row_i < 0 or row_i >= len(grid):
            continue
        elif column_i < 0 or column_i >= len(grid[0]):
            continue
        else:
            count += 1
    return count


def solution1(grid):
    frequencies = dict()
    
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if not val == ".":
                l = frequencies.get(val, [])
                l.append((i,j))
                frequencies[val] = l
    
    high_spots = []
    for key, positions in frequencies.items():
        for i, position in enumerate(positions):
            for j, other in enumerate(positions[i+1:]):
                row_diff = position[0] - other[0]
                col_diff = position[1] - other[1]

                one = position[0] + row_diff, position[1] + col_diff
                two = position[0] - row_diff, position[1] - col_diff
                three = other[0] + row_diff, other[1] + col_diff
                four = other[0] - row_diff, other[1] - col_diff
                freq_spots = [one, two, three, four]
                freq_spots = [x for x in freq_spots if not x in [position, other]]
                high_spots.extend(freq_spots)

    count = 0
    for row_i, column_i in set(high_spots):
        if row_i < 0 or row_i >= len(grid):
            continue
        elif column_i < 0 or column_i >= len(grid[0]):
            continue
        else:
            count += 1
    return count
    # with alive_bar(len(input)) as bar:
    #     bar()
    # return ""

def parse_input(file_name):
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            row = [x for x in line.strip()]
            grid.append(row)
    return grid

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    start = time.perf_counter()
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)
    stop = time.perf_counter()
    print(f"Took: {stop-start} seconds")

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()