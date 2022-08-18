#학번 이름 국어 영어 수학 총점

class Student:
    # instance 변수
    def __init__(self,num,name,국어,영어,수학):
        self.num = num
        self.name = name
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.총점 = 국어+영어+수학

    def display(self):
        print(self.num," ",self.name," ",self.국어," ",self.영어," ",self.수학," ",self.총점)

student1 = Student(1,"홍길동",25,34,56)
student2 = Student(2,"김길동",56,78,34)
student3 = Student(3,"이길동",78,56,78)

student1.display()
student2.display()
student3.display()