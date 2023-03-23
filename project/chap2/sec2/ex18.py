#출력제어

'''
코드설명
%c  문자                 %s 문자열
%i                      %d  10진수 정수
%u
%x 16진수
%e 지수
%f 실수
%g                      %G
%% %를출력
%' '를출력               %" "를출력

'''
#print를 printf처럼 쓰려면 pinrt("%x"% y)를쓰면된다 뒤에 변수명이 오는것앞에 %가 최초 ,로 볼수있다
#여러개를 쓰기위해서는 print("%d %s %f" % (x,y,z)) 로 쓸 수 있다
x=1004
str="""벌써
오늘이
목요일이라니
"""
flo= 3.141592
print("x정수  x=%d"%x)
print("8진수  x=%o"%x)
print("16진수 x=%x"%x)
print("문자열  str=%s"%str)
print("문자 str[1]=%c"%str[1])
print("flo = %f"%flo)
print("flo = %15f"%flo) #+15 오른쪽 정렬 -15는 왼쪽정렬로 볼수있다
print("flo = %0.4f"%flo)
print("flo = %.4f"%flo)
print("%d %s %f"% (x,str,flo))

'''
이스케이프 문자        이름              아스키값 (Numberic Value)
\b                  백스페이스              8
\t                  탭                     9
\n                  라인피드               10
\f                  폼피드                 12
\r                  캐리지                 13
\\                  역슬래시               92
\'                  작은따옴표              39
\"                  큰따옴표               34
'''
id = "강아지"
age = 50
height = 20.5
weight = 8
print("name\tage\theight\tweight")
print("%3s\t%3d\t%3.1f\t%3d\t"%(id,age,height,weight))
print("경로표시 d:\\woozookim\\python\\project\\chap2\\sec2\\ex18.py")
print("큰따옴표를 표시하기위해서는 \" \\\" \" 를 써야합니다")

# .fotmat 함수 익히기
print("id : {} , age : {}, height : {} , weight : {}".format(id,age,height,weight))
print("id : {1} , age : {3}, height : {0} , weight : {2}".format(height,id,weight,age))
print("id : {1} , age : {3:d}, height : {0:f} , weight : {2:d}".format(height,id,weight,age))
print("id : {1:4.2s} , age : {3:5d}, height : {0:.2f} , weight : {2:5d} \n\n\n\n".format(height,id,weight,age))
#문자열(s)의 경우는 들여쓰기 내어쓰기가 다른것들처럼 제대로 작동하지않고 > < ^ *를써야한다
#> < ^ *는 문자,숫자 상관없이 사용가능
print("id : {0:>10}".format(id)) # n에서 내 글자수만큼 빼고 우측으로가라(띄어쓰기해라)
print("id : {0:<10}".format(id)) # n에서 내 글자수만큼 빼고 좌측으로
print("id : {0:^12}".format(id)) # 나를 가운데로 놓고 좌우같게 (단, 홀수로 떨어질경우 왼쪽이 더 좁음)
print("id : {0:x^12}".format(id)) #나를 가운데로놓고 공백은 x로 채운다(x는 다른값이 될수있음)
print("나이 : {0:o}".format(age)) #8진수
#50 에 2가 5번 들어가니까 2*5 =10 10에도 2가 1번 들어가니까 12 50+12 =62
print("나이 : {0:x}".format(age)) #16진수
#50에 16이 3번들어가니까 30 50-48=2니까 30+2