# 입력
#input("입력해주세요") 문자열로 저장
#int(input("입력하세요")) 숫자로 저장 (자바의 .parseInt로 보면됨)
num1 = int(input("숫자1 입력 : ")) #숫자 입력시 int, float으로 변환
num2 = int(input("숫자2 입력 : "))
print("입력된 값 : ", num1+num2)
print("입력된 num1의 타입 : ", type(num1))
print("입력된 num2의 주소 : ", id(num1))
