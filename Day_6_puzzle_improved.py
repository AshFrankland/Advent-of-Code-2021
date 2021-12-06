def get_input():
    with open('Day_6_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        fish_strings = raw_input[0].split(',')
        fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for num in fish_strings:
            fish_dict[int(num)] += 1
        return fish_dict

def new_day(fish_dict):
    fish_dict = {
        0: fish_dict[1],
        1: fish_dict[2],
        2: fish_dict[3],
        3: fish_dict[4],
        4: fish_dict[5],
        5: fish_dict[6],
        6: fish_dict[7] + fish_dict[0],
        7: fish_dict[8],
        8: fish_dict[0]
    }
    return fish_dict

def main():
    fish_dict = get_input()
    for day in range(80):
        fish_dict = new_day(fish_dict)
    count = 0
    for key in fish_dict:
        count += fish_dict[key]
    print(count)
    for day in range(256 - 80):
        fish_dict = new_day(fish_dict)
    count = 0
    for key in fish_dict:
        count += fish_dict[key]
    print(count)

if __name__ == '__main__':
    main()