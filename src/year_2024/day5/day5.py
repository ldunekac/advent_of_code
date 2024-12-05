import sys

class Data:
    def __init__(self, before_after, after_before, instructions):
        self.before_after = before_after
        self.after_before = after_before
        self.instructions = instructions


def is_valid(before_after, after_before, instruction):
    for i, num in enumerate(instruction):
        before = (instruction[:i])
        after = instruction[i+1:]
        if not is_valid_before(after_before, before, num) or not is_valid_after(before_after, after, num):
            return False
    return True

def is_valid_before(after_before, before, num):
    for b in before:
       if num in after_before.get(b, set()):
           return False
    return True

def is_valid_after(before_after, after, num):
    for a in after:
        if num in before_after.get(a, set()):
            return False
    return True

def solution2(data):
    total = 0

    invalid_instructions = []
    for instruction in data.instructions:
        valid = True
        for i, num in enumerate(instruction):
            before = (instruction[:i])
            after = instruction[i+1:]
            # check failure
            for b in before:
                if num in data.after_before.get(b, {}):
                    valid = False
            for a in after:
                if num in data.before_after.get(a, {}):
                    valid = False
        if not valid:
            invalid_instructions.append(instruction)
            
    for i, invalid_instruction in enumerate(invalid_instructions):
        new_sequence = []
        for num in invalid_instruction:
            for i in range(len(new_sequence) + 1):
                before = new_sequence[:i]
                after = new_sequence[i:]
                if is_valid_before(data.after_before, before, num) and is_valid_after(data.before_after, after, num):
                    new_sequence.insert(i, num)
                    break
        
        if not is_valid(data.before_after, data.after_before, new_sequence):
            print("ERROR")

        middle_index = len(new_sequence) // 2
        total += new_sequence[middle_index]
    return total

def solution1(data):
    total = 0
    for instruction in data.instructions:
        valid = True
        for i, num in enumerate(instruction):
            before = (instruction[:i])
            after = instruction[i+1:]
            if not is_valid(data.before_after, data.after_before, instruction):
                valid = False
        if valid:
            middle_index = len(instruction) // 2
            total += instruction[middle_index]
    return total
    
def parse_input(file_name):
    before_after = dict()
    after_before = dict()
    instructions = []
    getting_rules = True
    with open(file_name, "r") as file:
        for line in file:
            if getting_rules:
                if line.strip() == "":
                    getting_rules = False
                    continue
                before, after = tuple(line.strip().split("|"))
                before = int(before)
                after = int(after)
                set_a = before_after.get(before, set())
                set_a.add(after)
                before_after[before] = set_a
                
                set_b = after_before.get(after,set())
                set_b.add(before)
                after_before[after] = set_b
            else:
                instruction = [int(x) for x in line.strip().split(",")]
                instructions.append(instruction)

    return Data(before_after, after_before, instructions)


def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()