import sys
from functools import reduce
from operator import mul

test = """30373
25512
65332
33549
35390
"""

def trees(lines):
    treemap = {}
    for (r,l) in enumerate(lines):
        for (c,i) in enumerate(l):
            treemap[(r,c)] = int(i)
    return treemap

DIRS = [(0,1), (1,0), (-1,0), (0,-1)]

def lines_of_sight(rc, treemap):
    (r,c) = rc
    all_lines = []
    for (dr,dc) in DIRS:
        line_of_sight = []
        for i in range(1,100):
            rc = (r+dr*i, c+dc*i)
            if rc not in treemap:
                break
            line_of_sight.append(treemap[rc])
        all_lines.append(line_of_sight)
    return all_lines

def part1(treemap):
    vissum = 0
    for ((r,c),height) in treemap.items():
        visible = False
        for los in lines_of_sight((r,c), treemap):
            if len(los) == 0 or all(h<height for h in los):
                visible = True
        if visible:
            vissum += 1
    return vissum

def product(l):
    return reduce(mul,l,1)

def part2(lines):
    scores = {}
    for ((r,c),height) in treemap.items():
        lines = []
        for los in lines_of_sight((r,c), treemap):
            if any(h>=height for h in los):
                block = next(h for h in los if h>=height)
                lines.append(los.index(block)+1)
            else:
                lines.append(len(los))
        scores[(r,c)] = product(lines)
    return max(score for score in scores.values())

if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    treemap = trees(lines)
    print(f"Part 1: {part1(treemap)}")
    print(f"Part 2: {part2(lines)}")
