        try:
            subprocess.run([self.pyapp, script, argv], check=True)
        except:
            sg.popup('執行錯誤!')


list 就是命令