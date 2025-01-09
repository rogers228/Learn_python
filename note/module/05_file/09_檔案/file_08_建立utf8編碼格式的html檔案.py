import os
import codecs
currdir = os.getcwd() #當前路徑
file = 'test.html' #檔名
fullpath = currdir + '\\' + file
html = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset = "big5">
        <meta name = "keywords" content = "yeoshe,pump">
        <script type = 'text/javascript' src = 'atm.js'></script>
        <script>mycss();</script>
        <title>%s</title>
    </head>
    <body>
        <a href="index.html" target="_self" title="Yeoshe MMS">Yeoshe MMS</a>
        <p>
        網頁產生時間:123
        <h1>
            <center>test</center>
        </h1>
        <table class='table'>
            <thead>
                <td>機台</td>
                <td>工程</td>
                <td>實做/應做/效能</td>
                <td>實際起~迄/工時</td>
                <td>下個準備</td>
            </thead>
            <tbody>
            </tbody>
        </table>
    </body>
</html>'''
with codecs.open(fullpath, "w", "utf-8-sig") as temp:
    temp.write(html)
print('finish')
