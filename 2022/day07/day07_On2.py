import sys
from collections import defaultdict

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def build_tree(lines):
    fs = defaultdict(dict)
    root = fs
    path = []
    for line in lines:
        if '$ cd' in line:
            d = line.split()[2]
            if d == '..':
                # reset fs
                fs = root
                path = path[:-1]
                for p in path:
                    fs = fs[p]
            else:
                path.append(d)
                fs = fs[d]
            continue
        if '$ ls' in line:
            continue
        (size, f) = line.split()
        if size == 'dir':
            fs[f] = dict()
        else:
            fs[f] = int(size)
    return root

def size(fs):
    if type(fs) == int:
        return fs
    return sum(size(fs[sub]) for sub in fs)

def index_sizes(fs, parent='', sizes=dict()):
    for k,v in fs.items():
        if type(v) == dict:
            sizes[parent+k] = size(v)
            sub_sizes = index_sizes(v,parent+k+'/')
            sizes.update(sub_sizes)
    return sizes

def build_size_index(lines):
    path = []
    size_index = defaultdict(int)
    name = lambda p: p[0] + '/'.join(p[1:])
    for line in lines:
        if '$ cd' in line:
            d = line.split()[2]
            if d == '..':
                path.pop()
            else:
                path.append(d)
            continue
        if '$ ls' in line:
            continue
        (size, f) = line.split()
        if size != 'dir':
            for i in range(0,len(path)):
                size_index[name(path[:i+1])] += int(size)
    return size_index


def part1(sizes):
    return sum(s for d,s in sizes.items() if s<=100000)

def part2(sizes):
    unused = 70_000_000 - sizes['/']
    small = [s for s in sizes.values() if unused+s>30_000_000]
    return sorted(small)[0]


if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    lines = text.splitlines()
    sizes = build_size_index(lines)
    print(f"Part 1: {part1(sizes)}")
    # example non-recursive solution for part 2
    print(f"Part 2: {part2(sizes)}")
