# https://www.acmicpc.net/problem/20546

def solution(cash,stocks):
    jh_cash,sm_cash=cash,cash
    jh_cnt,sm_cnt=0,0
    for i in range(len(stocks)):
        if jh_cash>=stocks[i]:
            #전량매수
            jh_cnt+=jh_cash//stocks[i] 
            jh_cash=jh_cash%stocks[i]

        if i<3:
            continue
        
        if stocks[i-3]<stocks[i-2]<stocks[i-1]<stocks[i]:
            #전량매도
            sm_cash+=sm_cnt*stocks[i]
            sm_cnt=0

        elif stocks[i-3]>stocks[i-2]>stocks[i-1]>stocks[i]:
            #전량매수
            sm_cnt+=sm_cash//stocks[i]
            sm_cash=sm_cash%stocks[i]
    
    sm=sm_cash+stocks[-1]*sm_cnt
    jh=jh_cash+stocks[-1]*jh_cnt

    if sm>jh:
        return "TIMING"
    elif sm<jh:
        return "BNP"
    else:
        return "SAMESAME"

cash=int(input())
stocks=list(map(int,input().split()))
print(solution(cash,stocks))