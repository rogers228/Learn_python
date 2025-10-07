from git import Repo

def test1():
    repo = Repo(r"C:\Users\user\Documents\Rogers\ispc_maintain") # 注意不同電腦所安裝的位置可能會不同
    print("目前分支:", repo.active_branch)
    print("最新 commit:", repo.head.commit.hexsha)

if __name__ == '__main__':
    test1()
