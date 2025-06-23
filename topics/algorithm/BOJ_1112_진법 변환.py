x,b=map(int,input().split())
answer=""
if x == 0: answer = "0"
else:
    result = []
    is_negative = x < 0
    x = abs(x) if b > 0 else x
    while x != 0:
        x, r = divmod(x, b)
        if b < 0 and r < 0:
            x += 1
            r -= b
        result.append(str(r))
    if is_negative and b > 0: result.append('-')
    answer = ''.join(reversed(result))
print(answer)