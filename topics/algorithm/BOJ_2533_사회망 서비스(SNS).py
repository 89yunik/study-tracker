import sys
sys.setrecursionlimit(10**9)

N=int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, sys.stdin.readline().split(" "))
    tree[u].append(v)
    tree[v].append(u)

dp = [[0,0] for _ in range(N+1)]
visited = [False] * (N+1)
def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = 1
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0]+=dp[v][1]
            dp[u][1]+=min(dp[v][0],dp[v][1])
dfs(1)
print(min(dp[1][0], dp[1][1]))