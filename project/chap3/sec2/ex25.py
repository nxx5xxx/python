#Wordpro를 import하여  alias를써서 짧은호출을 만들고
#리스트를 문자열로
#문자열을 리스트로 만들어보세요

import chap3.sec1.Wordpro as wp
lst = ["java","C","dev","python"]

str1=wp.toString(lst,"---")
print(str1)

str="우리는-하나-입니다"
lst1=wp.toList(str,'-')
print(lst1)
