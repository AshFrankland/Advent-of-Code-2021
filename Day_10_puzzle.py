def get_input():
    with open('Day_10_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    puzzle_input = []
    for line in raw_input:
        puzzle_input.append(line.rstrip('\n'))
    return puzzle_input

def find_corrupt(puzzle_input):
    corrupt_chars = {')': 0, ']': 0, '}': 0, '>': 0}
    open_chars = {'(', '[', '{', '<'}
    index_offset = 0
    for index in range(len(puzzle_input)):
        open_list = []
        for char in puzzle_input[index - index_offset]:
            if char in open_chars:
                open_list.append(char)
            else:
                if char == ')' and open_list[-1] == '(':
                    open_list.pop()
                elif char == ']' and open_list[-1] == '[':
                    open_list.pop()
                elif char == '}' and open_list[-1] == '{':
                    open_list.pop()
                elif char == '>' and open_list[-1] == '<':
                    open_list.pop()
                else:
                    corrupt_chars[char] += 1
                    puzzle_input.pop(index - index_offset)
                    index_offset += 1
                    break
    return corrupt_chars, puzzle_input

def complete_lines(puzzle_input):
    line_scores = []
    open_chars = {'(', '[', '{', '<'}
    char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    for line in puzzle_input:
        open_list = []
        completion_list = []
        score = 0
        for char in line:
            if char in open_chars:
                open_list.append(char)
            else:
                if char == ')' and open_list[-1] == '(':
                    open_list.pop()
                elif char == ']' and open_list[-1] == '[':
                    open_list.pop()
                elif char == '}' and open_list[-1] == '{':
                    open_list.pop()
                elif char == '>' and open_list[-1] == '<':
                    open_list.pop()
        while open_list:
            if open_list[-1] == '(':
                completion_list.append(')')
                open_list.pop()
            elif open_list[-1] == '[':
                completion_list.append(']')
                open_list.pop()
            elif open_list[-1] == '{':
                completion_list.append('}')
                open_list.pop()
            elif open_list[-1] == '<':
                completion_list.append('>')
                open_list.pop()
        for char in completion_list:
            score *= 5
            score += char_scores[char]
        line_scores.append(score)
    line_scores.sort()
    middle_score = line_scores[len(line_scores) // 2]
    return middle_score

def main():
    puzzle_input = get_input()
    corrupt_chars, puzzle_input = find_corrupt(puzzle_input)
    print((corrupt_chars[')'] * 3) + (corrupt_chars[']'] * 57) + (corrupt_chars['}'] * 1197) + (corrupt_chars['>'] * 25137))
    middle_score = complete_lines(puzzle_input)
    print(middle_score)

if __name__ == '__main__':
    main()