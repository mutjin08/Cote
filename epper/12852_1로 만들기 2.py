n=int(input())

dp=[0]*(n+1)
nums=[[] for _ in range(n+1)]

dp[1]=0
nums[1]=[1]
for i in range(2,n+1):
    dp[i]=dp[i-1]
    nums[i]=nums[i-1]

    if i%3==0 and dp[i//3]<=dp[i]:
        dp[i]=dp[i//3]
        nums[i]=nums[i//3] 

    if i%2==0 and dp[i//2]<=dp[i]:
        dp[i]=dp[i//2]
        nums[i]=nums[i//2] 
    
    dp[i]+=1
    nums[i]+=[i]

print(dp[n])
print(nums[n])