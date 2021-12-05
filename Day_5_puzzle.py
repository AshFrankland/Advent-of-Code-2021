import pprint

def get_input():
    with open('Day_5_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        coordinate_strings = []
        for num_pair in raw_input:
            coordinate_strings.append(num_pair.rstrip('\n').split(' -> '))
        coordinates = []
        for line_pair in coordinate_strings:
            for coordinate in line_pair:
                coordinates.append(coordinate.split(','))
        return coordinates

def gen_grid():
    grid = []
    for row in range(1000):
        grid.append([])
    for row in grid:
        for col in range(1000):
            row.append(0)
    return grid

def draw_lines(grid, coordinates):
    for pair in range(len(coordinates)):
        num_vents = 0
        smallest_ordinate = 0
        if pair % 2 == 1:
            pass
        elif coordinates[pair][0] == coordinates[pair + 1][0]:
            if int(coordinates[pair][1]) == int(coordinates[pair + 1][1]):
                num_vents = 1
                smallest_ordinate = int(coordinates[pair][1])
            elif int(coordinates[pair][1]) > int(coordinates[pair + 1][1]):
                num_vents = int(coordinates[pair][1]) - int(coordinates[pair + 1][1]) + 1
                smallest_ordinate = int(coordinates[pair + 1][1])
            elif int(coordinates[pair][1]) < int(coordinates[pair + 1][1]):
                num_vents = int(coordinates[pair + 1][1]) - int(coordinates[pair][1]) + 1
                smallest_ordinate = int(coordinates[pair][1])
            for vent in range(num_vents):
                grid[smallest_ordinate + vent][int(coordinates[pair][0])] += 1
        elif coordinates[pair][1] == coordinates[pair + 1][1]:
            if int(coordinates[pair][0]) > int(coordinates[pair + 1][0]):
                num_vents = int(coordinates[pair][0]) - int(coordinates[pair + 1][0]) + 1
                smallest_ordinate = int(coordinates[pair + 1][0])
            elif int(coordinates[pair][0]) < int(coordinates[pair + 1][0]):
                num_vents = int(coordinates[pair + 1][0]) - int(coordinates[pair][0]) + 1
                smallest_ordinate = int(coordinates[pair][0])
            for vent in range(num_vents):
                grid[int(coordinates[pair][1])][smallest_ordinate + vent] += 1
    return grid

def draw_diagonals(grid, coordinates):
    for pair in range(len(coordinates)):
        x = 0
        y = 0
        grad = 0
        if pair % 2 == 1:
            pass
        elif coordinates[pair][0] == coordinates[pair + 1][0] or coordinates[pair][1] == coordinates[pair + 1][1]:
            pass
        else:
            if int(coordinates[pair][0]) < int(coordinates[pair + 1][0]):
                x = int(coordinates[pair][0])
                y = int(coordinates[pair][1])
                if int(coordinates[pair][1]) < int(coordinates[pair + 1][1]):
                    grad = 1
                else:
                    grad = -1
            elif int(coordinates[pair][0]) > int(coordinates[pair + 1][0]):
                x = int(coordinates[pair + 1][0])
                y = int(coordinates[pair + 1][1])
                if int(coordinates[pair + 1][1]) < int(coordinates[pair][1]):
                    grad = 1
                else:
                    grad = -1
            ends = 0
            while True:
                if x == int(coordinates[pair][0]) or x == int(coordinates[pair + 1][0]):
                    ends += 1
                grid[y][x] += 1
                x += 1
                y += grad
                if ends == 2:
                    break
    return grid

def count_overlaps(grid):
    count = 0
    for row in grid:
        for num in row:
            if num > 1:
                count += 1
    return count

def main():
    coordinates = get_input()
    grid = gen_grid()
    grid = draw_lines(grid, coordinates)
    count = count_overlaps(grid)
    print(count)
    grid = draw_diagonals(grid, coordinates)
    count = count_overlaps(grid)
    print(count)

if __name__ == '__main__':
    main()