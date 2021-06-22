f = open("D:\\Downloads\\26 (1).txt", 'r')
N = int(f.readline())
mas = [int(line) for line in f]
mas.sort()
l = mas[N//2 - 1]
r = mas[N//2 + N//4]
c = 0
m = mas[-1]
for i in range(N):
    for j in range(i+1, N):
        s = mas[i] + mas[j]
        if s % 2 == 0 and l < s//2 < r:
            c += 1
            m = min(m, s//2)
print(c, m)
