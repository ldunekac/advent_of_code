import sys
import time
from alive_progress import alive_bar
from queue import PriorityQueue

def solution2(machines):
    total = 0
    with alive_bar(len(machines)) as bar:
        for machine in machines:
            (ax, ay), (bx, by), (goalx, goaly) = machine
            machine = (ax, ay), (bx, by), (goalx + 10000000000000, goaly + 10000000000000)
            total += min_cost2(machine)
            bar()
    return total

def main_cost2(machine):
    pass

def min_cost(machine):
    a_cost = 3
    b_cost = 1
    (ax, ay), (bx, by), (goalx, goaly) = machine

    found = False
    max_cost = None

    timesx = goalx // ax
    timesy = goaly // ay

    a_press = min(timesx, timesy)
    print(f"Initial A press: {a_press}")
    b_press_ans = -1
    a_press_ans = -1
    while a_press > -1:
        # print(a_press)
        new_goal_x = goalx - (ax * a_press)
        new_goal_y = goaly - (ay * a_press)

        b_pess_x = new_goal_x // bx
        b_pess_y = new_goal_y // by

        b_equal = b_pess_x == b_pess_y
        total_zero = goalx == a_press * ax + b_pess_x * bx and \
        goaly == a_press * ay + b_pess_y * by


        if not found and b_equal and total_zero:
            found = True
            max_cost = (a_press * 3) + (b_pess_x)
            b_press_ans = b_pess_x
            a_press_ans = a_press
        elif  b_equal and total_zero:
            new_cost = (a_press * 3) + (b_pess_x)
            if new_cost <= max_cost:
                max_cost = new_cost
                b_press_ans = b_pess_x
                a_press_ans = a_press

        a_press -= 1
    
    if a_press == -1 and not found:
        return 0
    # print(a_press_ans, b_press_ans)
    return (a_press_ans * 3) + b_press_ans




# 61916 too high

def solution1(machines):
    total = 0
    with alive_bar(len(machines)) as bar:
        for machine in machines:
            total += min_cost(machine)
            bar()
    return total

def parse_input(file_name):
    machines = []
    with open(file_name, "r") as file:
        a = 0
        b = 0
        goal = 0
        for line in file:
            if line.strip() == "":
                machines.append((a,b,goal))
            elif "Button" in line:
                button, value = line.split(":")
                x, y = value.strip().split(", ")
                x = int(x[2:])
                y = int(y[2:])
                if "A" in button:
                    a = (x, y)
                else:
                    b = (x,y)
            elif "Prize" in line: 
                _, loc = line.strip().split(": ")
                x, y = loc.strip().split(", ")
                x = int(x[2:])
                y = int(y[2:])
                goal = (x, y)
            else:
                raise Exception("WAT")
        machines.append((a, b, goal))
        # print(machines)
        return machines

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