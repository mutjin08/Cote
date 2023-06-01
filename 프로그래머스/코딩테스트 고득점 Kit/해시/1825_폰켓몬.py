# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    get=len(nums)//2
    nums=set(nums)
    species=len(nums)
    
    if species>=get:
        return get
    else:
        return species