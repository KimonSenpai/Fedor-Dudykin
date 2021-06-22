f = open("D:\\Downloads\\27b (1).txt", 'r')
N = int(f.readline())

a, b = map(int, f.readline().split())

dp = [[0 for i in range(7)] for i in range(N + 1)]
dp[1][a%7] = max(dp[1][a%7], a)
dp[1][b%7] = max(dp[1][b%7], b)

minSum = min(a, b)
for k in range(2, N + 1):
    a, b = map(int, f.readline().split())
    minSum += min(a, b)
    for i in range(7):
        if dp[k-1][i] == 0: continue
        dp[k][(i+a)%7] = max(dp[k][(i+a)%7], dp[k-1][i] + a)
        dp[k][(i+b)%7] = max(dp[k][(i+b)%7], dp[k-1][i] + b)

print(dp[N][minSum%7])