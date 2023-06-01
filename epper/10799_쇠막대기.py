# https://www.acmicpc.net/problem/10799
s=input()
answer=0

cnt=1
for i in range(1,len(s)):
    if s[i]==")":
        if s[i-1]==")":
            cnt-=1
            answer+=1
        else:
            cnt-=1
            answer+=cnt
    else:
        cnt+=1

print(answer)
