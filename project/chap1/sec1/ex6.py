#딕셔너리(dictionary = dict):키(key)와 값(value)을 튜플 형식의 데이터로서 집합연산이
#해당 키는 중복이 될 수 없으며, 값은 중복 될 수 있음
data1 = {'name':'강아지','age':'4','tel':'032-559-5959'}
data1['birth']= '19-03-01' #값의 추가
data1['point'] = [90,100,80] #리스트를 요소로 추가
print("data1 의 타입 : ",type(data1))
print("data1의 주소 : ",id(data1))
print("data1의 데이터 집합 : ",data1)
print("data1의 요소의 개수 :",len(data1))
keyname=data1.keys()
print("data1의 키이름만 모으기 :",keyname)
valuename=data1.values()
print("data1의 값 끼리 모으기 : ",valuename)
data1_tuple=data1.items() #순서쌍의 튜플로 모으기
print("data1의 순서쌍의 튜플 : ",data1_tuple) #튜플 : 읽기전용
print("특정 값만 출력 : ",data1.get('name'))
print("특정 값만 출력 2 : ",data1['age'])
print("특정 요소의 존재유무 : ", 'point' in data1)
del data1['tel']
print("data1의 tel을 지우고 출력",data1)
data1.clear()
print("data1의 모든요소 제거",data1)