str = '0123 56789 12345'
#문자열 슬라이싱
#리스트와 같이 슬라이싱이 가능하다
print(str[3]) #문자열에 4번째 (0부터시작하므로) 출력 (슬라이싱)
#인데스가 3인(=문자열배열에서 4번째) 문자만 슬라이싱(잘라내기)
print(str[2:8]) #2번째부터 8번째전까지만 슬라이싱
print(str[3:]) #3번째부터 끝까지
print(str[:8]) #처음부터 8번째 전까지

print(str[-4])#뒤에서부터 4번째에 있는것을 슬라이싱
print(str[:-4])#처음부터 뒤에4번째 전까지
print(str[-4:])#뒤에서부터4번째부터 끝까지

print(str[8:-1]) #8번째부터 뒤에서 -1번째 전까지

print(str[-4:-9]) #뒤에서부터 4번째부터 뒤에서부터 9번째 전까지 (출력안됨)
print(str[8:-12]) #둘이 겹치는 범위가 넘어가면 출력이 안됨을 알수있다

#[시작:여기전까지:스탭] 스탭은 [시작:여기전:x+=n] 이라고 볼수있다
print(str[::2]) #2칸씩 출력한것을 알수있다
print('\n\n')


#문자열 을 리스트로 분리 = 스플릿 split
#ex) lst1 = str.split(' ') ' '기준으로 문자열을 나눠 리스트로 만들어라
print(str)
lst1 = str.split(' ')
print(lst1) #' '기준으로 나뉜어 새로생성된 lst1리스트
#ex2
str2 = "강아지--고양이--고라니--님부스2000"
print(str2)
lst2 = str2.split("--") #''랑 "의 구분이 없다
print(lst2)

#리스트를 문자열로 합치기 = 조인 join
#ex) str_j= '-'.join(lst1)  lst1의 데이터를받아 구분기호 사이에 - 를 넣어 문자열 str_j를 만들어줘라
str_j = '-'.join(lst1)
print(str_j)
#ex2
str2_j = '__'.join(lst2)
print(str2_j)