import sys

test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

priority ='abcdefghijklmnopqrstuvwxyz'\
          'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part1(sacks):
    pri_sum = 0
    for sack in sacks:
        l = int(len(sack)/2)
        (c1, c2) = (sack[0:l], sack[l:])
        (c1, c2) = (set(c1), set(c2))
        common = c1.intersection(c2).pop()
        pri = priority.index(common)+1
        pri_sum += pri
    return pri_sum

def part2(sacks, s=0):
    # too much erlang, decided on recursion
    if len(sacks) == 0:
        return s
    elves = [sacks.pop(0),sacks.pop(0),sacks.pop(0)]
    elves = [set(s) for s in elves]
    common = elves[0] & elves[1] & elves[2]
    common = common.pop()
    pri = priority.index(common)+1
    return part2(sacks, s+pri)

def part2b(sacks):
    # non-recursive solution
    pri_sum = 0
    for r in range(0,len(sacks),3):
        elves = sacks[r:r+3]
        elves = [set(s) for s in elves]
        common = elves[0] & elves[1] & elves[2]
        common = common.pop()
        pri = priority.index(common)+1
        pri_sum += pri
    return pri_sum


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    sacks = text.split('\n')[:-1]
    print(f"Part 1: {part1(sacks)}")

    print(f"Part 2: {part2b(sacks)}")
    # orig recursive solution works, but it destroys the list in the process
    print(f"Part 2: {part2(sacks)}")
