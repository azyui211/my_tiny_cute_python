
# Git 설치
# Git install in M1 Macbook
# eval $(/opt/homebrew/bin/brew shellenv)
# brew install git

# SSH 키 등록
# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# C:\Users\UserName\.ssh\id_rsa.pub

# Git 세팅
# git config --global user.name username
# git config --global user.email user@email.com

import shotgun_api3

SERVER_PATH = 'https://giantstep.shotgunstudio.com'
SCRIPT_NAME = 'shotgrid_mov_uploader'
SCRIPT_KEY  = 'mvmxazyukt&dqgh2lbgBqpyyz'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# 샷그리드 검색 기본형
필터 = []
필드목록 = []
sg.find("", 필터, 필드목록)


# 샷그리드 검색 예제
# Shot 페이지에서 APP_0010 샷의 시작 프레임을 가져오기
filt = [["code", "is", "APP_0010"],
        ["project.Project.name", "is", "2023_06_theKillers"] ]
fied = ["sg_cut_in"]
sg.find("Shot", filt, fied)



    


