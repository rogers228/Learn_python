# 安裝模組
# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

# beautifulsoup4_讀取html_bytag_byid_byclass
def test1():
    with open('temp.html', mode='r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser') # 將html 解析為soup
    # print(soup.prettify()) # 觀看結構

    html_head = soup.head # 抓曲tag
    # print(html_head)
    html_body = soup.body # 抓曲tag
    # print(html_body)

    html_1 = soup.find(id="gn_parent_2_spec_2") # byid
    print(html_1)
    # soup.select_one('.stylelistrow') # by_class
    # soup.select('.stylelistrow')

if __name__ == '__main__':
    test1()