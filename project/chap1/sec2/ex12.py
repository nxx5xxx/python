#파이썬에만 있는연산자임
#파이썬은 맡교환이 가능 ex) x, y = y, x
#기타 연산자 : 교환연산자 , 멤버연산자(in, not in), 식별연산자(is ,not is) -- 주소비교
#같은기억장소 공유 = 얕은복사(static)

a = 5
b = 3
c = 3
print("교환 전")
print("a : ",a,"b :",b)
a, b= b, a
print("교환 후")
print("a : ",a,"b :",b,"\n")

lst=[4,5,6,7,8]
print("lst안에 6이 존재하는가?",6 in lst)
print("lst 안에 8이 존재하지않는가?", 8 not in lst , "\n")

print("a의 주소 :",id(a))
print("b의 주소 :",id(b))
print("c의 주소 :",id(c))
print("a =",a,"b =",b,"c =",c)
print("a==b",a==b,"a==c",a==c)
print("a is b",a is b,"a is c",a is c) #주소를 비교
# #파이썬은 값이같으면 주소가 같아서 이것도 True가 나온다
print("a!=b",a!=b,"a!=c",a!=c)
print("a is not b",a is not b,"a is not c",a is not c)
d = "강아지"
e = "강아지"
print(id(e))
print(id(d)) #문자열도 값이 같아서 주소가 같게나옴