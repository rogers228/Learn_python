
'''
網路爬蟲學習
'''

def main():
    examp_5()

def examp_5():
    #https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import re
    myurl = "https://news.tvbs.com.tw/"
    html = urlopen(myurl).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)
    for link in soup.find_all('a'):
        print(link.get('href'))

def examp_4():
    #使用BeautifulSoup + re 可抓取複雜的鏈結
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import re
    myurl = "https://morvanzhou.github.io/static/scraping/table.html"
    html = urlopen(myurl).read().decode('utf-8')
    print(html)
    soup = BeautifulSoup(html, features='html.parser') 
    img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')}) #抓取img tag 中 src符合正則的字串
    for link in img_links:
        print(link['src'])
    course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')}) #抓取a tag 中 href符合正則的連接字串
    for link in course_links:
        print(link['href'])
    print("\nexamp_4")

def examp_3():
    #使用BeautifulSoup抓取css
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    myurl = "https://morvanzhou.github.io/static/scraping/list.html"
    html = urlopen(myurl).read().decode('utf-8')
    #print(html)
    soup = BeautifulSoup(html, features='html.parser') 
    month = soup.find_all('li', {"class": "month"}) #抓取li標籤 中 class = month的資訊
    for m in month:
        #print(m)
        print(m.get_text())

    #多重查找
    jan = soup.find('ul', {"class": 'jan'}) #先找 class:jan 的所屬tag 元素
    #print(jan)
    d_jan = jan.find_all('li')              #從jan 的所屬tag 元素 裡面找li tag
    for d in d_jan:
        print(d.get_text())
def examp_2(): 
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    #使用BeautifulSoup抓取tag標籤
    myurl = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
    html = urlopen(myurl).read().decode('utf-8') #擷取網頁原始碼
    #print(html)
    #soup = BeautifulSoup(html, features='lxml')
    soup = BeautifulSoup(html, features='html.parser')
    print(soup.h1)
    print('\n', soup.p)
    all_href = soup.find_all('a')
    all_href = [l['href'] for l in all_href]
    print('\n', all_href)
    print('\nexamp_2 ok')
def examp_1():
    #簡易爬蟲
    import re
    myurl="https://morvanzhou.github.io/static/scraping/basic-structure.html"
    html = urlopen(myurl).read().decode('utf-8') #擷取網頁原始碼
    print(html)
    print('examp ok')

    res = re.findall(r"<title>(.+?)</title>", html) #正則擷取 標題
    print("\nPage title is: ", res[0])

    res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
    print("\nPage paragraph is: ", res[0])

    res = re.findall(r'href="(.*?)"', html)
    print("\nAll links: ", res)
if __name__ == "__main__":
    main()