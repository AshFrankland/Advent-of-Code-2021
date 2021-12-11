def get_input():
    with open('Day_11_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input_strings = []
        for line in raw_input:
            input_strings.append(line.rstrip('\n'))
        octos = []
        for line in range(len(input_strings)):
            octos.append([])
            for num in input_strings[line]:
                octos[line].append(int(num))
        return octos

def next_step(octos):
    for row in range(len(octos)):
        for num in range(len(octos[row])):
            octos[row][num] += 1
    return octos

def check_flashes(octos, flashes, r_i, b_i):
    added_one = False
    for row in range(len(octos)):
        for num in range(len(octos[row])):
            if row == 0:
                if num == 0:
                    if octos[0][0] > 9:
                        octos[0][0] = 0
                        if octos[0][1] != 0:
                            octos[0][1] += 1
                            added_one = True
                        if octos[1][0] != 0:
                            octos[1][0] += 1
                            added_one = True
                        if octos[1][1] != 0:
                            octos[1][1] += 1
                            added_one = True
                elif num == r_i:
                    if octos[0][-1] > 9:
                        octos[0][-1] = 0
                        if octos[0][-2] != 0:
                            octos[0][-2] += 1
                            added_one = True
                        if octos[1][-1] != 0:
                            octos[1][-1] += 1
                            added_one = True
                        if octos[1][-2] != 0:
                            octos[1][-2] += 1
                            added_one = True
                else:
                    if octos[0][num] > 9:
                        octos[0][num] = 0
                        if octos[0][num + 1] != 0:
                            octos[0][num + 1] += 1
                            added_one = True
                        if octos[0][num - 1] != 0:
                            octos[0][num - 1] += 1
                            added_one = True
                        if octos[1][num] != 0:
                            octos[1][num] += 1
                            added_one = True
                        if octos[1][num + 1] != 0:
                            octos[1][num + 1] += 1
                            added_one = True
                        if octos[1][num - 1] != 0:
                            octos[1][num - 1] += 1
                            added_one = True
            elif row == b_i:
                if num == 0:
                    if octos[-1][0] > 9:
                        octos[-1][0] = 0
                        if octos[-1][1] != 0:
                            octos[-1][1] += 1
                            added_one = True
                        if octos[-2][0] != 0:
                            octos[-2][0] += 1
                            added_one = True
                        if octos[-2][1] != 0:
                            octos[-2][1] += 1
                            added_one = True
                elif num == r_i:
                    if octos[-1][-1] > 9:
                        octos[-1][-1] = 0
                        if octos[-1][-2] != 0:
                            octos[-1][-2] += 1
                            added_one = True
                        if octos[-2][-1] != 0:
                            octos[-2][-1] += 1
                            added_one = True
                        if octos[-2][-2] != 0:
                            octos[-2][-2] += 1
                            added_one = True
                else:
                    if octos[-1][num] > 9:
                        octos[-1][num] = 0
                        if octos[-1][num + 1] != 0:
                            octos[-1][num + 1] += 1
                            added_one = True
                        if octos[-1][num - 1] != 0:
                            octos[-1][num - 1] += 1
                            added_one = True
                        if octos[-2][num] != 0:
                            octos[-2][num] += 1
                            added_one = True
                        if octos[-2][num + 1] != 0:
                            octos[-2][num + 1] += 1
                            added_one = True
                        if octos[-2][num - 1] != 0:
                            octos[-2][num - 1] += 1
                            added_one = True
            else:
                if num == 0:
                    if octos[row][0] > 9:
                        octos[row][0] = 0
                        if octos[row][1] != 0:
                            octos[row][1] += 1
                            added_one = True
                        if octos[row + 1][0] != 0:
                            octos[row + 1][0] += 1
                            added_one = True
                        if octos[row - 1][0] != 0:
                            octos[row - 1][0] += 1
                            added_one = True
                        if octos[row + 1][1] != 0:
                            octos[row + 1][1] += 1
                            added_one = True
                        if octos[row - 1][1] != 0:
                            octos[row - 1][1] += 1
                            added_one = True
                if num == r_i:
                    if octos[row][-1] > 9:
                        octos[row][-1] = 0
                        if octos[row][-2] != 0:
                            octos[row][-2] += 1
                            added_one = True
                        if octos[row + 1][-1] != 0:
                            octos[row + 1][-1] += 1
                            added_one = True
                        if octos[row - 1][-1] != 0:
                            octos[row - 1][-1] += 1
                            added_one = True
                        if octos[row + 1][-2] != 0:
                            octos[row + 1][-2] += 1
                            added_one = True
                        if octos[row - 1][-2] != 0:
                            octos[row - 1][-2] += 1
                            added_one = True
                else:
                    if octos[row][num] > 9:
                        octos[row][num] = 0
                        if octos[row][num + 1] != 0:
                            octos[row][num + 1] += 1
                            added_one = True
                        if octos[row][num - 1] != 0:
                            octos[row][num - 1] += 1
                            added_one = True
                        if octos[row + 1][num] != 0:
                            octos[row + 1][num] += 1
                            added_one = True
                        if octos[row - 1][num] != 0:
                            octos[row - 1][num] += 1
                            added_one = True
                        if octos[row + 1][num + 1] != 0:
                            octos[row + 1][num + 1] += 1
                            added_one = True
                        if octos[row - 1][num + 1] != 0:
                            octos[row - 1][num + 1] += 1
                            added_one = True
                        if octos[row + 1][num - 1] != 0:
                            octos[row + 1][num - 1] += 1
                            added_one = True
                        if octos[row - 1][num - 1] != 0:
                            octos[row - 1][num - 1] += 1
                            added_one = True
    if added_one:
        check_flashes(octos, flashes, r_i, b_i)
    for row in octos:
        for num in row:
            if num == 0:
                flashes += 1
    return octos, flashes

def check_big_flash(octos):
    for row in octos:
        for num in row:
            if num != 0:
                return False
    return True

def main():
    octos = get_input()
    flashes = 0
    r_i = len(octos[0]) - 1
    b_i = len(octos) - 1
    step = 0
    while True:
        step += 1
        octos = next_step(octos)
        octos, flashes = check_flashes(octos, flashes, r_i, b_i)
        if step == 100:
            print(flashes)
        if check_big_flash(octos):
            print(step)
            break

if __name__ == '__main__':
    main()