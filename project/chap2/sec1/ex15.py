#for

'''
for x in range(begin,end,[step]):
=
for(int x=begin,x<end,x++){}
'''
lst = [90,70,80,60,85,75,65,95,90,80]
for x in range(len(lst)):
    if lst[x]>=80 :
        print(x+1,"번째 합격")
    else:
        print(x+1,"번째 불합격")

for x in lst:
    if x>=80:
        print("합격")
    else:
        print("불합격")
#for in range를 활용하여 0~100의 5의 배수의 합계를 계산하라
sum=0
for x in range(0,101):
    if x%5==0: sum+=x
print("5의배수 합계",sum)

#다른방법
tot =0
for i in range(0,101,5) :
    tot+=i
print("5의배수 합계",tot)

#다른방법2
tot=0
for i in range(0,int(100/5)+1): #5의배수 개수만큼 실행 (20개지만 range는 전까지 실행이니까 (<) +1을한것)
    tot+=i*5
print("5의배수 합계",tot)