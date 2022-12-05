stacks = [[], [], [], [], [], [], [], [], []]

with open("day5/input.txt") as f:
    read_stacks = True
    for l in f:
        if l == "\n":
            read_stacks = False
            continue
        if read_stacks:
            if l[1] == "1":
                continue
            i = 1
            s = 0
            while i < len(l):
                if l[i] != " ":
                    stacks[s].append(l[i])
                s += 1
                i += 4
        else:
            c = l.split(" ")
            for i in range(min(int(c[1]), len(stacks[int(c[3]) - 1]))):
                stacks[int(c[5]) - 1].insert(0, stacks[int(c[3]) - 1].pop(0))


for stack in stacks:
    print(stack)

print("\n part 2")
stacks2 = [[], [], [], [], [], [], [], [], []]

with open("day5/input.txt") as f:
    read_stacks = True
    for l in f:
        if l == "\n":
            read_stacks = False
            continue
        if read_stacks:
            if l[1] == "1":
                continue
            i = 1
            s = 0
            while i < len(l):
                if l[i] != " ":
                    stacks2[s].append(l[i])
                s += 1
                i += 4
        else:
            c = l.split(" ")
            crates = stacks2[int(c[3]) - 1][:(min(int(c[1]), len(stacks2[int(c[3]) - 1])))]
            stacks2[int(c[5]) - 1] = crates + stacks2[int(c[5]) - 1]
            stacks2[int(c[3]) - 1] = stacks2[int(c[3]) - 1][(min(int(c[1]), len(stacks2[int(c[3]) - 1]))):]


for stack in stacks2:
    print(stack)
