def get_input():
    with open('Day_12_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
    caves = []
    for line in raw_input:
        cave = line.rstrip('\n')
        caves.append(cave.split('-'))
    return caves

def get_paths(caves):
    paths = {}
    for pair in caves:
        for cave in pair:
            paths[cave] = []
    for pair in caves:
        paths[pair[0]].append(pair[1])
        paths[pair[1]].append(pair[0])
    #cull_dead_ends(paths)
    paths.pop('end')
    for cave in paths:
        if 'start' in paths[cave]:
            paths[cave].remove('start')
    return paths

def cull_dead_ends(paths):
    dead_end_found = False
    for cave in paths:
        if len(paths[cave]) == 1 and paths[cave][0].islower():
            for c in paths:
                if cave in paths[c]:
                    paths[c].remove(cave)
            paths.pop(cave)
            dead_end_found = True
            break
    if dead_end_found:
        cull_dead_ends(paths)

def find_routes_old(paths, routes, visited_caves, current_cave):
    visited_caves.append(current_cave)
    for cave in paths[current_cave]:
        if cave == 'end':
            visited_caves.append(cave)
            routes.append(visited_caves.copy())
            visited_caves.pop()
        elif not (cave.islower() and cave in visited_caves):
            find_routes_old(paths, routes, visited_caves, cave)
    visited_caves.pop()
    if not visited_caves:
        return routes

def find_routes_new(paths, routes, visited_caves, current_cave):
    if current_cave.islower() and current_cave in visited_caves:
        visited_caves.append('2')
    else:
        visited_caves.append(current_cave)
    for cave in paths[current_cave]:
        if cave == 'end':
            visited_caves.append(cave)
            routes.append(visited_caves.copy())
            visited_caves.pop()
        elif not (cave.islower() and '2' in visited_caves and cave in visited_caves):
            find_routes_new(paths, routes, visited_caves, cave)
    visited_caves.pop()
    if not visited_caves:
        return routes

def main():
    caves = get_input()
    paths = get_paths(caves)
    routes = []
    start_cave = 'start'
    visited_caves = []
    routes = find_routes_old(paths, routes, visited_caves, start_cave)
    print(len(routes))
    routes = []
    routes = find_routes_new(paths, routes, visited_caves, start_cave)
    print(len(routes))

if __name__ == '__main__':
    main()