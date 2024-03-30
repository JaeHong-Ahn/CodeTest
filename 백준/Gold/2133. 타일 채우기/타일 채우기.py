N = int(input())

dp = [0] * 31

dp[2] = 3
dp[4] = 11

for i in range(5, N+1):
    if i % 2 == 0:
        dp[i] = (dp[i-2] * dp[2])
        plus = 2
        for j in range((i//2)-1):
            plus += dp[2*j]*2
        dp[i] += plus
    else:
        pass

print(dp[N])