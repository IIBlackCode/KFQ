import random


class StudentInfo:

    def __new__(cls):
        print('new')
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        print('init')
        self.__name = '김민서'
        self.__studentNum = random.randint(1, 100)
        self.__kor = random.randint(1, 100)
        self.__math = random.randint(1, 100)
        self.__eng = random.randint(1, 100)
        self.__total = self.__kor + self.__math + self.__eng

    def display(self):
        print("이름 :",self.__name," 국어:",self.__kor, " 영어:", self.__eng, " 수학:", self.__math, " 총점 ", self.__total)
    
    #decorator pattern
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def kor(self):
        return self.__kor
    
    @kor.setter
    def kor(self, score):
        if score >= 0:
            self.__kor = score
            
    @property
    def math(self):
        return self.__math
    
    @kor.setter
    def math(self, score):
        if score >= 0:
            self.__math = score
            
    @property
    def eng(self):
        return self.__eng
    
    @kor.setter
    def eng(self, score):
        if score >= 0:
            self.__eng = score


# Create instance
s1 = StudentInfo()
s1.kor = 10 #public으로 보이지만 private변수
s1.display()

s2 = StudentInfo()
s2.name = "홍길동"
s2.kor = 19
s2.eng = 20
s2.math = 21
s2.display()