# https://www.acmicpc.net/problem/1463

def solution(n):
    if n==1:
        return 0
    elif 1<n<4:
        return 1
    
    dp=[0 for _ in range(n+1)]
    dp[1],dp[2],dp[3]=0,1,1

    for i in range(4,n+1):
        if i%6==0:
            dp[i]=min(dp[i-1],dp[i//3],dp[i//2])+1
        elif i%2!=0 and i%3==0:
            dp[i]=min(dp[i-1],dp[i//3])+1
        elif i%2==0 and i%3!=0:
            dp[i]=min(dp[i-1],dp[i//2])+1
        else:
            dp[i]=dp[i-1]+1
    
    return dp[n]

n=int(input())
print(solution(n))