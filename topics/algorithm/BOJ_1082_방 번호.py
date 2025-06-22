N=int(input())
P=[*map(int, input().split())]
M=int(input())
min_cost = min(P)
if N==1: print('0')
else: 
    min_first_cost = min(P[1:])
    if min_first_cost > M: print('0')
    else :
        max_len = (M-min_first_cost) // min_cost
        min_first_digit = P.index(min_first_cost)
        min_digit = P.index(min_cost)

        result = [str(min_first_digit)] + [str(min_digit)]*max_len
        M-=min_first_cost+min_cost*max_len
        for i in range(max_len+1):
            for digit in range(N-1,-1,-1):
                cost=P[digit]-(min_cost if i>0 else min_first_cost)
                if M>=cost:
                    M-=cost
                    result[i]=str(digit)
                    break
        print(''.join(result))