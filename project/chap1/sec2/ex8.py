#사칙연산 , 외 7개 연산자
# +, -, *, **, /, //, %
a = 60
b = 10
c = "가나다"
d = "라마바"

print("a+b",a+b)
print("c+d",c+d)
#print("a+c",a+c)#문자열과 숫자는 더하기불가

print("a-b",a-b)
#print("a-c",a-c)#문자열과 숫자 빼기 불가
#print("c-d",c-d)#문자열과 문자을 빼기 불가

print("a*b",a*b)
print("a*c",a*c)#문자열 곱하기 숫자는 곱하기 수 만큼 출력(리피트=반복)
print("c*3",c*3)

# ** 거듭제곱 x의 y승 (60의 14승)
print("a**b",a**b)
#print("c**3",c**3) #문자열 거듭제곱 불가

print("a/b",a/b)
#print("c/d",c/d) #문자열 나누기불가
#print("a/c",a/c)#숫자 문자열로 나누기 불가
#print("c/a",c/a)#문자열 숫자로 나누기 불가

print("a//b",a//b)# // 몫

print("a%b",a%b) #나머지

