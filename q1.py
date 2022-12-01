totalE = []
prevmax1 = 0
prevmax2 = 0
cur = 0
with open("input.txt", "r+") as input:
    for line in input:
        if line == "\n":
            totalE.append(cur)
            cur = 0
        else:
            cur += int(line)
        totalE.sort()
    print(sum(totalE[-3:]))


