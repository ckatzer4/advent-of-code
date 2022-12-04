p1,p2 = None,None
if __name__ == "__main__":
    with open('input') as f:
        rounds = f.read().splitlines()

    CASES = {
        ('A', 'X'): 1+3,
        ('A', 'Y'): 2+6,
        ('A', 'Z'): 3+0,
        ('B', 'X'): 1+0,
        ('B', 'Y'): 2+3,
        ('B', 'Z'): 3+6,
        ('C', 'X'): 1+6,
        ('C', 'Y'): 2+0,
        ('C', 'Z'): 3+3,
    }

    p1 = sum(CASES[tuple(r.split())] for r in rounds)
    print(f"Part 1: {p1}")

    CASES2 = {
        ('A', 'X'): 3+0,
        ('A', 'Y'): 1+3,
        ('A', 'Z'): 2+6,
        ('B', 'X'): 1+0,
        ('B', 'Y'): 2+3,
        ('B', 'Z'): 3+6,
        ('C', 'X'): 2+0,
        ('C', 'Y'): 3+3,
        ('C', 'Z'): 1+6,
    }

    p2 = sum(CASES2[tuple(r.split())] for r in rounds)
    print(f"Part 2: {p2}")
