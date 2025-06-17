from collections import deque

T=int(input())
for _ in range(T):
    n=int(input())
    picks = map(int, input().split())
    graph = [[]  for _ in range(n+1)]
    in_degree = [0]*(n+1)
    for student, pick in enumerate(picks):
        graph[student+1].append(pick)
        in_degree[pick]+=1
    queue = deque([i for i in range(1,n+1) if in_degree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 : queue.append(neighbor)
    
    print(count)