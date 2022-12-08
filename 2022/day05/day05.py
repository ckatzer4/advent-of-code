import sys
from collections import defaultdict

test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def parse(text):
    platforms = defaultdict(list)
    moves = []
    platformtext, movetext = text.split('\n\n')
    strlen = max(len(l) for l in platformtext.splitlines())
    for l in platformtext.splitlines():
        if '[' in l:
            for (platform, i) in enumerate(range(1,strlen,4)):
                try:
                    crate = l[i]
                    if crate != ' ':
                        platforms[platform+1].append(crate)
                except:
                    pass
    platforms = {p: list(reversed(l)) for p,l in platforms.items()}
    for l in movetext.splitlines():
        (_,count,_,pfrom,_,pto) = l.split()
        moves.append((int(count),int(pfrom),int(pto)))
    return platforms,moves

def part1(platforms, moves):
    for (count, pfrom, pto) in moves:
        for _ in range(count):
            c = platforms[pfrom].pop()
            platforms[pto].append(c)
    result = ''
    for i in sorted(platforms.keys()):
        crates = platforms[i]
        result += crates[-1]
    return result

def part2(platforms, moves):
    for (count, pfrom, pto) in moves:
        crates = platforms[pfrom][-count:]
        platforms[pfrom] = platforms[pfrom][:-count]
        platforms[pto].extend(crates)
    # how about a generator?
    result = ''.join(platforms[i][-1] for i in sorted(platforms.keys()))
    return result


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    platforms, moves = parse(text)
    print(f"Part 1: {part1(platforms, moves)}")
    platforms, moves = parse(text) # need to start fresh!
    print(f"Part 2: {part2(platforms, moves)}")
