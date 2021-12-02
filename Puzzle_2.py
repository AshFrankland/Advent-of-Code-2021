import pprint

def get_input_nums():
    with open('puzzle_input.txt') as puzzle_input:
        input_nums = puzzle_input.readlines()
    return input_nums

def rolling_sum(input_data):
    scan_data = []
    for num in range(len(input_data)):
        if num == 0 or num == 1:
            pass
        else:
            scan_data.append((int(input_data[num]) + int(input_data[num - 1]) + int(input_data[num - 2])))
    return scan_data

def count_increases(scan_data):
    count = 0
    for num in range(len(scan_data)):
        if num == 0:
            pass
        else:
            if scan_data[num] > scan_data[num - 1]:
                count += 1
            # elif scan_data[num] == scan_data[num - 1]:
            #     print('EDGE CASE!!!')
    return count

def main():
    input_nums = get_input_nums()
    scan_data = rolling_sum(input_nums)
    increases = count_increases(scan_data)
    print()
    print("The number of times the rolling sum increases is: {}".format(increases))
    print()

if __name__ == '__main__':
    main()