# Git 설치

# M1
# val $(/opt/homebrew/bin/brew shellenv)
# brew install git

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