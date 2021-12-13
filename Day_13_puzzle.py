def get_input():
    with open('Day_13_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    dot_pairs = []
    fold_strings = []
    gap = False
    for line in raw_input:
        if line == '\n':
            gap = True
        elif gap:
            fold_strings.append(line.rstrip('\n'))
        else:
            dot_pairs.append(line.rstrip('\n'))
    dot_strings = []
    folds = []
    for pair in dot_pairs:
        dot_strings.append(pair.split(','))
    for fold in fold_strings:
        folds.append(fold.lstrip('fold along '))
    dots = []
    for coord in dot_strings:
        dots.append([])
        for ord in coord:
            dots[-1].append(int(ord))
    return dots, folds

def fold(dots, folds):
    if folds[0][0] == 'x':
        fold_dir = 0
        fold_line = int(folds[0].lstrip('x='))
    else:
        fold_dir = 1
        fold_line = int(folds[0].lstrip('y='))
    for dot in dots:
        if dot[fold_dir] > fold_line:
            dot[fold_dir] = fold_line - (dot[fold_dir] - fold_line)
    new_dots = []
    for dot in dots:
        if dot not in new_dots:
            new_dots.append(dot)
    folds.pop(0)
    return new_dots, folds

def make_grid(dots):
    grid = []
    for row in range(6):
        grid.append([])
        for col in range(40):
            grid[-1].append('.')
    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    return grid

def main():
    dots, folds = get_input()
    dots, folds = fold(dots, folds)
    print(len(dots))
    while folds:
        dots, folds = fold(dots, folds)
    grid = make_grid(dots)
    for row in grid:
        print(row)

if __name__ == '__main__':
    main()