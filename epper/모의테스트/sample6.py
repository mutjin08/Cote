from string import ascii_uppercase
alst=list(ascii_uppercase)
alen=len(alst)

n=int(input())
pointer=0
for i in range(1,n+1):
    print("."*(n+1-i),end="")
    for j in range(i):
        print(alst[pointer],end=" ")
        pointer+=1
        pointer%=alen
    print()