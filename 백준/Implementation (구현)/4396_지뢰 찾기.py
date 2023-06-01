# https://www.acmicpc.net/problem/4396

def mine_nums(n,mines,x,y):
    mine_cnt=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and mines[nx][ny]=="*":
            mine_cnt+=1
    return mine_cnt


def solution(n,mines,opens):
    mine_opened=False
    for i in range(n):
        for j in range(n):
            if opens[i][j]=="x":
                opens[i][j]=mine_nums(n,mines,i,j)
                if mines[i][j]=="*":
                    mine_opened=True
    
    if mine_opened==True:
        for i in range(n):
            for j in range(n):
                if mines[i][j]=="*":
                    opens[i][j]="*"
    
    return opens

n=int(input())
mines=[]
for _ in range(n):
    mines.append(list(input().split()))
opens=[]
for _ in range(n):
    opens.append(list(input().split()))

for res in solution(n,mines,opens):
    print(*res)
