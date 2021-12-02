def get_input():
    with open('Day_1_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    input = []
    for entry in raw_input:
        input.append(int(entry.rstrip('\n')))
    return input

def count_increases(input_nums):
    count = 0
    for num in range(len(input_nums)):
        if num == 0:
            pass
        else:
            if input_nums[num] > input_nums[num - 1]:
                count += 1
    return count

def rolling_sum(input_nums):
    sum_data = []
    for num in range(len(input_nums)):
        if num == 0 or num == 1:
            pass
        else:
            sum_data.append((input_nums[num] + input_nums[num - 1] + input_nums[num - 2]))
    return sum_data

def main():
    input_data = get_input()
    print(count_increases(input_data))
    sum_data = rolling_sum(input_data)
    print(count_increases(sum_data))

if __name__ == '__main__':
    main()