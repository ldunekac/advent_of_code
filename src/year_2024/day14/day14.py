import sys
import time
from alive_progress import alive_bar

def solution2(robots):
    width = 101
    height = 103
    # 6493
    for i in range (6000, 7000):
        input("Input")
        print(f"{i=}")
        final_locations = []
        for robot in robots:
            px, py = robot[0]
            vx, vy = robot[1]
            new_px = (px + (vx * i)) % width
            new_py = (py + (vy * i)) % height
            final_locations.append((new_px, new_py))

        fl_set = set(final_locations)

        for jj in range(height):
            for ii in range(width):
                if (ii, jj) in fl_set:
                    print('X', end='')
                else:
                    print('.', end='')
            print("\n", end='')

def solution1(robots):
    # Example
    # width = 11
    # height = 7
    # input
    width = 101
    height = 103
    final_lcoaitons = []
    with alive_bar(len(robots)) as bar:
        for robot in robots:
            px, py = robot[0]
            vx, vy = robot[1]
            new_px = (px + (vx * 100)) % width
            new_py = (py + (vy * 100)) % height
            final_lcoaitons.append((new_px, new_py))
            bar()

    q1 = sum(1 for x, y in final_lcoaitons if x < width // 2 and y < height // 2 )
    q2 = sum(1 for x, y in final_lcoaitons if x > width // 2 and y < height // 2 )
    q3 = sum(1 for x, y in final_lcoaitons if x < width // 2 and y > height // 2 )
    q4 = sum(1 for x, y in final_lcoaitons if x > width // 2 and y > height // 2 )
    print(q1, q2, q3, q4)

    return q1 * q2 * q3 * q4


def parse_input(file_name):
    robots = []
    with open(file_name, "r") as file:
        for line in file:
            p, v = line.strip().split()
            _, pcords = p.split("=")
            px, py = pcords.split(",")
            _, vcords = v.split("=")
            vx, vy = vcords.split(",")
            robots.append(((int(px), int(py)), (int(vx), int(vy))))
    return robots

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