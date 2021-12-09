def get_input():
    with open('Day_9_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    heatmap_strings = []
    for line in raw_input:
        heatmap_strings.append(list(line.rstrip('\n')))
    heatmap = []
    for list_index in range(len(heatmap_strings)):
        heatmap.append([])
        for num_string in heatmap_strings[list_index]:
            heatmap[list_index].append(int(num_string))
    return heatmap

def check_corners(heatmap, low_coords):
    bottom_index = len(heatmap) - 1
    right_index = len(heatmap[0]) -1
    if heatmap[0][0] < heatmap[0][1] and heatmap[0][0] < heatmap[1][0]:
        low_coords.append((0, 0))
    if heatmap[0][right_index] < heatmap[0][right_index - 1] and heatmap[0][right_index] < heatmap[1][right_index]:
        low_coords.append((0, right_index))
    if heatmap[bottom_index][0] < heatmap[bottom_index][1] and heatmap[bottom_index][0] < heatmap[bottom_index - 1][0]:
        low_coords.append((bottom_index, 0))
    if heatmap[bottom_index][right_index] < heatmap[bottom_index][right_index - 1] and heatmap[bottom_index][right_index] < heatmap[bottom_index - 1][right_index]:
        low_coords.append((bottom_index, right_index))
    return low_coords

def check_edges(heatmap, low_coords):
    bottom_index = len(heatmap) - 1
    right_index = len(heatmap[0]) - 1
    for num in range(1, right_index):
        if heatmap[0][num] < heatmap[0][num - 1] and heatmap[0][num] < heatmap[0][num + 1] and heatmap[0][num] < heatmap[1][num]:
            low_coords.append((0, num))
        if heatmap[bottom_index][num] < heatmap[bottom_index][num - 1] and heatmap[bottom_index][num] < heatmap[bottom_index][num + 1] and heatmap[bottom_index][num] < heatmap[bottom_index - 1][num]:
            low_coords.append((bottom_index, num))
    for num in range(1, bottom_index):
        if heatmap[num][0] < heatmap[num - 1][0] and heatmap[num][0] < heatmap[num + 1][0] and heatmap[num][0] < heatmap[num][1]:
            low_coords.append((num, 0))
        if heatmap[num][right_index] < heatmap[num - 1][right_index] and heatmap[num][right_index] < heatmap[num + 1][right_index] and heatmap[num][right_index] < heatmap[num][right_index - 1]:
            low_coords.append((num, right_index))
    return low_coords

def check_centres(heatmap, low_coords):
    b_i = len(heatmap) - 1
    r_i = len(heatmap[0]) - 1
    for row in range(1, b_i):
        for num in range(1, r_i):
            if heatmap[row][num] < heatmap[row][num - 1] and heatmap[row][num] < heatmap[row][num + 1] and heatmap[row][num] < heatmap[row - 1][num] and heatmap[row][num] < heatmap[row + 1][num]:
                low_coords.append((row, num))
    return low_coords

def calculate_risk(heatmap, low_coords):
    risk = 0
    for coord in low_coords:
        risk += heatmap[coord[0]][coord[1]] + 1
    return risk

def find_basins(heatmap, low_coords):
    basin_sizes = []
    b_i = len(heatmap) - 1
    r_i = len(heatmap[0]) - 1
    for coord in low_coords:
        basin_coords = {coord}
        basin_coords = get_basin(heatmap, coord, basin_coords, b_i, r_i)
        basin_sizes.append(len(basin_coords))
    return basin_sizes

def get_basin(heatmap, coord, basin_coords, b_i, r_i):
    if coord[0] > 0:
        if heatmap[coord[0] - 1][coord[1]] > heatmap[coord[0]][coord[1]] and heatmap[coord[0] - 1][coord[1]] < 9 and (coord[0] - 1, coord[1]) not in basin_coords:
            basin_coords.add((coord[0] - 1, coord[1]))
            basin_coords = get_basin(heatmap, (coord[0] - 1, coord[1]), basin_coords, b_i, r_i)
    if coord[1] > 0:
        if heatmap[coord[0]][coord[1] - 1] > heatmap[coord[0]][coord[1]] and heatmap[coord[0]][coord[1] - 1] < 9 and (coord[0], coord[1] - 1) not in basin_coords:
            basin_coords.add((coord[0], coord[1] - 1))
            basin_coords = get_basin(heatmap, (coord[0], coord[1] - 1), basin_coords, b_i, r_i)
    if coord[0] < b_i:
        if heatmap[coord[0] + 1][coord[1]] > heatmap[coord[0]][coord[1]] and heatmap[coord[0] + 1][coord[1]] < 9 and (coord[0] + 1, coord[1]) not in basin_coords:
            basin_coords.add((coord[0] + 1, coord[1]))
            basin_coords = get_basin(heatmap, (coord[0] + 1, coord[1]), basin_coords, b_i, r_i)
    if coord[1] < r_i:
        if heatmap[coord[0]][coord[1] + 1] > heatmap[coord[0]][coord[1]] and heatmap[coord[0]][coord[1] + 1] < 9 and (coord[0], coord[1] + 1) not in basin_coords:
            basin_coords.add((coord[0], coord[1] + 1))
            basin_coords = get_basin(heatmap, (coord[0], coord[1] + 1), basin_coords, b_i, r_i)
    return basin_coords

def main():
    heatmap = get_input()
    low_coords = []
    low_coords = check_corners(heatmap, low_coords)
    low_coords = check_edges(heatmap, low_coords)
    low_coords = check_centres(heatmap, low_coords)
    risk = calculate_risk(heatmap, low_coords)
    print(risk)
    basin_sizes = find_basins(heatmap, low_coords)
    basin_sizes = sorted(basin_sizes)
    basin_sizes.reverse()
    big_basins = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(big_basins)

if __name__ == '__main__':
    main()