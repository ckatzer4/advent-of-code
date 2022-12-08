import sys

test = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""

def windows(l,winlen):
    # a sliding window function for lists should be built-in
    for i in range(len(l)-winlen+1):
        yield l[i:i+winlen]

def part1(line):
    # original implementation with a buffer
    buff = line[:4]
    if len(set(buff)) == 4:
        return 4
    for (i,c) in enumerate(line):
        if i < 4:
            continue
        buff = buff[1:] + c
        if len(set(buff)) == 4:
            return i+1
    return None

def part2(line):
    # re-implemented with windows function
    for (i,buff) in enumerate(windows(line,14)):
        if len(set(buff)) == 14:
            return i+14
    return None


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    line = text[:-1]
    print(f"Part 1: {part1(line)}")
    print(f"Part 2: {part2(line)}")
