
for i in range(485617, 529679):
    val = i
    div = 2
    count = 0
    divs = []
    good = True
    while div**2 <= val:
        if val%div == 0:
            count += 1
            val //= div
            divs += [div]
            if val % div == 0:
                good = False
                break
        div += 1
        if count >= 3:
            good = False
            break
    if val in divs:
        good = False
    divs += [val]
    count += 1
    d = max(divs) - min(divs)
    if (not good) or count != 3 or len(set([v%10 for v in divs])) != 1 or d >= 100:
        continue
    print(i, d, val, '-', divs)

