def get_input():
    with open('Day_14_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    fusions = False
    polymer = []
    insert_key = {}
    for line in raw_input:
        if fusions:
            insert = line.rstrip('\n')
            insert_key[insert[0] + insert[1]] = (insert[0], insert[-1], insert[1])
        elif line == '\n':
            fusions = True
        else:
            polymer = line.rstrip('\n')
    ele_count = {}
    for ele in polymer:
        if ele in ele_count:
            ele_count[ele] += 1
        else:
            ele_count[ele] = 1
    for ele in insert_key.values():
        if ele[1] not in ele_count:
            ele_count[ele[1]] = 0
    ele_pairs = {}
    for ele in range(len(polymer) - 1):
        if (polymer[ele] + polymer[ele + 1]) in ele_pairs:
            ele_pairs[polymer[ele] + polymer[ele + 1]] += 1
        else:
            ele_pairs[polymer[ele] + polymer[ele + 1]] = 1
    return ele_count, ele_pairs, insert_key

def next_step(ele_count, ele_pairs, insert_key):
    new_pairs = {}
    for pair in ele_pairs:
        count = ele_pairs[pair]
        ele_count[insert_key[pair][1]] += count
        if (insert_key[pair][0] + insert_key[pair][1]) in new_pairs:
            new_pairs[insert_key[pair][0] + insert_key[pair][1]] += count
        else:
            new_pairs[insert_key[pair][0] + insert_key[pair][1]] = count
        if (insert_key[pair][1] + insert_key[pair][2]) in new_pairs:
            new_pairs[insert_key[pair][1] + insert_key[pair][2]] += count
        else:
            new_pairs[insert_key[pair][1] + insert_key[pair][2]] = count
    return ele_count, new_pairs

def main():
    ele_count, ele_pairs, insert_key = get_input()
    for step in range(10):
        ele_count, ele_pairs = next_step(ele_count, ele_pairs, insert_key)
    first_count = []
    for ele in ele_count.values():
        first_count.append(ele)
    first_count.sort()
    print(first_count[-1] - first_count[0])
    for step in range(30):
        ele_count, ele_pairs = next_step(ele_count, ele_pairs, insert_key)
    final_count = []
    for ele in ele_count.values():
        final_count.append(ele)
    final_count.sort()
    print(final_count[-1] - final_count[0])

if __name__ == '__main__':
    main()