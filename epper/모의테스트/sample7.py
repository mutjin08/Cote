def solution(s):
    answer = 0
    cnt = 0
    for i in range(len(s)):
        if s[i]=="O":
            cnt+=1
        else:
            cnt=0
        answer+=cnt
    return answer