class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 아래 humans에 할당된 list object는 다음과 같다.
# Human("이름", 연령)

humans = [ #리스트
    Human("Abi", 29),  ## 개별 인스턴스 생성 
    Human("Batista", 32),
    Human("Charlse", 37),
    Human("Dolphine", 30),
    Human("Eva", 26),
    Human("Frin", 18),
    Human("Gless", 42),
    Human("Harby", 12),
    Human("Iris", 41),
    Human("David", 31)]

# humans에 할당된 list object와 출력조건을 확인하며 이름과 연령을 구해보자.

# 1-1) 이름을 출력해보자.
# 출력조건 : 'D'로 시작하는 이름을 출력하자. /// startwith
def quesion1():
    print("Starts with D:")

    for human in humans:
        name = human.name

        if name.find('D') == 0:
            print("D로 시작함",name)
        else:
            print("D로 시작하지 않음",name)
            a = name
    print(a)
    return (a)


# # 1-2) 이름을 출력해보자.
# # 출력조건 : 'e'로 끝나는 이름을 출력하자. // endwith
def quesion2():
    print("Ends with e:")
    b = []
    for human in humans:
        name = human.name
        # print(name[len(name)-1])
        if name[len(name)-1] == 'e':
            print("e로 끝나는 이름 :", name)
            b.append(name)
        else:
            print("e로 끝나지 않음 : ", name)
    print(b)
    return(b)

# # 1-3) 이름을 출력해보자.
# # 출력조건 : 이름스펠링이 'C' 와 'G' 사이로 시작하는 이름을 출력하자.
def quesion3():
    print("Starts between C and G, inclusive:")

    c = []
    for human in humans:
        name = human.name
        # print(name[0],ord(name[0]))
        if name[0] >= 'C':
            if  name[0] <= 'G' :
                print("C와 G사이로 시작하는 이름 :", name)
                c.append(name)
            else:
                print("아닌것 : ", name)
        else:
            print("아닌것 : ", name)

    print(c)
    return(c)

# # 1-4) 연령을 출력해보자.
# # 출력조건 : 주어진 모든 연령에 대해 10을 더한상태의 연령을 출력하자.
def quesion4():
    print("Ages plus 10:")
    d = []
    for human in humans:
        print(human.name, human.age,human.age + 10)
        d.append(human.age + 10)
    print(d)
    return(d)

# # 1-5) 이름과 연령을 출력해보자.
# # 출력조건 : '이름-연령'의 형식으로 이름과 연령을 출력하자.
def quesion5():
    print("Name hyphen age:")
    e = []
    for human in humans:
        tmp = human.name +"-"+ str(human.age)
        print(tmp)
        e.append(tmp)
    print(e)
    return(e)

# # 1-6) 이름과 연령을 출력해보자.
# # 출력조건 : '이름-연령'의 형식으로 27~32세의 연령을 갖고 있는 사람의 이름과 연령을 출력하자.
def quesion6():
    print("Names and ages between 27 and 32:")
    f = []
    for human in humans:
        tmp = human.name +"-"+ str(human.age)
        if 27 <= human.age <= 32:
            print(tmp)
            f.append(tmp)
    print(f)
    return(f)

# # 1-7) 이름과 연령을 출력해보자.
# # 출력조건 : ("이름", 연령)의 형식으로 이름을 대문자로 변경시키고 연령에 5를 더한상태의 이름과 연령을 출력하자.
def quesion7():
    print("All names uppercase:")
    g = [tuple(human.name, human.age+5) for human in humans]
    # for human in humans:
    #     human.age = human.age + 5
    #     tmp = (human.name,human.age)
    #     print(tmp)
    #     g.append(tmp)
    print(g)
    return(g)

# # 1-8) 연령을 출력해보자.
# # 출력조건 : 모든 연령을 제곱근으로 변경시키고, 제곱근에 대해 소수점 2째자리까지 표현하는 연령을 출력하자. (결과값은 반올림을 해야하며 반올림관련 내장함수를 활용해야 합니다.)
def quesion8():
    print("Square root of ages:")
    h = [round(human.age**(1/2),2) for human in humans]
    print(h)
    return(h)

if __name__ == "__main__":
    # quesion1()
    # quesion2()
    # quesion3()
    # quesion4()
    # quesion5()
    # quesion6()
    quesion7()
    # quesion8()

