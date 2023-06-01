alst=[1,2,2,3,4,5,5,5,5,6,7,7,8]
adic={}
for a in alst:
    if a in adic:
        adic[a]+=1
    else:
        adic[a]=1

print(adic)
for a in adic.values():
    print(a,end=" ")