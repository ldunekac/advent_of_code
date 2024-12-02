import sys


def is_decreasing(level):
    prev = None
    for i, num in enumerate(level):
        if i == 0:
            prev = num
        else:
            if num >= prev:
                return False
            prev  = num
    return True

def is_increasing(level):
    prev = None
    for i, num in enumerate(level):
        if i == 0:
            prev = num
        else:
            if num <= prev:
                return False
            prev = num
    return True

def good_adjacent(level):
    diffs = [abs(a-b) for a,b in zip(level, level[1::])]
    for diff in diffs:
        if diff == 0 or diff > 3:
            return False
    return True

def solution1(levels):
    total = 0
    for level in levels:
        if not good_adjacent(level):
            pass
        elif is_decreasing(level):
            total += 1
        elif is_increasing(level):
            total += 1
        else:
            pass

    return total

def level_good(level):
    if not good_adjacent(level):
        return False
    elif is_decreasing(level):
        return True
    elif is_increasing(level):
        return True
    else:
        return False
def solution2(levels):
    total = 0
    for level in levels:
        if level_good(level):
            total += 1
        else:
            level_len = len(level)
            for i in range(level_len):
                new_level = level[0:i] + level[i+1:level_len]
                if level_good(new_level):
                    total += 1
                    break
    return total

def parse_input(file_name):
    levels = []
    with open(file_name, "r") as file:
        for line in file:
            levels.append([int(a) for a in line.split()])
    return levels

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()