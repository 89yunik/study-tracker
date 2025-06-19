N=int(input())
MOD=10**9
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)]
for digit in range(1,10): dp[1][digit][1 << digit] = 1
for length in range(1, N):
    for digit in range(10):
        for bit in range(1<<10):
            if dp[length][digit][bit]==0:continue
            for next_digit in [digit-1, digit+1]:
                if 0<=next_digit<=9:
                    next_bit=bit|(1<<next_digit)
                    dp[length+1][next_digit][next_bit] += dp[length][digit][bit]
                    dp[length+1][next_digit][next_bit] %= MOD
print(sum(dp[N][digit][1023] for digit in range(10)) % MOD)