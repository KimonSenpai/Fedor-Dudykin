f = open("D:\\Downloads\\18.txt", 'r')

matr = []
for line in f:
    print(line)
    matr += list(map(int, line[3:].split(';')))

N = len(matr[0])

Max = [[0]*N for _ in range(N)]
for i in range(1, N):
    if Max[0][i-1] != 0 and abs(matr[0][i-1] - matr[0][i]) <= 50:
        Max[0][i] = Max[0][i-1] + abs(matr[0][i-1] - matr[0][i])
    if Max[i-1][0] != 0 and abs(matr[i-1][0] - matr[i][0]) <= 50:
        Max[i][0] = Max[i-1][0] + abs(matr[i-1][0] - matr[i][0])

for i in range(1, N):
    for j in range(1, N):
        v = abs(matr[i-1][j] - matr[i][j])
        h = abs(matr[i][j-1] - matr[i][j])
        if Max[i-1][j] != 0 and v <= 50:
            Max[i][j] = max(Max[i][j], Max[i-1][j] + v)
        if Max[i][j-1] != 0 and h <= 50:
            Max[i][j] = max(Max[i][j], Max[i][j-1] + h)

res = max(max(l) for l in Max)
print(res)