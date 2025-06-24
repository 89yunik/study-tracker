I = input().replace('()', 'L')
stack, pieces = [], 0

for curr in I:
    if curr == 'L': pieces += len(stack)
    elif curr == '(': stack.append(curr)
    else:
        stack.pop()
        pieces += 1 

print(pieces)