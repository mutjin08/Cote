# https://www.acmicpc.net/problem/9095

def solution(n):
    dp=[0]*max((n+1),4)
    dp[1],dp[2],dp[3]=1,2,4

    for i in range(4,n+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    
    return dp[n]

t=int(input())
for _ in range(t):
    n=int(input())
    print(solution(n))