# https://www.acmicpc.net/problem/1244

def solution(n_switches,switches,n_students,students):
    for student in students:
        sex,num=student

        if sex==1:
            for i in range(1,n_switches+1):
                if i>=num and i%num==0:
                    switches[i]=0 if switches[i]%2==1 else 1
        elif sex==2:
            switches[num]=0 if switches[num]%2==1 else 1
            left,right=num-1,num+1
            while 1<=left and right<=n_switches:
                if switches[left]!=switches[right]:
                    break
                switches[left]=0 if switches[left]%2==1 else 1
                switches[right]=0 if switches[right]%2==1 else 1
                left-=1
                right+=1
    return [switches[i:i+20] for i in range(1,n_switches+1,20)]

n_switches=int(input())
switches=[-1]+list(map(int,input().split()))
n_students=int(input())
students=[]
for _ in range(n_students):
    students.append(list(map(int,input().split())))

for res in solution(n_switches,switches,n_students,students):
    print(*res)
