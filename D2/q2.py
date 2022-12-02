score = 0
score2 = 0
with open("input.txt", "r+") as input:
    for line in input:
        s = line.replace('\n','').split(' ')
        if s[0] == 'A':
            if s[1] == 'X':
                score += 1 + 3
                score2 += 3 + 0 
            elif s[1] == 'Y':
                score += 2 + 6
                score2 += 1 + 3
            elif s[1] == 'Z':
                score += 3 + 0
                score2 += 2 + 6
        elif s[0] == 'B':
            if s[1] == 'X':
                score += 1 + 0
                score2 += 1 + 0 
            elif s[1] == 'Y':
                score += 2 + 3
                score2 += 2 + 3 
            elif s[1] == 'Z':
                score += 3 + 6
                score2 += 3 + 6
        elif s[0] == 'C':
            if s[1] == 'X':
                score += 1 + 6
                score2 += 2 + 0 
            elif s[1] == 'Y':
                score += 2 + 0
                score2 += 3 + 3
            elif s[1] == 'Z':
                score += 3 + 3
                score2 += 1 + 6

print(score, score2)
