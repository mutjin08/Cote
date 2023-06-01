from string import ascii_lowercase
alst=list(ascii_lowercase)
alst.sort(reverse=True)
alen=len(alst)

n=int(input())
pointer=0

for i in range(1,n+1):
    print("."*i,end="")
    for j in range(n+1-i):
        print(alst[pointer],end=" ")
        pointer+=1
        pointer%=alen
    print()