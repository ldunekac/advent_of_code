import sys
import re

def do_ranges(memory):
    dos = [0] + [m.start() for m in re.finditer("do\(\)", memory)]
    donts = [m.start() for m in re.finditer("don\'t\(\)", memory)]

    good_ranges = []
    donts_max = max(donts)
    for do in dos:
        if len(good_ranges) > 0:
            last_range = good_ranges[-1]
            if last_range[0] <= do <= last_range[1]:
                # The current do is between a do and don't skip the due
                continue
        range_start = do
        if do > donts_max:
            good_ranges.append((range_start, len(memory)))
            break
        else:
            range_stop = min([d for d in donts if do < d])
            good_ranges.append((range_start, range_stop))

    # print(dos)
    # print(donts)
    # print(good_ranges)

    return good_ranges


def in_good_range(index, good_ranges):
    for start, end in good_ranges:
        if start <= index <= end:
            return True
    return False

def solution2(memory):
    total = 0
    good_ranges = do_ranges(memory)

    multis = [0] + [m.start() for m in re.finditer("mul\(", memory)]

    for multi in multis:
        index = multi + 3
        if not in_good_range(index, good_ranges):
            continue

        num1=""
        i = 0
        error = True
        for i in range(4):
            next_char = memory[index+i+1]
            if next_char >= "0" and next_char <= "9":
                num1 += next_char
            elif next_char == ",":
                error = False
                break
            else:
                break
        if error:
            continue

        index = index + i + 1
        num2= ""
        error = True
        for i in range(4):
            next_char = memory[index+i+1]
            if next_char >= "0" and next_char <= "9":
                num2 += next_char
            elif next_char == ")":
                error = False
                break
            else:
                break
        if error:
            continue
        total += int(num1) * int(num2)
    return total

def solution1(memory):
    total = 0
    while(True):
        index = memory.find("mul(")
        if index < 0:
            break
        index += 3
        num1=""
        i = 0
        error = True
        for i in range(4):
            next_char = memory[index+i+1]
            if next_char >= "0" and next_char <= "9":
                num1 += next_char
            elif next_char == ",":
                error = False
                break
            else:
                break
        if error:
            memory = memory[index+4:]
            continue
        index = index + i + 1
        num2= ""
        error = True
        for i in range(4):
            next_char = memory[index+i+1]
            if next_char >= "0" and next_char <= "9":
                num2 += next_char
            elif next_char == ")":
                error = False
                break
            else:
                break
        memory = memory[index+i+1:]
        if error:
            continue
        total += int(num1) * int(num2)
    return total

def parse_input(file_name):
    with open(file_name, "r") as file:
        return file.read()

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()