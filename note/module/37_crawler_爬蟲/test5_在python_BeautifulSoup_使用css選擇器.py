# 在python BeautifulSoup 使用css選擇器

    def querySelectorAll(self, queryStr):
        with open(self.all_html, mode='r', encoding='utf-8') as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html.parser') # 將html 解析為soup
        result_list = soup.select(queryStr)
        return result_list

    def querySelectorOne(self, queryStr):
        with open(self.all_html, mode='r', encoding='utf-8') as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html.parser') # 將html 解析為soup
        result_list = soup.select_one(queryStr)
        return result_list

    def list2Str(self, soup_list):
        paragraphs = []
        for e in soup_list:
            paragraphs.append(str(e))
        result = '\n'.join(paragraphs)
        result = BeautifulSoup(result, 'html.parser').prettify() # 將html 解析為soup
        return result # string


def test2_tour():
    ss = Csr2ssr()
    html = ss.list2Str(ss.querySelectorOne('div#tour1'))
    print(html)