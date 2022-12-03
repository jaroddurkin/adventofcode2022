with open("day3/input.txt") as f:
    s = 0
    for l in f:
        comp1, comp2 = l[:int(len(l)/2)], l[int(len(l)/2):]
        common = list(set(comp1).intersection(set(comp2)))
        val = ord(common[0]) - 38 if common[0].isupper() else ord(common[0]) - 96
        s += val
    print(s)

with open("day3/input.txt") as f:
    s = 0
    group = []
    for l in f:
        l = l.replace("\n", "")
        group.append(l)
        if len(group) == 3:
            common = list(set.intersection(set(group[0]), set(group[1]), set(group[2])))
            val = ord(common[0]) - 38 if common[0].isupper() else ord(common[0]) - 96
            s += val
            group = []

    print(s)
