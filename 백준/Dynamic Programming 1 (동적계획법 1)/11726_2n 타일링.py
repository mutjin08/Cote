# https://www.acmicpc.net/problem/11726

def solution(n):
    if n<3:
        return n
    
    dp=[0]*(n+1)
    dp[1],dp[2]=1,2

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%10007

n=int(input())
print(solution(n))