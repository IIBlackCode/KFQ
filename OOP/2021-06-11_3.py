class Person:
    d = "아빠"

    def __init__(self):
        self.data = self.d

    #cls : 현 클래스의 정보
    @classmethod
    def class_person(cls):
        return cls()

    #self도 아니고 클래스소속도 아님
    @staticmethod
    def static_person():
        return Person()

class WhatPerson(Person):
    d = "엄마"

person1 = WhatPerson.class_person()
person2 = WhatPerson.static_person()
print(person1.d)
print(person2.d)