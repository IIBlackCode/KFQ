import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_1 import first_test, second_test, third_test, b_sort
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_first_test():
    from sprint_challenge.Part_1 import first_test

    res_as = 0
    res = first_test()
    for i in res:
        res_as += ord(i)
    assert res_as == 414, "정확한 시간복잡도를 반환해야합니다."


def test_second_test():
    from sprint_challenge.Part_1 import second_test

    res_as = 0
    res =  second_test()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."


def test_third_test():
    from sprint_challenge.Part_1 import third_test

    res_as = 0
    res =  third_test()
    for i in res:
        res_as += ord(i)
    assert res_as == 414, "정확한 시간복잡도를 반환해야합니다."


def test_b_sort():
    from sprint_challenge.Part_1 import b_sort

    node = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    res_as = 0
    res =  b_sort(node)
    for i in res:
        res_as += ord(i)
    assert res_as == 414, "정확한 시간복잡도를 반환해야합니다."
