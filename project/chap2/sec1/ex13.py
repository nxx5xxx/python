#조건문 : if , if else , if elif else
x= True
if x:
        print("True의 값")
        print("True의 값2")
print("tab을 치지않은 값")
'''
=
if(x){
        System.out.println("True의 값");
        System.out.println("True의 값2");
}
System.out.println("tab을 치지 않은값");
'''
y=90;
if y>=70: print("70보다 큽니다.")
'''
=
if(y>=70) System.out.println("70보다 큽니다.");
'''

#판정은 모든 과목이 50점 이상이고, 평균이 70 이상이면, 합격 아니면 불합격
a = int(input("과목 1의 점수를 입력하세요 : "))
b = int(input("과목 2의 점수를 입력하세요 : "))
c = int(input("과목 3의 점수를 입력하세요 : "))
avg = float((a+b+c)/3)
if a>=50 and b>=50 and c>=50 and avg>=70: print("합격하셨습니다, 축하드립니다.")
else : print("탈락")
#elif
if avg>=90 : print("5수준\t합격")
elif avg>=80 : print("4수준\t합격")
elif avg>=70 : print("3수준\t유보")
elif avg>=60 : print("2수준\t불합격")
else : print("1수준\t불합격")

#중첩if를 사용해서
#셋중에 한개가 100점일경우 과목 만점자
#평균이 90~100사이에만 있을경우 전체점수에대해 칭찬
#평균이 90점이상이 아니고 만점이 있을경우
if avg>=90:
        if a==100 or b==100 or c==100 :
                print("과목만점자")
        else :
                print("전체적인 성적이 우수합니다")
else :
        if a==100 or b==100 or c==100:print("전체적인 성적이 우수하지는 않으나 그래도 잘하는 과목이 있습니다")
        else: print("다른 적성을 찾아보세요")