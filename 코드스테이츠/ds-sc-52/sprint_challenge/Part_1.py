# 1번 문제 - 파이썬과 자료구조의 시간복잡도 (총 문제 : 4개)
# 아래 코드를 분석하면서 시간복잡도를 작성해주세요.

ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 

def first_test():

    test_list = {}
    for first_index in range(0, 10):
        test_list[first_index] = first_index

    for first_index in range(0, 10): #중첩 반복문
        for second_index in range(0, 10):
            test_list[first_index] * test_list[second_index]

    return QUADRATIC


def second_test():
    test_list = [1,2,3,6,4,9,10,12]
    test_target = 12
    for index in range(0, len(test_list)): #반복문 1개
        print(test_list[index], test_target)
        if test_list[index] == test_target:
            print("Yes")
            break
        else:
            print("No")
            break
    return LINEAR


def third_test():
    first_list = [1,2,3]
    second_list = [12,13,14]    

    for first_index in first_list:
        for second_index in second_list:
            if (first_index + second_index) % 2 == 0:
                print("짝수")

            else:
                print("홀수")
    return QUADRATIC


def b_sort(node):
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(node) - 1):
            if node[i] > node[i+1]:
                node[i], node[i+1] = node[i+1], node[i]
                swap_bool = True

    return QUADRATIC
    

if __name__ == '__main__':
    print("===== first_test =====")
    print(first_test())

    print("===== second_test =====")
    print(second_test())

    print("===== third_test =====")
    print(third_test())

    print("===== b_sort =====")
    node = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    print(b_sort(node))