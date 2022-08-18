# 2번 문제 - 알고리즘과 시간복잡도
    # 주어진 문제에 따라 알고리즘 로직을 파악하고 코드를 구현한다.
    # 구현된 코드의 시간복잡도에 대해 확인한다.
        # 주의사항 : 구현되는 코드에 따라 시간복잡도는 달라질 수 있으니 
        # 알고리즘 로직과 시간복잡도의 개념을 개별적으로 고려해야 한다.

ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 

# 2-1)2개의 단어를 입력받고, 두 단어가 anagram 인지 여부(True or False)를 출력해주는 코드를 구현하세요.
# if __name__ == '__main__': 구문 아래에서 아나그램 여부를 파악하기 위해 anagram 함수를 작성해주세요.
# 단 반복문을 꼭 사용해야합니다.

def anagram(test_word):
    list = []
    for i in range(len(test_word)):
        list.append(test_word[i])

    for i in range(len(test_word ) -1):
        for j in range(len(test_word) -1):
            # print(i,'회전 :',test_word)
            # print('[i]',list[i],ord(list[i]))
            # print('[j + 1]',list[j + 1], ord(list[j + 1]))
            if ord(list[i]) > ord(list[j + 1]):
                temp = list[i]
                list[i] = list[j+1]
                list[j+1] = temp
                print(list)
    print('RESULT : ',list)
    return list


def assert_anagram_time_complexity():
    return LINEAR

# 2-2) recursive(재귀)에 대한 문제를 해결해보자.
# 주어진 아래의 함수를 분석하며 예상되는 시간복잡도를 서술하세요.

def recursiveFun1(n): # 해당 함수의 코드를 수정하지 마세요
    if n <= 0:
        return 1
    else:
        return 1 + recursiveFun1(n-1)

def recursiveFun1_time_complexity():
    return LINEAR


# 2-3) recursive(재귀)에 대한 문제를 해결해보자.
# 주어진 아래의 함수를 분석하며 예상되는 시간복잡도를 서술하세요.

def recursiveFun2(n): # 해당 함수의 코드를 수정하지 마세요
    if n <= 0:
        return 1
    else:
        return 1 + recursiveFun2(n-5)

def recursiveFun2_time_complexity():
    return ANSWER # 답안을 작성해주세요.

# 2-4) recursive(재귀)에 대한 문제를 해결해보자.
# 주어진 아래의 함수를 분석하며 예상되는 시간복잡도를 서술하세요.

def recursiveFun3(n): # 해당 함수의 코드를 수정하지 마세요
    for i in range(0,n,2):      
        pass

    if n <= 0:
        return 1
    else:
        return 1 + recursiveFun3(n-5)

# newyork times
# monkeys write

def recursiveFun3_time_complexity():
    return ANSWER # 답안을 작성해주세요.

if __name__ == '__main__':
    print("===== anagram =====")
    test_word1 = input("첫번째 단어입력 :")
    test_word2 = input("두번째 단어입력 :")
    print("anagram 여부 :", anagram(test_word1))

    print("===== recursiveFun1 Argument Test =====")
    print(recursiveFun1(5))
    print(recursiveFun1_time_complexity())

    print("===== recursiveFun2 Argument Test =====")
    print(recursiveFun2(5))
    print(recursiveFun2_time_complexity())
