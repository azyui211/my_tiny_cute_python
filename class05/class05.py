
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

class shotgrid_api():
    def __init__(self):
        self.sg = self.get_sg()
        
    def get_sg(self):
        SERVER_PATH = 'https://giantstep.shotgunstudio.com'
        SCRIPT_NAME = 'shotgrid_mov_uploader'
        SCRIPT_KEY  = 'mvmxazyukt&dqgh2lbgBqpyyz'
        sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

        return sg

import shotgun_api3
SERVER_PATH = 'https://giantstep.shotgunstudio.com'
SCRIPT_NAME = 'shotgrid_mov_uploader'
SCRIPT_KEY  = 'mvmxazyukt&dqgh2lbgBqpyyz'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

필터 = []
필드 목록 = []

filt = [["code", "is", "APP_0010"],
        ["project.Project.name", "is", "2023_06_theKillers"] ]
fied = ["sg_cut_in"]
sg.find("Shot", filt, fied)



    


