C,N = map(int,input().split())
dp=[0]+[float('inf') for _ in range(C)]
for _ in range(N):
    cost, customerCount = map(int, input().split())
    for i in range(C+1):
        oldCost = 0 if i < customerCount else dp[i-customerCount]
        dp[i] = min(oldCost+cost, dp[i])
print(dp[C])