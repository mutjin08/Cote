n=int(input())
words=[]
answer=n

for _ in range(n):
    words.append(input())

for word in words:
    letters=[]
    for i in range(1,len(word)):
        if word[i]!=word[i-1] and word[i] in letters:
            answer-=1
            break

print(answer)