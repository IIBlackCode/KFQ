import dis
import pytest

def list_func_calls(fn, s):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname==s:
            cnt += 1
    return cnt

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_2 import anagram, assert_anagram_time_complexity, \
            recursiveFun1_time_complexity,recursiveFun2_time_complexity, recursiveFun3_time_complexity

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_anagram():
    from sprint_challenge.Part_2 import anagram

    assert list_func_calls(anagram, 'FOR_ITER') >= 1, "반복문을 꼭 사용해야합니다."
    assert anagram('newyork times') == anagram('monkeys write'), "아나그램의 여부를 판단해야합니다."
    assert anagram('madam curie') == anagram('radium came'), "아나그램의 여부를 판단해야합니다."
    assert anagram('dormitory') == anagram('dirtyroom'), "아나그램의 여부를 판단해야합니다."
    assert anagram('dormitory') != anagram('cleanroom'), "아나그램의 여부를 판단해야합니다."
    assert anagram('Oh, lame saint!') != anagram('The Mona Lisa!'), "아나그램의 여부를 판단해야합니다."

def test_anagram_time_complexity():
    from sprint_challenge.Part_2 import assert_anagram_time_complexity

    res_as = 0
    res = assert_anagram_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."

def test_recursiveFun1_time_complexity():
    from sprint_challenge.Part_2 import recursiveFun1_time_complexity

    res_as = 0
    res = recursiveFun1_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."

def test_recursiveFun2_time_complexity():
    from sprint_challenge.Part_2 import recursiveFun2_time_complexity

    res_as = 0
    res = recursiveFun2_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."

def test_recursiveFun3_time_complexity():
    from sprint_challenge.Part_2 import recursiveFun3_time_complexity

    res_as = 0
    res = recursiveFun3_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 414,"정확한 시간복잡도를 반환해야합니다."