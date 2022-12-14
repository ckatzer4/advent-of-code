import sys

test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

def parse_rock(lines):
    grid = dict()
    for l in lines:
        pairs = [p.split(',') for p in l.split(' -> ')]
        pairs = [(int(p1), int(p2)) for (p1,p2) in pairs]
        for i in range(1,len(pairs)):
            ((sc,sr),(ec,er)) = (pairs[i-1], pairs[i])
            if sr == er:
                if sc < ec:
                    for c in range(sc,ec+1):
                        grid[(c,sr)] = '#'
                elif sc > ec:
                    for c in range(ec,sc+1):
                        grid[(c,sr)] = '#'
                else:
                    grid[(sc,sr)] = '#'
            elif sc == ec:
                if sr < er:
                    for r in range(sr,er+1):
                        grid[(sc,r)] = '#'
                elif sr > er:
                    for r in range(er,sr+1):
                        grid[(sc,r)] = '#'
                else:
                    grid[(sc,sr)] = '#'
    return grid

def part1(grid):
    sand_free = False
    sand_count = 0
    void = max(r for (c,r) in grid)+1
    while not sand_free:
        sand = (500,0)
        falling = True
        while falling:
            for (dc,dr) in [(0,1),(-1,1),(1,1)]:
                fall_pos = (sand[0]+dc, sand[1]+dr)
                if fall_pos not in grid:
                    sand = fall_pos
                    break
            else: #nobreak
                grid[sand] = 'o'
                sand_count += 1
                falling = False
            if sand[1] == void:
                sand_free = True
                break
    return sand_count

def part2(lines):
    sand_stuck = False
    sand_count = 0
    floor = max(r for (c,r) in grid)+2
    while not sand_stuck:
        sand = (500,0)
        falling = True
        while falling:
            for (dc,dr) in [(0,1),(-1,1),(1,1)]:
                fall_pos = (sand[0]+dc, sand[1]+dr)
                if not fall_pos[1] == floor and fall_pos not in grid:
                    sand = fall_pos
                    break
            else: #nobreak
                grid[sand] = 'o'
                sand_count += 1
                falling = False
            if sand == (500,0):
                sand_stuck = True
                break
    return sand_count
    return None

if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    grid = parse_rock(lines)
    print(f"Part 1: {part1(grid)}")
    grid = parse_rock(lines)
    print(f"Part 2: {part2(grid)}")
