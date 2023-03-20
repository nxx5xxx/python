# 파이썬의 컬렉션 프레임웤 : 리스트,튜플,셋,딕트(맵)
# 리스트 (배열)
# 여러개의 데이터를 순서를 유지한 상태로 저장
# 순서성이 있음(== 인덱스=[]가 있음), 데이터 중복 허용, 읽고 쓰기가 모두 가능
# 추가, 제거 , 삽입 모두 가능
# 타입여러개 혼용가능
# 파이썬의 기본타입은 4가지 (정수,문자열,논리,실수)
lst = [0,1,2,3,4,5,6]
print("lst=", lst)
print("lst타입 :", type(lst))
print("lst주소 :", id(lst))
print('lst[0]', lst[0])
print("lst 1번재에서 4번째 전 까지 출력 : ", lst[1:4]) #슬라이싱 : 리스트[begin:end]
print("lst 2부터 끝까지 출력 : ",lst[2:]) #리스트[begin:]
print("lst[:3] :",lst[:3])#3번 전까지 출력
print("lst[:] :",lst[:])#처음부터 끝까지 출력
print("lst[-2:]",lst[-2:])#오른쪽부터 두번째까지 출력
print("lst[:-2]",lst[:-2])#끝에 두개 빼고출력
print("lst요소의 수",len(lst))

#리스트의 연산
lst2 = [40,50,45]
print("리스트 더하기 : ", lst+lst2)#리스트 뒤에 다른리스트를 붙여줌
print("리스트 반복하기 : ", lst2*3)#리스트를 3번 반복하여 출력
#lst2[3]=65 #요소의 값 추가 X
lst2.append(65) #요소의 값 한개추가 append
lst2[1]=60 #요소의 값 변명
print("lst2 :",lst2)
lst2.insert(2,50) #요소의 중간삽입
print("lst2 :",lst2)
lst2.sort() #요소의 정렬 (작은것부터)
print("lst2.sort : ",lst2)
lst2.reverse()
print("lst2.revers :", lst2)
print("60의 인덱스 : ",lst2.index(60))
print("60의 요소개수 : ",lst2.count(60))
del lst[2] #인덱스를 이용한 제거 (lst이라는 리스트에서 3번째를 제거하라
print("lst : ",lst)
lst.remove(5) #5라는 값을 제거하라
print("lst : ",lst)
lst.extend([7,8,9])
print("lst : ",lst)