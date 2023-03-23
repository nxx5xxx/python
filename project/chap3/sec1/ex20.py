#함수나 매소드 : 사용자 정의 함수와 내장함수
#함수나 매소드의 타입 : 매개변수와 리턴값의 유무에 따라
#자바는 function을 붙이고 타입이 필요없지만 (c하고유사 : c는 접근제한자가 안붙음)
#파이썬은 def로 시작 (user define function의 줄임말)
#ex) def x():엔터탭    값

#오버라이딩 가능
#def x(매개변수): 리턴(return)
def fnc1():
    print("매개변수도없고 리턴값도 없는 함수")
#fnc1호출
fnc1()

def fnc2(x):
    print("매개변수는 있고 리턴값이 없는함수 x : ",x)
#fnc2 호출
fnc2(5)

def fnc3():
    return "매개변수는 없고 리턴값이 있는 함수"
re_fnc3 = fnc3()
#re_fnc3 = "매개변수는 없고 리턴값이 있는함수" 랑 같은뜻

print(re_fnc3)
#print("매개변수는 없고 리턴값이 있는함수") 랑 같은뜻

def fnc4(y, z): #매개변수도 있고 리턴값도 있는함수
    return y+z
re_fnc4 = fnc4(5,2)
print(re_fnc4)

'''
즉, def fnc(값): 에서 fnc(5)등 값을 넣을경우 함수는 그 값을 자기 아래쪽에 대입해 그 값을 출력해준다
예를들어 def fnc(x):
     print(x+5) 라 하면  x에 5를 대입해 print문까지 불러와주는것
#여기서 fnc는 함수명임

'''
def fnc10(x):
    print(x+5)
fnc10(5)

'''
def fnc():
    return    -------이것은 위에 설명한것처럼 fnc를 호출할경우 return에 있는것을 그대로 돌려주는것이다
'''