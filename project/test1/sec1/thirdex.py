#계산기 이용하여 문제풀기
import test1.sec1.Third as cal
print("사칙연산 할 두가지 수를 입력하세요")
x=int(input())
y=int(input())
print("더하기 : ",cal.plus(x,y))
print("빼기 : ",cal.minus(x,y))
print("나누기 : ",cal.div(x,y))
print("곱하기 : ",cal.multiple(x,y))
