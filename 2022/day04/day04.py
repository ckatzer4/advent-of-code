import sys

test = """
"""

def part1(lines):
    count = 0
    for (s1, s2) in lines:
        s1s, s1e = s1.split('-')
        s2s, s2e = s2.split('-')
        s1 = set(range(int(s1s),int(s1e)+1))
        s2 = set(range(int(s2s),int(s2e)+1))
        if s1.issubset(s2) or s2.issubset(s1):
            count += 1
    return count

def part2(lines):
    count = 0
    for (s1, s2) in lines:
        s1s, s1e = s1.split('-')
        s2s, s2e = s2.split('-')
        s1 = set(range(int(s1s),int(s1e)+1))
        s2 = set(range(int(s2s),int(s2e)+1))
        if not s1.isdisjoint(s2):
            count += 1
    return count


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.split('\n')[:-1]
    pairs = [l.split(',') for l in lines]
    print(f"Part 1: {part1(pairs)}")
    print(f"Part 2: {part2(pairs)}")
