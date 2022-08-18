import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_3 import added_word, added_word_time_complexity

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_added_word_time_complexity():
    from sprint_challenge.Part_3 import added_word_time_complexity

    res_as = 0
    res = added_word_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."

def test_added_words_working_normally():
    from sprint_challenge.Part_3 import added_word
    
    assert 'is' == added_word('the best', 'the best is')
    assert None == added_word('the best is', 'the best')
    assert 'states' == added_word('code', 'code states')
