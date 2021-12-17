def get_input():
    with open('Day_17_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    x_target = ()
    y_target = ()
    for line in raw_input:
        if line[0] == 'x':
            x = line.rstrip('\n').lstrip('x=')
            x = x.split(',')
            x_target = (int(x[0]), int(x[1]))
        else:
            y = line.rstrip('\n').lstrip('y=')
            y = y.split(',')
            y_target = (int(y[0]), int(y[1]))
    return x_target, y_target

def highest_y(y_target):
    highest_point = [0]
    valid_y = []
    for y_start in range(-200, 200):
        y_vel = y_start
        y_pos = 0
        while y_pos > y_target[1]:
            y_pos += y_vel
            y_vel -= 1
            if y_vel < 1 and len(highest_point) < 2:
                highest_point.append(y_pos)
        if y_pos >= y_target[0]:
            valid_y.append(y_start)
            if highest_point[1] >= highest_point[0]:
                highest_point.pop(0)
            else:
                highest_point.pop(1)
        else:
            highest_point.pop(1)
    return highest_point[0], valid_y

def target_hits(x_target, y_target, valid_y):
    hit_count = 0
    for y_start in valid_y:
        for x_start in range(100):
            pos = [0, 0]
            x_vel = x_start
            y_vel = y_start
            while pos[0] <= x_target[1] and pos[1] >= y_target[0]:
                pos[0] += x_vel
                pos[1] += y_vel
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1
                if pos[0] >= x_target[0] and pos[0] <= x_target[1] and pos[1] >= y_target[0] and pos[1] <= y_target[1]:
                    hit_count += 1
                    break
    return hit_count

def main():
    x_target, y_target = get_input()
    highest_point, valid_y = highest_y(y_target)
    print(highest_point)
    hit_count = target_hits(x_target, y_target, valid_y)
    print(hit_count)

if __name__ == '__main__':
    main()