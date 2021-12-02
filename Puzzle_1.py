import pprint

def get_input_nums():
    with open('puzzle_input.txt') as puzzle_input:
        input_nums = puzzle_input.readlines()
    return input_nums

def count_increases(input_nums):
    count = 0
    for num in range(len(input_nums)):
        if num == 0:
            pass
        else:
            if int(input_nums[num]) > int(input_nums[num - 1]):
                count += 1
            elif int(input_nums[num]) == int(input_nums[num - 1]):
                print('EDGE CASE!!!')
    return count

def main():
    input_nums = get_input_nums()
    increases = count_increases(input_nums)
    print()
    print("Now that you've finished shouting, the number of 'explicit' increases is: {}".format(increases))
    print()

if __name__ == '__main__':
    main()