hello = 'global'


def print_hello():
    hello = 'Hello, world!'

    def print_message():
        nonlocal hello
        hello = 'inner function'
        print('지역변수(inner function)이 아닌 outer변수 호출하려면?')
        print(hello)  # 근접접근 원리에 따라 호출

    print_message()


print_hello()