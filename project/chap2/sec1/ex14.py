#while 조건 :
#       반복실행구간

#스코어와 작업번호를 입력받고
#0이면 작업종료 , 1이면 점수를 입력, 2점수 리스트 출력, 3이면 통계를 낸다
score = [0,0,0,0]
count = 0
i=0
tot=0
while True:
    x = int(input("작업번호 [0:작업종료 1:점수 입력 2:리스트출력 3:통계]"))
    if x==0 :
        print("작업을 종료합니다")
        break
    elif x==1:
        if count<len(score):
            score[count] = int(input("점수입력 :"))
            count+=1
        else : print("범위를 초과했습니다")
    elif x==2:
            print("리스트 : ",score)
#            print("리스트: ",score[i])
    elif x==3:
        while i<count :
            tot += score[i]
            i+=1
        print("점수의 합:", tot)
    else:
        print("번호를 잘못 입력하셨습니다")

#while문을 활용하여 1~100짝수의 합계
x=0
sum=0
while x<=100:
    x+=1
    if x%2==0:sum+=x
print(sum)

#2씩증가해서 더하는방법
x=0
sum=0
while x<=100:
    sum+=x
    x+=2
print(sum)

#홀수일때 지나치는방법
x=0
sum=0
while(x<=100):
    if x%2!=0:
        continue
    sum+=x
    x+=1
print(sum)

#while과 if문을 활용하여 10명 점수의 판정을 계산하여 출력
#판정은 점수가 80점 이상이면, "합격", 60점 이상이면, "재평가" 60미만이면"탈ㄹㄹ락"
#대입연산자 x+=1은 불가 ex9참조
lst = [90,70,80,60,85,75,65,95,90,80]
x=0
while x<len(lst):
    if(lst[x]>=80):
        print(x+1,"번째 합격")
    elif(lst[x]>=60):
        print(x+1,"번째 재평가")
    else:
        print(x+1,"번째 탈ㄹㄹㄹ락")
    x+=1
