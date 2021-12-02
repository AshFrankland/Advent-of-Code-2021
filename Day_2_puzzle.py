def get_input():
    with open('Day_2_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    input = []
    for entry in raw_input:
        input.append(entry.rstrip('\n'))
    return input

def handle_input_old(input_list):
    pos = {'hori': 0, 'depth': 0}
    for entry in input_list:
        if entry[0] == 'f':
            pos['hori'] += int(entry[len(entry) - 1])
        elif entry[0] == 'd':
            pos['depth'] += int(entry[len(entry) - 1])
        elif entry[0] == 'u':
            pos['depth'] -= int(entry[len(entry) - 1])
    return pos

def handle_input_new(input_list):
    aim = 0
    pos = {'hori': 0, 'depth': 0}
    for entry in input_list:
        if entry[0] == 'f':
            pos['hori'] += int(entry[len(entry) - 1])
            pos['depth'] += aim * int(entry[len(entry) - 1])
        elif entry[0] == 'd':
            aim += int(entry[len(entry) - 1])
        elif entry[0] == 'u':
            aim -= int(entry[len(entry) - 1])
    return pos

def main():
    input_list = get_input()
    final_pos_old = handle_input_old(input_list)
    final_pos_new = handle_input_new(input_list)
    print(final_pos_old['hori'] * final_pos_old['depth'])
    print(final_pos_new['hori'] * final_pos_new['depth'])

if __name__ == '__main__':
    main()