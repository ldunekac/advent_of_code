import sys

def solution2(sequence):
    current = dict()
    for x in sequence:
        current[x] = current.get(x, 0) + 1

    for _ in range(75):
        next_dict = dict()
        for key, val in current.items():
            if key == '0':
                next_dict['1'] = next_dict.get('1', 0) + val
            elif len(key) % 2 == 0:
                half = len(key)//2
                num1 = str(int("".join(list(key)[:half])))
                num2 = str(int("".join(list(key)[half:])))
                next_dict[num1] = next_dict.get(num1, 0) + val
                next_dict[num2] = next_dict.get(num2, 0) + val
            else:
                new_num = str(int(key) * 2024)
                next_dict[new_num] = next_dict.get(new_num, 0) + val
        current = next_dict

    print(len(current))
    return sum(val for _, val in current.items())

def solution1(sequence):
    current_sequence = sequence
    for _ in range(25):
        new_sequence = []
        for num in current_sequence:
            if num == '0':
                new_sequence.append('1')
            elif len(num) % 2 == 0:
                half = len(num)//2
                new_sequence.append(str(int("".join(list(num)[:half]))))
                new_sequence.append(str(int("".join(list(num[half:])))))
            else:
                new_sequence.append(str(int(num) * 2024))
        current_sequence = new_sequence
    return len(current_sequence)

def parse_input(file_name):
    with open(file_name, "r") as file:
        return file.read().strip().split()

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)
    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()