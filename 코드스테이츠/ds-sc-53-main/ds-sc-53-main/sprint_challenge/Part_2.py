# 아래 함수를 구현하자.
def graph_algorithm(graph, start):
    
    node_list = list(graph) 
    node_list.remove(start)
        
    visit_node = [start]
    path_list = []
    next_node = None
# [human.name + '-'+ str(human.age) for human in humans if 27 <= human.age <= 32] 
    while node_list:
        distance_of_node = 10
        for start_index in visit_node:
            print('start_index : ',start_index)
            print('visit_node : ',visit_node)
            print("=========================================================================")
            sum = 0
            for distance_index in graph[start_index]: # 키값을 요소로 활용 s1, s2, ...
                ##### 소스코드 작성 #####
                for distance_index2 in graph[start_index] :
                    print('(',distance_index,',',distance_index2,') 값:',graph[distance_index][distance_index2])
                    # 최소값 조건
                    # 현재도시 제외
                    if distance_index != distance_index2:
                        # 방문도시 제외

                        min_v = graph[distance_index][distance_index2]
                        if graph[distance_index][distance_index2] < min_v:
                            min_v = graph[distance_index][distance_index2]

                sum += min_v

                print(sum)
        # sum < distance_of_node 넘지않는 조건
        # return 배열
        if sum < distance_of_node :
            pass
        
    return path_list

if __name__ == '__main__':
    weighted_graph = {  
        "s1":{"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5":3},
        "s2":{"s1": 1, "s2": 0, "s10": 2, "s12": 2, "s5":2},
        "s10":{"s1": 2, "s2": 6, "s10": 0, "s12":3, "s5":4},
        "s12":{"s1": 3, "s2": 5, "s10": 2, "s12":0,"s5":2},
        "s5":{"s1": 3, "s2": 5, "s10": 2, "s12":4,"s5":0},
    }

    path_list2 = graph_algorithm(weighted_graph, 's1')
    print(path_list2)
