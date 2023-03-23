'''
내장모듈이미지만 임포트가 필요한 함수
venv에 내장모듈이 깔린다 (프로젝트를 생성하면 알아서 생성됨)
외부모듈은 External Libraries에 있다
외무모듈을 쓰려면 import가 필요하다
statistics는 집계함수가 깔려있는 모듈
math는 수학함수가 깔려있다
##
import statistics
import math
로 쓸 수도있고 
import statistics, math
처럼 여러모듈을 할꺼번에 불러올수도있다
##
내가만든 모듈을 갖고오려면 (같은디렉토리) -모듈은 ~.py를 말하는것
import 패키지명.클래스이름
ex) import sec1.ex20

하나의 모듈에서 특정함수 한개만 불러오는것은 
from sec1.ex20 import fnc1

특정한값만 불러오는 이유는 메모리 절약을 위해
'''

#모듈을 불러와서 아직 사용하지않으면 회색으로 표시됨
#import statistics, math
lst = [80, 90, 100, 70, 80, 90, 85, 65, 75]
print("lst의 개수 : ", len(lst),"\nlst : ", lst)
print("lst의 합계 : ", sum(lst))

#평균 : mean - statistics가 있어야 사용가느으하다
#엔터는 ,\을 한 후 엔터
from statistics import mean, harmonic_mean, geometric_mean, stdev, variance,\
    median,mode
#산포도
print("산술평균(일반 평균) : ", mean(lst))
print("조화평균(추이)(산술평균의역수) : ",harmonic_mean(lst))
print("기하평균 : ",geometric_mean(lst))
print("표준편차 : ", stdev(lst))#stdev = 스탠다드 데벌레션
print("분산 : ", variance(lst))
print("중간값(중위수를 뜻함) : " , median(lst))
print("최빈값(최고 빈도수가 많은수) : ", mode(lst))

import math as m
# alias : as
print(m.sqrt(2)) #x의제곱근 (루트x)
print(m.pi)
print(m.pow(4,5)) #math.pow(x,y) x^5
print(m.cos(30))
print(m.sin(30))
print(m.tan(30))
print(m.ceil(55.222)) #올림
print(m.floor(55.888)) #버림
#print(m.round(55.444) #반올림 math엔 없다
print(m.trunc(55.955)) #절사 : 소수점 이하를 없앰
print(m.gcd(60,35)) #최대공약수
print(m.lcm(60,35)) #최소공배수