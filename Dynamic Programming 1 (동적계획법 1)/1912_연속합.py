# https://www.acmicpc.net/problem/1912

def solution(n,nums):
    dp=[0]*(n)
    dp[0]=nums[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+nums[i],nums[i])
    return max(dp)


n=int(input())
nums=list(map(int,input().split()))
print(solution(n,nums))