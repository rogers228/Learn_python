if True:
    import sys, os
    import subprocess

    sys.path.append(os.getenv('GRST_PATH'))
    from global_config import OPTION, current_base_path

def deploy_css():
    print(f"🚀 開始部署css")
    # 呼叫核心 deploy.py
    script = os.path.join(current_base_path(), 'ispc_portal', 'script', 'deploy.py')

    # ✨ 核心修正：強制設定環境變數 PYTHONIOENCODING 為 utf-8
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    cmd = [sys.executable, script, "--id", "specic_css"]

    try:
        # 傳入 env 參數
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            env=env,       # 指定環境變數
            encoding="utf-8" # 確保讀取 stdout 時也用 utf-8
        )

        print(f"✅ 部署成功！\n輸出內容:\n{result.stdout}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ 部署失敗！錯誤碼: {e.returncode}")
        # e.stderr 也需要確保正確顯示
        print(f"錯誤訊息: {e.stderr}")
        return False

if __name__ == '__main__':
    deploy_css()