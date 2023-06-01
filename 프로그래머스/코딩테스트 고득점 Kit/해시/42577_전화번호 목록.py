def solution(phone_book):
    phone_book.sort()
    n=len(phone_book)
    
    for i in range(1,n):
        x,y=phone_book[i-1],phone_book[i]
        if len(x)<=len(y) and x==y[:len(x)]:
            return False
    return True