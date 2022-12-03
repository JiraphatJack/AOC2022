lines = open("input.txt").read().strip().split("\n")

def getVal(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

sum1 = 0
for line in lines:
    first, second = line[:len(line)//2], line[len(line)//2:]
    match, = set(first) & set(second)
    sum1 += getVal(match)

print(sum1)

sum2 = 0
for i in range(0, len(lines), 3):
    line1, line2, line3 = lines[i:i+3]
    match, = set(line1) & set(line2) & set(line3)
    sum2 += getVal(match)

print(sum2)

