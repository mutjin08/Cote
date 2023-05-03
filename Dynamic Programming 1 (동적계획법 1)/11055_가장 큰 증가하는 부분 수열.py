# https://www.acmicpc.net/problem/11055

def solution(n,nums):
    dp=nums[:]
    for i in range(n):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],dp[j]+nums[i])
    return max(dp)

n=int(input())
nums=list(map(int,input().split()))
print(solution(n,nums))