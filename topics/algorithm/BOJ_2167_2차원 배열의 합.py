N,M=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(N)]
K=int(input())
for _ in range(K):
    i,j,x,y=map(int,input().split())
    s=0
    for a in range(i-1,x):
        for b in range(j-1,y):
            s+=arr[a][b]
    print(s)