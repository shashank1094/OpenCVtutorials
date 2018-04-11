d = {1: 44, 2: 22, 3: 33}
for w in sorted(d, key=d.get, reverse=True):
    print(w, d[w])
