#튜플(tuple) : ()로 선언, 읽기전용 (내용변경이 불가)
tp1 = (60, 90, 70, 80, 65, 55, 85, 55)
print("tp1 : ",tp1)
print("tp1의 자료형 타입 : ",type(tp1))
print("tp1의 주소 : ", id(tp1))
print("tp1 [1:4]",tp1[1:4]) #슬라이싱
# tp1[2] = 1 읽기전용이므로 불가
print("tp1 의 길이 : ",len(tp1)) #길이
print("tp1 55의 개수 :",tp1.count(55))
print("tp1 55를 가진 인덱스의 값 :",tp1.index(55)) #앞에서부터 한개만 찾음
#요소의 값을 변경할수 없으므로 정렬, 삽입, 추가, 삭제가 불가
#변경하고싶은경우엔 튜플을 리스트(배열)로 바꿔야함
tp1 = list(tp1) #리스트로변경
tp2 = list(tp1)
print("tp1의 타입 :",type(tp1))
print("tp2의 타입 :",type(tp2))
print("tp2의 값 :",tp2)
tp1 = tuple(tp1) #튜플로변경
print("tp1의 타입 :",type(tp1))
#요소값이 같을경우???