from random import *
import pytest


@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from sprint_challenge.Part_3 import fibonacci, coin_exchange

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def test_part3_fib_dont_use_recursion():
    from sprint_challenge.Part_3 import fibonacci

    assert fib(5) == fibonacci(5)
    assert fibonacci.cnt == 1, "재귀를 사용하면 안됩니다."


def test_part3_fib_return_correct_answer():
    from sprint_challenge.Part_3 import fibonacci

    for num in range(0, 30):
        assert fib(num) == fibonacci(num), f"피보나치 수를 반환해야합니다.{num}에서 문제가 발생했습니다"
    

def test_part3_coin_exchange_dont_use_recursion():
    from sprint_challenge.Part_3 import coin_exchange

    assert coin_exchange([100,200,300], 3, 400) == 4
    assert coin_exchange.cnt == 1, "재귀를 사용하면 안됩니다."


def test_part3_coin_exchange_return_correct_answer():
    from sprint_challenge.Part_3 import coin_exchange

    assert coin_exchange([100,200,300], 3, 400) == 4, "100원 200원 300원으로 400원을 만들 수 있는 방법은 4가지 입니다."
    assert coin_exchange([10,20,30], 3, 50) == 5, "10원 20원 30원으로 50원을 만들 수 있는 방법은 5가지 입니다."
    assert coin_exchange([10,20,30], 3, 1000) == 884, "10원 20원 30원으로 1000원을 만들 수 있는 방법은 884가지 입니다."
    
