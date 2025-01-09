# https://neutron0916.medium.com/python-eel-%E5%89%B5%E9%80%A0%E5%80%8B%E4%BA%BA%E7%B6%B2%E9%A0%81gui%E6%A1%8C%E9%9D%A2%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F-%E5%85%A5%E9%96%80%E7%AF%87-2500b38ed070

import eel

# 這裡寫上你要的function
count =0

@eel.expose #用decorator的方式，將JS要呼叫的PY function暴露給eel, 讓eel當作一個library  去給JS使用
def say_something(word):      
    global count 
    count = count +1
    #返回 字串加上被呼叫的次數     
    return f'JS call Python script and return {word}, and this was be called {count} times'


eel.init('web') # eel.init(網頁的資料夾)
eel.start('main.html',size = (600,400)) #eel.start(html名稱, size=(起始大小))


# cmd 執行
# cd /d C:\Users\user\Documents\Rogers\python_lee_test
# python app.py