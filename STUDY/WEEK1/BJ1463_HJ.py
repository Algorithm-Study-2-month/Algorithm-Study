n=int(input())
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[1] = 0
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1,dp[i-1]+1)
    elif i %2 ==0:
        dp[i] = min(dp[i//2]+1,dp[i-1]+1)
    else:
        dp[i]=dp[i-1]+1
print(dp[i])
