totalE = []
cur = 0
with open("input.txt", "r+") as input:
    for line in input:
        if line == "\n":
            totalE.append(cur)
            cur = 0
        else:
            cur += int(line)
        totalE.sort()
    print("for part1 ans: ", totalE[-1:][0])

    print("for part2 ans: ", sum(totalE[-3:]))


