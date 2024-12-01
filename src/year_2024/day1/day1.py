
def solution2(list1, list2):
    list1.sort()
    list2.sort()
    similarity_multiplier = {}
    for num in list2:
        multiplier = similarity_multiplier.get(num, 0)
        multiplier += 1
        similarity_multiplier[num] = multiplier

    return sum(num * similarity_multiplier.get(num,0) for num in list1)


def solution1(list1, list2):
    list1.sort()
    list2.sort()
    return sum(abs(a-b) for a,b in zip(list1, list2))

def read_input(filename):
    list1, list2 = [], []
    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            assert len(line) == 2
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    return list1, list2


def main():
    inputfile = "example.txt"
    list1, list2 = read_input(inputfile)
    answer = solution1(list1, list2)
    print(f"Solution to part 1 example: {answer}")

    inputfile = "input.txt"
    list1, list2 = read_input(inputfile)
    answer = solution1(list1, list2)
    print(f"Solution to part 1 input: {answer}")

    inputfile = "example.txt"
    list1, list2 = read_input(inputfile)
    answer = solution2(list1, list2)
    print(f"Solution to part 2 example: {answer}")

    inputfile = "input.txt"
    list1, list2 = read_input(inputfile)
    answer = solution2(list1, list2)
    print(f"Solution to part 2 input: {answer}")


if __name__ == "__main__":
    main()