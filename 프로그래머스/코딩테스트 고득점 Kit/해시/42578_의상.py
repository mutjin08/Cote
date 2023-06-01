# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    boxes={}
    for c,t in clothes:
        if t in boxes:
            boxes[t]+=1
        else:
            boxes[t]=1
    answer = 1
    for v in boxes.values():
        answer*=v+1
    answer-=1
    return answer