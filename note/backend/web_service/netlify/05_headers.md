# headers 檔案

```
_headers 檔案
```
是 Netlify 提供用來設定 HTTP 回應標頭（HTTP Response Headers） 的特殊檔案。只要把這個檔案放在 部署輸出目錄（publish folder，例如 dist / build / public），Netlify 會依內容自動替你的網站設定標頭。


用純文字格式設定 HTTP Headers

控制安全性、快取、CORS、iframe、CSP 等

不需要伺服器程式（因為 Netlify 是靜態主機）

## 禁止 iframe
```py
# 路由
/*
  X-Frame-Options: DENY
```


## CORS 設定
```
/api/*
  Access-Control-Allow-Origin: *
```

## 快取
```py
# index.html 不使用快取 （保持最新 HTML）
/index.html
  Cache-Control: no-cache


# 長時間快取 public(是指 HTTP 回應可以被 CDN / Proxy / 瀏覽器快取)
# 31536000 秒 = 365 天（1 年）
# 表示 這個資源在有效期內絕對不會改變  除非使用者 Ctrl + F5 / 強制重新整理
/assets/*
  Cache-Control: public, max-age=31536000, immutable

```