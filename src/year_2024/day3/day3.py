import sys


def solution2(levels):
    return 0

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