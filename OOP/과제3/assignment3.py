# [과제3][본인이름] 다음 조건에 맞도록 lamba 표현식으로 프로그래밍하시오.
# 다음 files 데이터에서 확장자가 *.jpg, *.png인 이미지 파일만 출력하는 프로그램을 1) 일반함수, 2) 람다표현식을 활용해 프로그래밍 하시오.
# 힌트) list(), filter(), find()
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

def 일반함수():
    global files
    result = []
    for i in files:
        if '.jpg' in i or '.png' in i:
            result.append(i)    
    return result

def 람다표현식():
    return list(filter((lambda x: '.jpg' in x or '.png' in x), files))
print("일반함수\t: ",일반함수())
print("람다표현식\t: ",람다표현식())