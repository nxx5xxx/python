#비교연산자와 논리연산자
#비교 연산자  : >, >=, <, <=, ==, !=
#논리 연산자 : and or not (자바와 다르게 && ,|| , ! 이아님)
a= 3
b = 4
c  =5
print('비교연산자')
print("a>b",a>b)
print("c>=b",c>=b)
print("a<b",a<b)
print("b==c",b==c)
print("a!=c",a!=c)

print("\n논리연산자")
print("b>a and c>b", b>a and c>b)
print("a<b or c<b", a<b or c<b)
print("a<b", not a<b) #a<b보다 작지 않다
# print("b>a xor c>b", b>a xor c>b) #그딴거없음