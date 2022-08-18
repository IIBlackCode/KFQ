import random2


class StudentInfo:

    def __new__(cls):
        print('new')
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        print('init')
        self.__studentNum = random2.randint(1, 100)
        self.__kor = random2.randint(1, 100)
        self.__math = random2.randint(1, 100)
        self.__eng = random2.randint(1, 100)
        self.__total = self.__kor + self.__math + self.__eng

    def display(self):
        print("국어:",self.__kor, " 영어:", self.__eng, " 수학:", self.__math, " = ", self.__total)


# Create instance
s1 = StudentInfo()
s1.kor = 10

s2 = StudentInfo()
s2.display()