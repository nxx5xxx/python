#반복실행 for 내포문
lst = [90,70,80,60,85,75,65,95,90,80]
# [조건만족시 if 조건식 else 조건거짓시 for 변수 in 컬렉션]
res = ["합격" if su>=80 else "불합격" for su in lst]
#다른식
'''
for su in lst:
    if su>=80:
        res.append("합격")
    else:
        res.append("불합격")
'''
#다른식
'''
lst = [90,70,80,60,85,75,65,95,90,80]
res = []
for x in range(len(lst)):
    if lst[x]>=80:
        res.append("합격")
    else:
        res.append("불합격")
'''
#[계산식 for 변수 in 컬렉션]
py = [num/10 for num in lst]
#다른식
'''
py = []
for num in lst:
    py.append(num/10)
'''
#다른식
'''
lst = [90,70,80,60,85,75,65,95,90,80]
py = []
for x in range(len(lst)):
    num=lst[x]
    py.append(num/10) ##append는 배열추가
'''
for x in range(len(lst)):
    print(x+1,"번째\t","최종 : ",res[x],"\t평점 :",py[x])
