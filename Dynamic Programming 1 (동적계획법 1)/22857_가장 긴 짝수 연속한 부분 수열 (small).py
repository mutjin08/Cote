# https://www.acmicpc.net/problem/22857

def solution(n,k,nums):
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        nums[i]%=2
        for j in range(k+1):
            if nums[i]==0:
                dp[i][j]=dp[i-1][j]+1
            elif nums[i]!=0 and j!=0:
                dp[i][j]=dp[i-1][j-1]
                
    return max(map(max,dp))

n,k=map(int,input().split())
nums=[0]+list(map(int,input().split()))
print(solution(n,k,nums))