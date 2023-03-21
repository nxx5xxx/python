#진법 변환
a= 31
bin_a= bin(a)
print("2진수로 변환한 a  :",bin_a)
b= 14
print("2진수로 b를출력    :",bin(b))
oct_a = oct(a)
print("8진수로 변환한 a :",oct_a)
print("8진수로 출력한 b :",oct(b))
hex_a = hex(a)
print("16진수로 변환한 a :",hex_a)
print("16진수로 출력한 b :",hex(b))

#비트(2진수) 연산자 : &, |, ^, ~
print("2진수로 변환한 a  :",bin_a)
print("2진수로 b를출력    :",bin(b))
print("a & b :", bin(a&b))#and
print("a | b :",bin(a|b)) #or
print("a ^ b :",bin(a^b)) #xor
print("~a (a의 보수) :",bin(~a)) #complement(not) 연산
print("~b (b의 보수) :",bin(~b))



