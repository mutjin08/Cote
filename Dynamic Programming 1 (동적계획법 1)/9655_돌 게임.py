# https://www.acmicpc.net/problem/9655

def solution(n):
    if n%2==0:
        return "CY"
    else:
        return "SK"

n=int(input())
print(solution(n))