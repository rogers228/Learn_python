import os
from git import Repo

def test1():
    TARGET_DIR = os.path.join(os.environ["USERPROFILE"], "Documents", "ispc_maintain")
    repo = Repo(TARGET_DIR) # 注意不同電腦所安裝的位置可能會不同
    print("目前分支:", repo.active_branch)
    print("最新 commit:", repo.head.commit.hexsha)

if __name__ == '__main__':
    test1()
