#리스트를 하나의 문자열로 만드는 함수를 정의하세요
#split과 join은 문자에 관련된 함수라 숫자로하면안됨

# toString() 리스트를 하나의 문자열로 만드는 함수
#join

def toString(x,y):
    return y.join(x)

#강사님답안
# def toString(lst, sep):
#     res = sep.join(lst)
#     return res

# toList() 하나의 문자열을 분리하여 리스트로 만드는함수
#split

def toList(x,y):
    return x.split(y)
#강사님답안
# def toList1(data, sep):
#     res = data.split(sep)
#     return res