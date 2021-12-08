def get_input():
    with open('Day_7_input.txt') as puzzle_input:
        raw_input = puzzle_input.read()
    crab_strings = raw_input.split(',')
    crab_nums = []
    for num in crab_strings:
        crab_nums.append(int(num))
    return crab_nums

def align_crabs_old(crab_nums):
    big_num = 0
    for num in crab_nums:
        if num > big_num:
            big_num = num
    fuel_min = False
    for pos in range(big_num + 1):
        fuel_count = 0
        for num in crab_nums:
            fuel_count += abs(num - pos)
        if fuel_min:
            if fuel_count < fuel_min:
                fuel_min = fuel_count
        else:
            fuel_min = fuel_count
    return fuel_min

def align_crabs_new(crab_nums):
    big_num = 0
    for num in crab_nums:
        if num > big_num:
            big_num = num
    fuel_min = False
    for pos in range(big_num + 1):
        fuel_count = 0
        for num in crab_nums:
            fuel_count += sum(range(abs(num - pos) + 1))
        if fuel_min:
            if fuel_count < fuel_min:
                fuel_min = fuel_count
        else:
            fuel_min = fuel_count
    return fuel_min

def main():
    crab_nums = get_input()
    fuel_min_old = align_crabs_old(crab_nums)
    print(fuel_min_old)
    fuel_min_new = align_crabs_new(crab_nums)
    print(fuel_min_new)

if __name__ == '__main__':
    main()