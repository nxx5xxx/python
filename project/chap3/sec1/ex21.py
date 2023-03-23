#클래스
#class 클래스명 :
class Student:
    '''
생성자
def __init__(self, 생성자명,생성자명2,생성자명3):
    self.생성자명 = 생성자명
    self.생성자명2 = 생성자명2
    self.생성자명3 = 생성자명3
    self는 this와 같다고 보면된다
    '''
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr


#메소드
#    def 메소드명(self):


    def print_st(self): #self를 불러옴
        print(" 이름 : ", self.name)
        print(" 나이 : ", self.age)
        print(" 주소 : ", self.addr)


#생성
#변수명 = 클래스명()
#student1 = Student() 또는
#student2 = Student("이름","메일","주소")


#student2 = Student()
student1 = Student("강아지","5","경기도고양시일산구")

#호출

student1.print_st()