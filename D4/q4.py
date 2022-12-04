lines = open("input.txt").read().strip().split("\n")

count1 = 0
count2 = 0
for line in lines:
    elf1, elf2 = line.split(",")
    a1,a2 = map(int,elf1.split("-"))
    b1,b2 = map(int,elf2.split("-"))
    if a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2:
        count1 += 1
    if (a2 >= b1 and a1 <= b2) or (b2 >= a1 and b1 <= a2):
        count2 += 1

print(count1, count2)