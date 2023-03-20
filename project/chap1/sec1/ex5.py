#셋(set) : 집합 . 순서가없는 자료형으로 데이터 중복이 없음
#자료의 추가, 삭제 등이 가능, 합집합, 차집합등의 연산이 가능
# {}로 값을 대입하고 , 초기화함
#비 순서형 자료라 함

lst1 = [80,90,70,80,60,70]
s1 = {80,90,70,80,60,70}
s2 = {40, 70, 65, 75, 60, 85}
print("lst1 : ",lst1)
print("lst1의 타입 : ", type(lst1),"\n lst1의 길이 :", len(lst1),)
print("s1 : ",s1)
print("s1의 타입과 길이",type(s1),len(s1))
print("s1과 s2의 교집합 : ", s1&s2)
print("s1과 s2의 교집합2 :", s1.intersection(s2))
print("s1과 s2의 합집합 : ", s1|s2)
print("s1과 s2의 합집합2 : ", s1.union(s2))
print("s1과 s2의 차집합 : ",s1-s2)
print("s1과 s2의 차집합2 : ",s1.difference(s2))
#리스트에서 중복된것을 제거하고싶을땐 set으로 변경
lst1 = set(lst1)
print("set타입으로 바뀐 lst1 :" , lst1)
print("s1 => ",s1)
s1.add(99) #원소의 추가 (비순서형이라 아무곳에 추가됨)
print("s1 1개의 원소를 추가 => ",s1)
s1.update([55,86,78]) #원소 여러개 추가
print("s1 여러개 원소를 추가 => ",s1)
s1.remove(78) #원소를 제거
print("s1 78이라는 값을 제거=> ",s1)
