# -*- coding:utf-8 -*-

import os
def addFunc(seq):
    result = os.listdir("/projects/sequence/" + seq)
    
    return result

shot_list = addFunc("EDU")


# 가방의 내용물을 보는 함수
def show_items_in_a_bag(inputA):
    for item in my_bag:
        print(item)
        return res

my_bag = ["지갑", "노트", "펜", "우산"]
res = show_items_in_a_bag(my_bag)     # 실행

# 우산이 있으면 사용하는 함수
def take_an_umbrella(weather, someones_bag):
    if weather == "rainy":
        if "우산" in someones_bag:
            print("우산을 꺼냅니다.")
            return "우산"
        else:
            print("비를 맞습니다.")
            return None
    else:
        print("비가 오지 않습니다.")
        return None
take_an_umbrella("rainy", my_bag)

# 구구단 함수
def multiplication(input_number):
    for i in range(9):
        num = i + 1
        print(str(input_number) + " x " + str(num) + " = " + str(input_number*num))

multiplication(3)

pathA = "/projects/sequences/fileA.pdf"
        
import os
os.listdir("/projects")
os.makedirs("/projects/sequences")
os.path.splitext(pathA)[1]

pathA = "/projects/folder"


def replaceExt(pathA, ext, target_ext):
    for file_name in os.listdir(pathA):
        if os.path.splitext(file_name)[1] == ext:
            original_file = pathA + "/" + file_name
            target_file = pathA + "/" + file_name.replace(ext, target_ext)
            os.rename(original_file, target_file)
            
replaceExt("/projects/", ".jpg", ".png")
replaceExt("/projects/A/", ".mp4", ".mov")
os.rename("/projects/fileA.pdf", "/projects/fileB.jpg")
