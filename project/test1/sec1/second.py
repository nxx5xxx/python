# 1000미만의 자연수에서 3과 5의 배수의 총합 계산
sum=0
for x in range(1,1000):
    if x%3==0 and x%5==0 :
        sum+=x
print("1000 미만의 자연수에서 3과 5의 배수의 총합 : ",sum)
