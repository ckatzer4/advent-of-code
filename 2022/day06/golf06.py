l = open('input').read()[:-1]
print('\n'.join(f"Part {p+1}: {next(i+w for i in range(len(l)-w+1) if len(set(l[i:i+w])) == w)}" for p,w in enumerate([4,14])))
