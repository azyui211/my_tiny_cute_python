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



