def get_input():
    with open('Day_3_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    input = []
    for entry in raw_input:
        input.append(entry.rstrip('\n'))
    return input

def gamma_and_epsilon(input_data):
    gamma = ''
    for digit in range(12):
        ones = 0
        zeros = 0
        for num in input_data:
            if num[digit] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
        else:
            gamma += '0'
    epsilon = ~int(gamma, 2) & 4095
    #print('{0}\n{1:b}'.format(gamma, epsilon))
    print(int(gamma, 2) * epsilon)

def oxy_gen(input_data):
    digit = 0
    while len(input_data) > 1:
        ones = 0
        zeros = 0
        for num in input_data:
            if num[digit] == '1':
                ones += 1
            else:
                zeros += 1
        keep = ''
        if ones >= zeros:
            keep = '1'
        else:
            keep = '0'
        new_data = []
        for num in input_data:
            if num[digit] == keep:
                new_data.append(num)
        input_data = new_data
        digit += 1
    return input_data[0]

def co2_scrub(input_data):
    digit = 0
    while len(input_data) > 1:
        ones = 0
        zeros = 0
        for num in input_data:
            if num[digit] == '1':
                ones += 1
            else:
                zeros += 1
        keep = ''
        if zeros <= ones:
            keep = '0'
        else:
            keep = '1'
        new_data = []
        for num in input_data:
            if num[digit] == keep:
                new_data.append(num)
        input_data = new_data
        digit += 1
    return input_data[0]

def main():
    input_data = get_input()
    gamma_and_epsilon(input_data)
    oxy_gen_rating = oxy_gen(input_data)
    co2_scrub_rating = co2_scrub(input_data)
    print(int(oxy_gen_rating, 2) * int(co2_scrub_rating, 2))

if __name__ == '__main__':
    main()