a = 10
b = 20
c = 5


def test1():
    print(a)

def test2():
    return a

def test3(value):
    print(value)

def test4(value):
    return value

def main():

    test1()
    test2()
    print(a + test2())
    test3()

if __name__ == "__main__":
    main()