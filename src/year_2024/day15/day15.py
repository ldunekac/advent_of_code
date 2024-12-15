import sys
import time
from alive_progress import alive_bar


def update_map(map):

    new_map = []
    for row in map:
        new_row = []
        for col in row:
            if col == "#":
                new_row.extend(["#","#"])
            elif col == "O":
                new_row.extend(["[", "]"])
            elif col == ".":
                new_row.extend([".", "."])
            elif col == "@":
                new_row.extend(["@", "."])
            else:
                raise Exception(f"{col} is not in the new map mapping")
        new_map.append(new_row)
    return new_map

def push_up_or_down(loc, dir_row, map):
    loc_row, loc_col = loc
    boxes_to_move = []

    if map[loc_row + dir_row][loc_col] == "[":
        boxes_to_move.append([(loc_row + dir_row, loc_col), (loc_row + dir_row,loc_col + 1)])
    elif map[loc_row + dir_row][loc_col] == "]":
        boxes_to_move.append([(loc_row + dir_row, loc_col), (loc_row + dir_row, loc_col - 1)])
    elif map[loc_row + dir_row][loc_col] == ".":
        map[loc_row][loc_col] = "."
        map[loc_row + dir_row][loc_col] = "@"
        return (loc_row + dir_row, loc_col), map
    elif map[loc_row + dir_row][loc_col] == "#":
        return loc, map
    else:
        raise Excpeiton("No where to go")


    while True:
        last_row = boxes_to_move[-1]
        next_row_boxes = []
        # print(last_row)
        for row, col in last_row:
            if map[row + dir_row][col] == "[":
                next_row_boxes.extend([(row + dir_row, col),(row + dir_row, col + 1)])
            elif map[row + dir_row][col] == "]":
                next_row_boxes.extend([(row + dir_row, col), (row + dir_row, col - 1)])
            elif map[row + dir_row][col] == "#":
                # Hit a wall, nothing happens
                return loc, map
            elif map[row + dir_row][col] == ".":
                continue
            else:
                raise Exception("Where are we going?")

        if len(next_row_boxes) == 0:
            # Move all of the boxes
            for boxes in reversed(boxes_to_move):
                # print(boxes)
                for row, col in set(boxes):
                    map[row + dir_row][col] = map[row][col]
                    map[row][col] = "."
            map[loc_row][loc_col] = "."
            map[loc_row + dir_row][loc_col] = "@"
            return (loc_row + dir_row, loc_col), map
        else:
            boxes_to_move.append(next_row_boxes)


def push_left_or_right(loc, direciton, map):
    dir_row, dir_col = direciton
    loc_row, loc_col = loc
    amount_to_move = 1
    while True:
        end_row = loc_row + (dir_row * amount_to_move)
        end_col = loc_col + (dir_col * amount_to_move)
        if map[end_row][end_col] == "#":
            # Nothing happends
            return loc, map
        elif map[end_row][end_col] == ".":
            for i in range(amount_to_move, 0, -1):
                new_row = loc_row + (dir_row * i)
                new_col = loc_col + (dir_col * i)

                pre_row = loc_row + (dir_row * (i - 1))
                pre_col = loc_col + (dir_col * (i - 1))
                map[new_row][new_col] = map[pre_row][pre_col]

            map[loc_row][loc_col] = "."
            return (loc_row + dir_row , loc_col + dir_col), map

        elif map[end_row][end_col] == "[" or map[end_row][end_col] == "]":
            amount_to_move += 1

def solution2(input):
    old_map, commands = input
    map = update_map(old_map)
    loc = find_start(map)

    with alive_bar(len(commands)) as bar:
        # for row in map:
        #     for col in row:
        #         print(col, end='')
        #     print('\n', end = '')

        for command in commands:
            if command == "^":
                loc, map = push_up_or_down(loc, -1, map)
            elif command == "<":
                loc, map = push_left_or_right(loc, (0, -1), map)
            elif command == "v":
                loc, map = push_up_or_down(loc, 1, map)
            elif command == ">":
                loc, map = push_left_or_right(loc, (0, 1), map)
            else:
                raise Exception(f"{command} is not a command")
            bar()

            # for row in map:
            #     for col in row:
            #         print(col, end='')
            #     print('\n', end = '')

    total = 0
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == "[":
                total += (100 * i) + j
    return total

def find_start(map):
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == "@":
                return (i, j)
    raise Exception("No start found")


def push(loc, direction, map):

    dir_row, dir_col = direction
    loc_row, loc_col = loc
    amount_to_move = 1
    while True:
        end_row = loc_row + (dir_row * amount_to_move)
        end_col = loc_col + (dir_col * amount_to_move)
        if map[end_row][end_col] == "#":
            # Nothing happends
            return loc, map
        elif map[end_row][end_col] == ".":
            for i in range(amount_to_move, 0, -1):
                new_row = loc_row + (dir_row * i)
                new_col = loc_col + (dir_col * i)

                pre_row = loc_row + (dir_row * (i - 1))
                pre_col = loc_col + (dir_col * (i - 1))
                map[new_row][new_col] = map[pre_row][pre_col]

            map[loc_row][loc_col] = "."
            return (loc_row + dir_row , loc_col + dir_col), map

        elif map[end_row][end_col] == "O":
            amount_to_move += 1

    return loc, map

def solution1(input):
    map, commands = input
    loc = find_start(map)

    with alive_bar(len(commands)) as bar:
        for command in commands:
            if command == "^":
                loc, map = push(loc, (-1, 0), map)
            elif command == "<":
                loc, map = push(loc, (0, -1), map)
            elif command == "v":
                loc, map = push(loc, (1, 0), map)
            elif command == ">":
                loc, map = push(loc, (0, 1), map)
            else:
                raise Exception(f"{command} is not a command")
            bar()


    total = 0
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == "O":
                total += (100 * i) + j

    # for row in map:
    #     for col in row:
    #         print(col, end='')
    #     print('\n', end = '')
    return total


def parse_input(file_name):
    map = []
    commands = ""
    building_map = True
    with open(file_name, "r") as file:
        for line in file:
            if line.strip() == "":
                building_map = False
            elif building_map:
                map.append([x for x in line.strip()])
            else:
                commands += line.strip()

    return map, commands

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