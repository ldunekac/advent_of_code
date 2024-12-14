import sys
import time
from alive_progress import alive_bar


def solution2(input):
    with alive_bar(len(input)) as bar:
        bar()
    return ""

def solution1(input):
    with alive_bar(len(input)) as bar:
        bar()
    return ""


def parse_input(file_name):
    with open(file_name, "r") as file:
        for line in file:
            continue

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