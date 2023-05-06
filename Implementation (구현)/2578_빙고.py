# https://www.acmicpc.net/problem/2578

def bingo_nums(graph):
    cnt=0
    cols=[0,0,0,0,0]
    rows=[0,0,0,0,0]
    digs=[0,0]

    for i in range(5):
        
        rows[i]=sum(graph[i])

        for j in range(5):

            if graph[i][j]==1:
                cols[j]+=1

                if i==j:
                    digs[0]+=1
                if i+j==4:
                    digs[1]+=1

    for n in cols+rows+digs:
        if n==5:
            cnt+=1
    return cnt

def solution(calls,writes):
    graph=[[0 for _ in range(5)] for _ in range(5)]

    for i in range(25):
        x,y=writes[calls[i]]
        graph[x][y]=1

        if bingo_nums(graph)>2:
            return i+1

writes=[[] for _ in range(26)]
calls=[]

for i in range(5):
    temp=list(map(int,input().split()))
    for j in range(5):
        writes[temp[j]]=[i,j]
for _ in range(5):
    calls+=list(map(int,input().split()))

print(solution(calls,writes))