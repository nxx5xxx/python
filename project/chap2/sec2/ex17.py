#출력제어 : print , 이스케이프문자 , 형식제어자 , format
name = "강아지"
age = 10
#sep
print("이름",name,"\n나이",age,sep="=") #,사이에 =을 넣어줌
#이스케이프 문자 : \n \t \f

#형식지시자 : %s, %d, %f , ....
print("이름: %s \n나이: %d" % (name, age))
'''
print를 printf처럼 사용이가능하다
ex) print("name=%s age=%d" % (name,age))
'''
#format 함수
print("당신의 이름은 {}이며, 나이는 {}세 입니다.".format(name, age)) #{}는 인자를 뜻함
print("제가 가장 좋아하는 치킨은{1},{0},{2}입니다".format("후라이드","양념","간장")) #{x}순서대로 0,1,2로 들어감