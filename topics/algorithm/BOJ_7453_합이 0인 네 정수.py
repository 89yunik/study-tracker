from collections import Counter
n=int(input())
A,B,C,D=[[],[],[],[]]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a);B.append(b);C.append(c);D.append(d)
ab_sum = Counter()
for a in A:
    for b in B:
        ab_sum[a+b] +=1
count = 0
for c in C:
    for d in D:
        count += ab_sum.get(-(c+d),0)
print(count)