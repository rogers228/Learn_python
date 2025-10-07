from git import Repo

def check_repo_needs_pull(repo_path="."):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    origin.fetch() # 取得最新遠端狀態

    local_commit = repo.head.commit                             # 本地分支的最後一次提交。
    remote_commit = origin.refs[repo.active_branch.name].commit # 遠端分支的最後一次提交。

    if local_commit.hexsha == remote_commit.hexsha:
        print("✅ 本地版本已是最新，不需要 pull。")
    else:
        print("⚠️ 有新的提交可用，建議執行 git pull。")


def update_repo(repo_path="."):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    # 先抓取遠端最新資料
    print("🔍 檢查遠端更新...")
    origin.fetch()

    local_commit = repo.head.commit
    remote_commit = origin.refs[repo.active_branch.name].commit

    if local_commit.hexsha == remote_commit.hexsha:
        print("✅ 已是最新版本，無需更新。")
    else:
        print("⚠️ 偵測到遠端有新版本，開始執行 git pull...")
        try:
            origin.pull()
            print("✅ 更新完成！")
        except GitCommandError as e:
            print("❌ 更新失敗：", e)


def test1():
    check_repo_needs_pull(r"C:\Users\user\Documents\Rogers\ispc_maintain")  # 注意不同電腦所安裝的位置可能會不同

def test2():
    update_repo(r"C:\Users\user\Documents\Rogers\ispc_maintain")  # 注意不同電腦所安裝的位置可能會不同


if __name__ == "__main__":
    test2()
