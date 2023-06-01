# https://www.acmicpc.net/problem/2839

def solution(n):
    dp=[-1]*(n+1)
    dp[3],dp[5]=1,1

    for i in range(6,n+1):
        if i%5==0:
            dp[i]=dp[i-5]+1
        elif i%5!=0 and i%3==0:
            dp[i]=dp[i-3]+1
        elif dp[i-3]>0 and dp[i-5]>0:
            dp[i]=min(dp[i-3],dp[i-5])+1
    
    return dp[n]        

n=int(input())
print(solution(n))