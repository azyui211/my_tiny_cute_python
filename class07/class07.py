
### 함수는 언제 만들어서 쓰는 것일까 ###

'''
두줄요약 : 함수를 만들지 않고 프로그래밍해도 전혀 문제없지만
          반복되는 명령이 많아서 코드가 길어질 때 선택적으로 사용.

예시) 버튼 UI 만들기
'''
from PySide2.QtWidgets import QPushButton


buttonA = QPushButton()
buttonA.align("Left")
buttonA.font("Arial")
buttonA.position(0,0)

buttonB = QPushButton()
buttonB.align("Center")
buttonB.font("Arial")
buttonB.position(0,50)

buttonC = QPushButton()
buttonC.align("Right")
buttonC.font("Arial")
buttonC.position(0,100)






# 함수를 사용해서 위 코드를 좀 더 보기 편하게 줄여보면

def make_button(align, x, y):
    button = QPushButton()
    button.align(align)
    button.font("Arial")
    button.position(x,y)
    return button


buttonA = make_button("Left", 0, 0)
buttonB = make_button("Center", 0, 50)
buttonC = make_button("Right", 0, 100)



### 문자열 실습 ###

# 더하기
## 1
who = "Sup"
category = "Comment"

## 2
title = "Sup Comment"
textA = "OK입니다."
textB = "펍해주세요."


# 곱하기
dot_line = "-"
split_line = dot_line * 20

# 인덱스
mov_path = "X:\\projects\\2023_06_theKillers\\temp\\INJ_0020_edit_v001.mov"
mov_path.index("")

# 인덱스 자르기
today = "20240110"

# 숫자 표현
numA = 9
numB = 7
numC = 4

"%d" % numA
"{}".format(numA)

"%03d" % numA
"{:03d}".format(numA)

# 숫자 올리기
numA = "7"
numA = str(int(numA) + 1)

# 길이
textA = "giantstep"
num = len(textA)


# 일부 문자 존재 여부 확인
textA = "giantstep"

if "step" in textA:
    print("pass")

if not "step" in textA:
    print("pass")

if "Step" in textA:
    print("pass")


# 자르기

textA = "INJ_0010_v001.mov"
textA.split("_")
textA.split(".")
textA.split("v0")
textA.split("00")


# 붙이기

who = "Sup"
category = "Comment"
words = [who, category]

"_".join(words)
" ".join(words)
"/".join(words)


'''
# 실습 예제
아래의 mov_path 경로를 가지고 다음의 요소들을 변수로 등록해보기

project 이름                                    관련항목 : 자르기
shot 이름                                       관련항목 : 자르기
task 이름                                       관련항목 : 자르기
mov_version (숫자 형태 / 문자열 형태 - v000)       관련항목 : 자르기, 숫자 표현
shot 폴더경로                                    관련항목 : 자르기, 인덱스, 인덱스 자르기, 붙이기
task 폴더경로                                    관련항목 : 자르기, 인덱스, 인덱스 자르기, 붙이기
프로젝트를 등록한 년월을 숫자 네자리로 표현 ex) 2306    관련항목 : 자르기, 인덱스 자르기, 붙이기
'''
mov_path = "/projects/2023_06_theKillers/sequence/INJ/INJ_0040/animation/ani01/dev/images/mov/INJ_0040_ani01_v005_w04.mov"
project_name = 
shot_name = 
task_name = 
mov_version_int = 
mov_version_str = 
shot_path =
task_path =
project_registered_date =
