def get_input():
    with open('Day_8_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    code_pairs = []
    for code in raw_input:
        code_pair = code.rstrip('\n').split(' | ')
        code_pairs.append(code_pair)
    return code_pairs

def count_ez_nums(code_pairs):
    count = 0
    for code_pair in code_pairs:
        output_nums = code_pair[1].split()
        for digit in output_nums:
            if len(digit) == 5 or len(digit) == 6:
                pass
            else:
                count += 1
    return count

def get_length(str):
    return len(str)

def deduce_digits(code_pairs):
    output_digits = []
    for code_pair in code_pairs:
        code_dict = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set(), 9:set()}
        test_codes = code_pair[0].split()
        test_codes.sort(key=get_length)
        one = list(test_codes[0])
        code_dict[1] = set(one)
        test_codes.pop(0)
        seven = list(test_codes[0])
        code_dict[7] = set(seven)
        test_codes.pop(0)
        four = list(test_codes[0])
        code_dict[4] = set(four)
        test_codes.pop(0)
        eight = list(test_codes[6])
        code_dict[8] = set(eight)
        test_codes.pop()
        for num in range(3):
            count = 0
            for char in one:
                if char in set(test_codes[num]):
                    count += 1
            if count == 2:
                three = list(test_codes[num])
                code_dict[3] = set(three)
                test_codes.pop(num)
                break
        for num in range(2, 5):
            count = 0
            for char in one:
                if char in set(test_codes[num]):
                    count += 1
            if count == 1:
                six = list(test_codes[num])
                code_dict[6] = set(six)
                test_codes.pop(num)
                break
        count = [0, 0]
        for char in four:
            if char in set(test_codes[0]):
                count[0] += 1
            if char in set(test_codes[2]):
                count[1] += 1
        if count[0] == 2:
            two = list(test_codes[0])
            five = list(test_codes[1])
            code_dict[2] = set(two)
            code_dict[5] = set(five)
        else:
            two = list(test_codes[1])
            five = list(test_codes[0])
            code_dict[2] = set(two)
            code_dict[5] = set(five)
        if count[1] == 3:
            zero = list(test_codes[2])
            nine = list(test_codes[3])
            code_dict[0] = set(zero)
            code_dict[9] = set(nine)
        else:
            zero = list(test_codes[3])
            nine = list(test_codes[2])
            code_dict[0] = set(zero)
            code_dict[9] = set(nine)
        digits = ''
        real_codes = code_pair[1].split()
        for code in real_codes:
            for key in code_dict:
                if set(code) == code_dict[key]:
                    digits += str(key)
                    break
        output_digits.append(int(digits))
    return output_digits

def main():
    code_pairs = get_input()
    ez_count = count_ez_nums(code_pairs)
    print(ez_count)
    output_digits = deduce_digits(code_pairs)
    print(sum(output_digits))

if __name__ == '__main__':
    main()