#형 변환(기본형 -
a = "123"
b = 123
c = True
d = 12.3
e = "12.3"
f = 0

#타입
print("a타입 : ",type(a))
print("b타입 : ",type(b))
print("c타입 : ",type(c))
print("d타입 : ",type(d))
print("e타입 : ",type(e))
print("f타입 : ",type(f),"\n")

#정수화
print("a 정수화",int(a))
print("b 정수화",int(b))
print("c 정수화",int(c))
print("d 정수화",int(d))
#print("e 정수화",int(e)) 스트링""를 정수화해도 안에가 실수라 불가
print("f 정수화",int(f),"\n")

#실수화
print("a 실수화",float(a))
print("b 실수화",float(b))
print("c 실수화",float(c))
print("d 실수화",float(d))
print("e 실수화",float(e))
print("f 실수화",float(f),"\n")

#문자화(string) - str
print("a 문자화",str(a))
print("b 문자화",str(b))
print("c 문자화",str(c))
print("d 문자화",str(d))
print("e 문자화",str(e))
print("f 문자화",str(f),"\n")


#논리화(boolean) - bool : 1이상은 다 true가 됨
print("a 논리화",bool(a))
print("b 논리화",bool(b))
print("c 논리화",bool(c))
print("d 논리화",bool(d))
print("e 논리화",bool(e))
print("f 논리화",bool(f))