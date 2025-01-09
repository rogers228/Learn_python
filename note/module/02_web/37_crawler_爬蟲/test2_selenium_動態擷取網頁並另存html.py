# 安裝模組
# python -m pip install selenium
# python -m pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 動態擷取網頁並另存html
def test1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 僅首次會安裝
    # driver.get("http://www.yeoshe.tw")
    driver.get("http://yshr.asuscomm.com/pdmodel/1q6m1gnc07xE24LLrlcJ")

    html = driver.execute_script("return document.documentElement.outerHTML;") # 依網址取得動態後的網頁html
    soup = BeautifulSoup(html, 'html.parser') # 將html 解析為soup
    with open('temp.html', mode='w', encoding='utf-8') as f: # 另存html 避免多次爬取
        f.write(str(soup))

    print('html is saved')

if __name__ == '__main__':
    test1()