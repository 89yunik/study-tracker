N=int(input())
students=map(int,input().split())
stack,cnt=[],1
for student in students:
    stack.append(student)
    while stack and stack[-1] == cnt: 
        cnt+=1
        stack.pop()
print('Nice' if cnt == N+1 else 'Sad')