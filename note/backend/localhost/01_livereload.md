# livereload

輕量級的 localhost，支援熱重載
pip install livereload

## 應用場景
我想他非常適合我，應為我經常手動組裝js, scss, css, html, jinja2，
例如
1. 編寫js 後 將所有js組裝成一個檔案，編譯為min.js，最後重組index.html
2. 編寫scss 後自動編譯為css ，最後重組index.html
3. 編寫jinja2 後自動執行重組index.html
可能還有更多例子，他真是自動化的好幫手



## 避免瀏覽器使用快取
<script src="min.js?v={{ timestamp }}"></script>
<link rel="stylesheet" href="style.css?v={{ timestamp }}">