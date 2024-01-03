# -*- coding:utf-8 -*-

import os
import shutil

os.path.exists("경로")
# 입력한 "경로"가 실제로 존재하면 True, 아니면 False 반환

os.path.isfile("경로")
# 입력한 "경로"가 파일이면 True, 아니면 False 반환

os.path.isdir("경로")
# 입력한 "경로"가 폴더면 True, 아니면 False 반환

os.path.dirname("경로")
# 입력한 "경로"의 한 단계 상위 폴더 경로를 반환
# ex) os.path.dirname("/projects/testA/fileA.py")
#      --> "/projects/testA"
#      os.path.dirname("/projects/testA")
#      --> "/projects"

# 파일 복사
shutil.copy2("/pathA/fileA.pdf", "/pathB/sub/fileB.pdf")
# 폴더 복사
shutil.copytree("/pathA/subA", "/pathB/")

pathA = "/home/seokwon.choi/mySrc"
os.listdir(pathA)


중국집A = 중국집()
중국집A.면만드는함수()


class 중국집B():
    def __init__(self):
        None

class 중국집(중국집B):
    def __init__(self):
        self.사장님 = ""
        self.위치 = ""
        전화번호 = ""
        
    def 면만드는함수(self, 밀가루, 물):
        면 = 밀가루 + 물
        return 면

    def 육수만드는함수(self, 물, 재료):
        육수 = 물 + 재료
        return 육수
        
        

