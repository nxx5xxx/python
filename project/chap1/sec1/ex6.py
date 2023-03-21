#딕셔너리(dictionary = dict):키(key)와 값(value)을 튜플 형식의 데이터로서 집합연산이
#해당 키는 중복이 될 수 없으며, 값은 중복 될 수 있음
data1 = {'name':'강아지','age':'4','tel':'032-559-5959'}
data1['birth']= '19-03-01' #값의 추가
print("data1 의 타입 : ",type(data1))
print("data1의 주소 : ",id(data1))
print("data1의 데이터 집합 : ",data1)