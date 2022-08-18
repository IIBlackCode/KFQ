#[과제1][김민서] for문과 if문 등의 제어문으로 다음과 같이 출력하도록 python 프로그래밍하시오.
for i in range(1,6):
    for j in range(1,6):
#         print("*", end= " ")
        print("[",i,",",j,"]", end= " ")
    else:
            print(" ", end= " ")
    print("")

print("1). ")
for i in range(1,6):
    for j in range(1,6):
        print("*", end= " ")
#         print("[",i,",",j,"]", end= " ")
    else:
            print(" ", end= " ")
    print("")

print("2). ")
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*", end= " ")
#             print("[",i,",",j,"]", end= " ")
        else:
            print(" ", end= " ")
    print("")

print("3). ")
for i in range(1,6):
    for j in range(1,6):
        if i+j >= 6:
            print("*", end= " ")
        else:
            print(" ", end= " ")
#             print("[",i,",",j,"]", end= " ")
    print("")
print("4). ")
for i in range(0,7):
    for j in range(0,7):
        # print("[", i, ",", j, "]", end=" ")
        # '''
        if (i>=j)and(i+j >= 6):
            print("*", end= " ")
        else:
            print(" ", end= " ")
#             print("[",i,",",j,"]", end= " ")
#         '''
    print("")