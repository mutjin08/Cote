# https://www.acmicpc.net/problem/11053
def solution(n,nums):
    dp=[1]*(n+1)

    for i in range(1,n+1):
        for j in range(1,i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[j]+1,dp[i])
    return max(dp)

n=int(input())
nums=[0]+list(map(int,input().split()))
print(solution(n,nums))