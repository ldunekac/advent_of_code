import sys
from alive_progress import alive_bar


def solution2(equations):
    total = 0
    with alive_bar(len(equations)) as bar:
        for equation in equations:
            test_val = equation[0]
            sequence = equation[1]
            operators = ["*"] * (len(sequence) - 1)
            while True:
                sequence_val = sequence[0]
                for next_val, op in zip(sequence[1:], operators):
                    if op == "*":
                        sequence_val = sequence_val * next_val
                    elif op == "+":
                        sequence_val = sequence_val + next_val
                    elif op == "||":
                        sequence_val = int(str(sequence_val) + str(next_val))
                    else:
                        print("DIE")

                if test_val == sequence_val:
                    total += test_val
                    break

                if all([x == "||" for x in operators]):
                    break
                for j, op in enumerate(operators):
                    if op == "*":
                        operators[j] = "+"
                        for k in range(j):
                            operators[k] = "*"
                        break
                    elif op == "+":
                        operators[j] = "||"
                        for k in range(j):
                            operators[k] = "*"
                        break
            bar()    
    return total


def solution1(equations):
    total = 0
    with alive_bar(len(equations)) as bar:
        for equation in equations:
            test_val = equation[0]
            sequence = equation[1]
            operators = ["*"] * (len(sequence) - 1)
            while True:
                sequence_val = sequence[0]
                for next_val, op in zip(sequence[1:], operators):
                    if op == "*":
                        sequence_val = sequence_val * next_val
                    elif op == "+":
                        sequence_val = sequence_val + next_val
                    else:
                        print("DIE")

                if test_val == sequence_val:
                    total += test_val
                    break

                if all([x == "+" for x in operators]):
                    break
                for j, op in enumerate(operators):
                    if op == "*":
                        operators[j] = "+"
                        for k in range(j):
                            operators[k] = "*"
                        break
            bar()    
    return total


def parse_input(file_name):
    lines = []
    with open(file_name, "r") as file:
        for line in file:
            test_value, sequence = line.strip().split(":")
            test_value = int(test_value)
            sequence = [int(x) for x in sequence.strip().split()]
            lines.append((test_value, sequence))
    return lines

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()