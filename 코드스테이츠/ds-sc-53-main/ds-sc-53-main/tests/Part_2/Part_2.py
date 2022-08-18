import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from sprint_challenge.Part_2 import graph_algorithm

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_graph_algo():
    from sprint_challenge.Part_2 import graph_algorithm

    weighted_graph = {  
        "s1":{"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5":3},
        "s2":{"s1": 1, "s2": 0, "s10": 2, "s12": 2, "s5":2},
        "s10":{"s1": 2, "s2": 6, "s10": 0, "s12":3, "s5":4},
        "s12":{"s1": 3, "s2": 5, "s10": 2, "s12":0,"s5":2},
        "s5":{"s1": 3, "s2": 5, "s10": 2, "s12":4,"s5":0},
    }
    path_list2 = graph_algorithm(weighted_graph, 's1')
    assert path_list2 == [('s1', 's2'), ('s2', 's10'), ('s10', 's12'), ('s12', 's5')]
