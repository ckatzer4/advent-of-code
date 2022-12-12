import sys
import time

test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

def parse_map(lines):
    hill = dict()
    for (r,l) in enumerate(lines):
        for (c,char) in enumerate(l):
            if char == 'S':
                start = (r,c)
            hill[(r,c)] = char
    return hill, start

DIRS = [(0,1), (-1,0), (0,-1), (1,0)]

def neighbors(hill, coord, unvisited):
    (r,c) = coord
    for (dr, dc) in DIRS:
        neighbor = (r+dr, c+dc)
        if (not neighbor in unvisited):
            continue
        can_climb = (ord(hill[neighbor])-ord(hill[coord])) <=1 and hill[neighbor] != 'E'
        is_first_step = hill[coord] == 'S' and hill[neighbor] == 'a'
        is_last_step = hill[coord] == 'z' and hill[neighbor] == 'E'
        if can_climb or is_first_step or is_last_step:
            yield neighbor

def search(hill, start):
    shortest_path = {c:999999999 for c in hill}
    unvisited = {c for c in hill}
    shortest_path[start] = 0
    tic = time.perf_counter()
    toc = time.perf_counter()
    while unvisited:
        coord = min(unvisited, key=lambda u: shortest_path[u])
        for opt in neighbors(hill, coord, unvisited):
            if shortest_path[opt] > shortest_path[coord]+1:
                shortest_path[opt] = shortest_path[coord]+1
        unvisited.remove(coord)
    return shortest_path

def search_any_a(hill, start):
    shortest_path = {c:999999999 for c in hill}
    unvisited = {c for c in hill}
    shortest_path[start] = 0
    for c, v in hill.items():
        if v == 'a':
            shortest_path[c] = 0
    while unvisited:
        coord = min(unvisited, key=lambda u: shortest_path[u])
        for opt in neighbors(hill, coord, unvisited):
            if shortest_path[opt] > shortest_path[coord]+1:
                shortest_path[opt] = shortest_path[coord]+1
        unvisited.remove(coord)
    return shortest_path

def part1(hill, start):
    shortest_path = search(hill, start)
    e_coord = next(c for c in hill if hill[c]=='E')
    return shortest_path[e_coord]

def part2(hill, _start):
    shortest_path = search_any_a(hill, start)
    e_coord = next(c for c in hill if hill[c]=='E')
    return shortest_path[e_coord]

if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    (hill, start) = parse_map(lines)
    print(f"Part 1: {part1(hill, start)}")
    print(f"Part 2: {part2(hill, start)}")
    # p2: 513 too high
