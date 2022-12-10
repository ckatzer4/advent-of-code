import sys

test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

def part1(lines):
    ins = [l.split() for l in lines]
    (cycle, x) = (0, 1)
    strength = 0
    checks = set(range(20,221,40))
    for i in ins:
        if i[0] == 'noop':
            cycle += 1
            if cycle in checks:
                strength += cycle*x
        elif i[0] == 'addx':
            cycle += 1
            if cycle in checks:
                strength += cycle*x
            cycle += 1
            if cycle in checks:
                strength += cycle*x
            x += int(i[1])
    return strength

def part2(lines):
    screen = [
        ['.' for c in range(40)]
        for r in range(6)
    ]
    ins = [l.split() for l in lines]
    (cycle, x) = (0, 1)
    for i in ins:
        if i[0] == 'noop':
            if abs(cycle%40-x) <=1:
                screen[cycle//40][(cycle%40)] ='#'
            cycle += 1
        elif i[0] == 'addx':
            if abs(cycle%40-x) <=1:
                screen[cycle//40][(cycle%40)] ='#'
            cycle += 1
            if abs(cycle%40-x) <=1:
                screen[cycle//40][(cycle%40)] ='#'
            cycle += 1
            x += int(i[1])
    for l in screen:
        print(''.join(l))
    return None


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
