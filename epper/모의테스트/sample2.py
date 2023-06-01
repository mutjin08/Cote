#힌트 : 정수를 입력받아서 조건에 따라 출력문을 작성합니다.
#입력안내용 메시지는 작성하지 않습니다.

n=int(input())
if n%2==1 and 1000<=n<2000:
    print("I Love It!")
elif n%2==1 and n<1000:
    print("I Like It!")
else:
    print("!")