import sys


def solution2(grid):
    return ""


def solution1(grid):
    return ""


def parse_input(file_name):
    return ""


def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)
    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()