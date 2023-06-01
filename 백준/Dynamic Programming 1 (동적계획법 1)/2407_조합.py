# https://www.acmicpc.net/problem/2407

def solution(n,m):
    dp=[[1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][1]=i

    for i in range(2,n+1):
        for j in range(2,i+1):
            dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
    
    return dp[n][m]

n,m=map(int,input().split())
print(solution(n,m))