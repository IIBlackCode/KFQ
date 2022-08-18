#STATIC과 CLASS의 차이
class Hello:
    num = 10
    t = '내가 상속해 줬어'

    #class : 메모리가 할당될 때 인스턴스의 유무 관계없이 호출가능
    @classmethod
    def calc_class(cls,x):  #첫번째 인수가 self가 아닌 cls(클래스에 대한 정보)
        return x + 10

    @classmethod
    def t_class(cls):  # 첫번째 인수가 self가 아닌 cls(클래스에 대한 정보)
        return cls.t

    #static :  메모리 특성상 전역(함수적 개념)에 해당
    #원래 static으로 선언해서 class처럼 사용
    #main보다 먼저 메모리에 할당되기 때문에 전역에 걸처 사용이 가능
    #원칙상 main도 static에 해당, Java는 main함수에 static이 붙는다.
    #class 밖에서 가장 밖에 함수나 변수를 선언하게 되면 전역변수,함수가 된다.
    #class 안에 선언된 함수를 method, class안에 선언된 static 함수는 클래스 소속으로 관리
    '''
        #class변수와 static변수 차이
        class변수 : 클래스 정보를 인수로 전달받아야 한다.
        static변수 : 전역에 존재하기 때문에 인수를 전달받을 필요가 없다.
        이 두 변수는 상속에서 큰 차이를 본다.
    '''
    @staticmethod
    def clac_static(x):
        return x + 40
    @staticmethod
    def t_static():
        return Hello.t

    def display(self,x):
        print('display x : ',x)

class HelloChild(Hello):
    t = '나는 상속받았어'

h = Hello()
print(" class : ",h.calc_class(10), " static: ",h.clac_static(10))
print(" class : ",Hello.calc_class(10)," static: ",Hello.clac_static(10))
h.display(20)

hc = HelloChild()
print('class :',HelloChild.t_class()) # 해당 클래스의 정보를 인수로 전달하기 때문에 HelloChild의 변수가 리턴됨
print('static:',HelloChild.t_static())
