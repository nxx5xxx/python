#파이썬 내장함수

#절대값 (+-기호를 빼버림) abs(x)
print("절대값 abc(-99) : ", abs(-99))

#해당 아스키코드 문자 chr(x)
print("해당 아스키코드 문자 chr(65) :", chr(65))

#최대값 max([43,52,90,60,55])
print("최대값: max([43,52,90,60,55]) : " ,max([43,52,90,60,55]))

#최소값 min([43,52,90,60,55])
print("최소값: min([43,52,90,60,55]) : " ,min([43,52,90,60,55]))

#합계 sum([43,52,90,60,55])
print("합계 sum([43,52,90,60,55]) : ", sum([43,52,90,60,55]))

#정렬 sorted([43,52,90,60,55])
print("정렬 sorted([43,52,90,60,55])", sorted([43,52,90,60,55]))

#파이썬과 자바스크립트에만 있는언어 eval
#계산식 문자열 eval("x*y-z") ""안에있는것을 계산해줌
print("문자열 안에를 계산 eval(\"22*2/11\") : ", eval("22*2/11"))


#콘솔에 help(list)를쳐보면 문법의 사용법이 나온다