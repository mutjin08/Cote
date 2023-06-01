n,m=map(int,input().split())
knows=set(map(int,input().split()[1:]))

parties=[]
for _ in range(m):
    participants=set(map(int,input().split()[1:]))
    parties.append(participants)
    if knows&participants:
        knows=knows|participants

answer=0
for party in parties:
    if knows&party:
        continue
    else:
        answer+=1

print(answer)