import sys
from functools import cmp_to_key

test = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def is_ordered(left,right):
    if type(left) == list and type(right) == list:
        if len(left)>0 and len(right)>0:
            first_ordered = is_ordered(left[0], right[0])
            if first_ordered is None:
                return is_ordered(left[1:], right[1:])
            else:
                return first_ordered
        elif len(left) == 0 and len(right)>0:
            return True
        elif len(left)>0 and len(right) == 0:
            return False
        elif len(left) == 0 and len(right) == 0:
            return None
    elif type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left == right:
            return None
        else:
            return False
    elif type(left) == list and type(right) == int:
        return is_ordered(left, [right])
    elif type(left) == int and type(right) == list:
        return is_ordered([left], right)
    else:
        print(f'Was I supposed to handle this case? {left} {right}')


def part1(pairs):
    return sum(i for (i,p) in enumerate(pairs, start=1) if is_ordered(p[0], p[1]))

def part2(packets):
    @cmp_to_key
    def packet_key(x,y):
        ordered = is_ordered(x,y)
        if ordered: return 1
        elif ordered is None:
            return 0
        else:
            return -1
    packets.sort(key=packet_key, reverse=True)
    return (packets.index([[2]])+1) * (packets.index([[6]])+1)

if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    pairs = text.split('\n\n')
    pairs = [pair.splitlines() for pair in pairs]
    # I'm sorry
    pairs = [(eval(p[0]), eval(p[1])) for p in pairs]
    print(f"Part 1: {part1(pairs)}")
    packets = [[[2]], [[6]]]
    for (p1, p2) in pairs:
        packets.append(p1)
        packets.append(p2)
    print(f"Part 2: {part2(packets)}")
