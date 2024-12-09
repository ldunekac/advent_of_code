import sys
from copy import deepcopy

def pare_for_part2(instructions):
    file_locations = []
    current_index = 0
    file_id = 0
    for i, val in enumerate(instructions):
        val = int(val)
        if i % 2 == 0: # is a file
            file_locations.append((file_id, current_index, val))
            file_id += 1
            current_index += val
        else:
            current_index += val

    file_locations_with_free_space_attached = []
    for left, right in zip(file_locations, file_locations[1:]):
        free_space = right[1] - (left[1] + left[2])
        file_locations_with_free_space_attached.append([left[0], left[1], left[2], free_space])

    last = file_locations[-1]
    file_locations_with_free_space_attached.append([last[0], last[1], last[2], 0])
    return file_locations_with_free_space_attached


def solution2(instructions):
    instructions = pare_for_part2(instructions)

    # loop though reverse indexes
    current_file_id = instructions[-1][0]
    for id in range(current_file_id, -1, -1):
        if id == 0:
            break
        # print(id)
        i = 0
        val = None
        # Find the next file index to work with
        for i, val in enumerate(instructions):
            if val[0] == id:
                break

        # Loop though the list to see if it can be inserted
        for j, potential_spot in enumerate(instructions):

            if potential_spot[1] >= val[1]: # if the current open stop is farther away
                break
            # Loop through the list to find free space
            elif potential_spot[3] >= val[2]: # found a spot
                # print(f"before: {instructions}")
                # print(f"Found a spot {potential_spot}")
                # Update the new free positions
                free_space = potential_spot[3]
                potential_spot[3] = 0 # potential spot has no more free space

                move_block_free_space = val[3]
                move_block_num_digits = val[2]
                remain_free_space = free_space - (move_block_num_digits)
                inserted_block = [val[0], potential_spot[1] + potential_spot[2], val[2], remain_free_space]

                instructions[i-1][3] = instructions[i-1][3] + move_block_free_space +  move_block_num_digits

                instructions.insert(j+1, inserted_block)

                instructions = instructions[0:i+1] + instructions[i+2:]
                break
                # * zero for the prev block
                # * remaining for the new moving block
                # * Add in free to the part that was removed
                # insert it
        # print(f"after: {instructions}")


    # print(instructions)
    total = 0
    for val in instructions:
        for j in range(val[2]):
            total += (val[1] + j) * val[0]
    return total

def parse_file_locations(instructions):
    file_locations = []
    current_index = 0
    file_id = 0
    for i, val in enumerate(instructions):
        val = int(val)
        if i % 2 == 0: # is a file
            file_locations.append((file_id, current_index, val))
            file_id += 1
            current_index += val
        else:
            current_index += val
    return file_locations

def solution1(instructions):
    file_locations = parse_file_locations(instructions)
    # print(file_locations)
    total = 0
    f_i = 0
    current_location = file_locations.pop(0)
    while True:
        # print(f"{f_i=} {total=}")
        # print(current_location)
        if current_location is None:
            return total
        if current_location[1] <= f_i < current_location[1] + current_location[2]:
            # print("In memory")
            total += f_i * current_location[0]
            f_i += 1
        elif f_i == current_location[1] + current_location[2]:
            # print("Wat")
            if len(file_locations) == 0:
                return total
            current_location = file_locations.pop(0)
            if current_location is None:
                return total
        elif f_i < current_location[1]: # Need to pull from the back to fill in space
            # print("filling empty space")
            last = file_locations[-1] if len(file_locations) > 0 else current_location
            update_last = (last[0], last[1], last[2] - 1)
            total += f_i * last[0]
            f_i += 1
            if len(file_locations) > 0:
                if last[2] - 1 == 0:
                    file_locations = file_locations[:-1]
                else:
                    file_locations[-1] = update_last
            else:
                if update_last[2] == 0:
                    return total
                current_location = update_last

    return total

def parse_input(file_name):
    with open(file_name, "r") as file:
        return file.read().strip()

def main():
    sol_num = int(sys.argv[1])
    input_file = sys.argv[2]
    input_data = parse_input(input_file)
    answer = solution1(input_data) if sol_num == 1 else solution2(input_data)

    print(f"Solution to Part {sol_num} for {input_file} is: {answer}")

if __name__ == "__main__":
    main()