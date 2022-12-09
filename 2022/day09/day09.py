import sys

test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

test2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

def are_touching(h,t):
    (hr, hc) = h
    (tr, tc) = t
    if abs(hr-tr)<2 and abs(hc-tc)<2:
        return True
    return False

def tail_move(h,t):
    (hr, hc) = h
    (tr, tc) = t
    if hr<tr:
        if abs(hr-tr) > abs(hc-tc):
            return (tr-1,hc)
        elif hc<tc:
            return (tr-1,tc-1)
        else:
            return (tr-1,tc+1)
    elif hr>tr:
        if abs(hr-tr) > abs(hc-tc):
            return (tr+1,hc)
        elif hc<tc:
            return (tr+1,tc-1)
        else:
            return (tr+1,tc+1)
    elif hc<tc:
        return (hr,tc-1)
    else:
        return (hr,tc+1)

DIRS = {
    'U': (1,0),
    'D': (-1,0),
    'R': (0,1),
    'L': (0,-1),
}

def part1(moves):
    # orig solution
    (h,t) = ((0,0),(0,0))
    tail_pos = set([t])
    for (d, i) in moves:
        for _ in range(i):
            if d == 'U':
                h = (h[0]+1,h[1])
                if not are_touching(h,t):
                    t = tail_move(h,t)
            elif d == 'R':
                h = (h[0],h[1]+1)
                if not are_touching(h,t):
                    t = tail_move(h,t)
            elif d == 'D':
                h = (h[0]-1,h[1])
                if not are_touching(h,t):
                    t = tail_move(h,t)
            elif d == 'L':
                h = (h[0],h[1]-1)
                if not are_touching(h,t):
                    t = tail_move(h,t)
            tail_pos.update([t])
    return len(tail_pos)

def part2(moves, rope_len):
    # cleaned up for less branching and arbitrary rope length
    rope = [(0,0) for i in range(rope_len)]
    tail_pos = set([rope[-1]])
    for (d, i) in moves:
        (dr, dc) = DIRS[d]
        for _ in range(i):
            h = rope[0]
            rope[0] = (h[0]+dr,h[1]+dc)
            for j in range(1,rope_len):
                (h,t) = (rope[j-1], rope[j])
                if not are_touching(h,t):
                    rope[j] = tail_move(h,t)
            tail_pos.update([rope[-1]])
    return len(tail_pos)


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test2
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    moves = [l.split() for l in lines]
    moves = [(a, int(b)) for (a,b) in moves]
    print(f"Part 1: {part2(moves,2)}")
    print(f"Part 2: {part2(moves,10)}")
