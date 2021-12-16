def get_input():
    with open('Day_15_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    row_strings = []
    for line in raw_input:
        row_strings.append(line.rstrip('\n'))
    risk_lvl_smol = {}
    smol_x = len(row_strings[0])
    smol_y = len(row_strings)
    for row in range(len(row_strings)):
        for col in range(len(row_strings[row])):
            risk_lvl_smol[(col, row)] = int(row_strings[row][col])
    big_row_strings = row_strings.copy()
    for inc in range(1, 5):
        for line in range(len(row_strings)):
            for char in row_strings[line]:
                if (int(char) + inc) % 9 != 0:
                    big_row_strings[line] += str((int(char) + inc) % 9)
                else:
                    big_row_strings[line] += '9'
    for inc in range(1, 5):
        for line in range(len(row_strings)):
            big_row_strings.append('')
            for char in range(len(big_row_strings[0])):
                if (int(big_row_strings[line][char]) + inc) % 9 != 0:
                    big_row_strings[-1] += str((int(big_row_strings[line][char]) + inc) % 9)
                else:
                    big_row_strings[-1] += '9'
    risk_lvl_big = {}
    big_x = len(big_row_strings[0])
    big_y = len(big_row_strings)
    for row in range(len(big_row_strings)):
        for col in range(len(big_row_strings[row])):
            risk_lvl_big[(col, row)] = int(big_row_strings[row][col])
    return risk_lvl_smol, smol_x, smol_y, risk_lvl_big, big_x, big_y

def risk_scan(risk_lvls, min_risks, max_x, max_y):
    update = False
    for y in range(max_y):
        for x in range(max_x):
            if x > 0:
                if (min_risks[(x - 1, y)] + risk_lvls[(x, y)]) < min_risks[(x, y)] or min_risks[(x, y)] == 0:
                    min_risks[(x, y)] = min_risks[(x - 1, y)] + risk_lvls[(x, y)]
                    update = True
            if y > 0:
                if (min_risks[(x, y - 1)] + risk_lvls[(x, y)]) < min_risks[(x, y)] or min_risks[(x, y)] == 0:
                    min_risks[(x, y)] = min_risks[(x, y - 1)] + risk_lvls[(x, y)]
                    update = True
            if x < (max_x - 1):
                if (min_risks[x + 1, y] + risk_lvls[(x, y)]) < min_risks[(x, y)] and min_risks[(x + 1, y)] != 0:
                    min_risks[(x, y)] = min_risks[(x + 1, y)] + risk_lvls[(x, y)]
                    update = True
            if y < (max_y - 1):
                if (min_risks[(x, y + 1)] + risk_lvls[(x, y)]) < min_risks[(x, y)] and min_risks[(x, y + 1)] != 0:
                    min_risks[(x, y)] = min_risks[(x, y + 1)] + risk_lvls[(x, y)]
                    update = True
    if update:
        risk_scan(risk_lvls, min_risks, max_x, max_y)
    return min_risks

def main():
    risk_lvl_smol, smol_x, smol_y, risk_lvl_big, big_x, big_y = get_input()
    min_risk_smol = {}
    for y in range(smol_y):
        for x in range(smol_x):
            min_risk_smol[(x, y)] = 0
    min_risk_smol = risk_scan(risk_lvl_smol, min_risk_smol, smol_x, smol_y)
    print(min_risk_smol[(smol_x - 1, smol_y - 1)])
    min_risk_big = {}
    for y in range(big_y):
        for x in range(big_x):
            min_risk_big[(x, y)] = 0
    min_risk_big = risk_scan(risk_lvl_big, min_risk_big, big_x, big_y)
    print(min_risk_big[(big_x - 1, big_y - 1)])

if __name__ == '__main__':
    main()