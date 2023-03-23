'''
import chap3.sec1.Calculator
print(chap3.sec1.Calculator.plus(5, 4))
'''

#알리아스를 써서
import chap3.sec1.Calculator as cal
print(cal.plus(5,4))
print(cal.minus(10,15))
print(cal.multi(10,3))
print("%.2f" % cal.divide(10,3))