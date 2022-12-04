if __name__ == "__main__":
    with open('input') as f:
        text = f.read()

    elves = text.split('\n\n')
    sums = [sum(int(i) for i in e.split('\n') if i) for e in elves]
    print(f"Part 1: {max(sums)}")

    top = sorted(sums)[-3:]
    print(f"Part 2: {sum(top)}")
