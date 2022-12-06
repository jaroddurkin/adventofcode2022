with open("day6/input.txt") as f:
    d = {}
    for l in f:
        i = 0
        while len(d.keys()) < 4:
            if l[i] in d:
                a = d.pop(l[i])
                pops = []
                for key in d:
                    if d[key] < a:
                        pops.append(key)
                for b in pops:
                    d.pop(b)
            d[l[i]] = i
            i += 1
    print(d.keys())
    print(d[list(d)[-1]] + 1)


with open("day6/input.txt") as f:
    d = {}
    for l in f:
        i = 0
        while len(d.keys()) < 14:
            if l[i] in d:
                a = d.pop(l[i])
                pops = []
                for key in d:
                    if d[key] < a:
                        pops.append(key)
                for b in pops:
                    d.pop(b)
            d[l[i]] = i
            i += 1
    print(d.keys())
    print(d[list(d)[-1]] + 1)
