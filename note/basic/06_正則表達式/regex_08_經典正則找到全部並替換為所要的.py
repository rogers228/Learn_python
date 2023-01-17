# 經典正則找到全部並替換為所要的


    def img_gh(self, source):
        # 去除 img tag的封閉斜線符號 /
        # BeautifulSoup 爬取網頁時 會自動補上封閉符號避免出錯，但卻不符合html5規範
        # print(source)

        pattern = re.compile(r"\s*<img(.*)\/>") # 正則 頭到尾及括號
        lis_find = re.findall(pattern, source) # 找到 括號內
        # for e in lis_find:
            # print(e)
        lis_group = [e.group() for e in re.finditer(pattern, source)] # 找到 頭尾含括號
        # for e in lis_group:
            # print(e)
        new_str = source
        for find_in, group in zip(lis_find, lis_group): # 逐一取代
            # print(file, str_replace )
            new_str = new_str.replace(group, f' <img{find_in}>')
        # print(new_str)
        return new_str