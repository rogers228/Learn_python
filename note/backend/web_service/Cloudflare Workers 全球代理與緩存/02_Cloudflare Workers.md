什麼是 Cloudflare Workers(CFW)？

它是一種 Serverless（無伺服器） 運算服務。它不跑在某台固定的主機上，而是直接跑在 Cloudflare 全球數百個資料中心（邊緣節點）上。

當使用者請求圖片時，程式碼會在離使用者最近的地點執行，反應速度極快。



A. 隱藏後端 URL
使用者的瀏覽器只會看到 https://img.yourdomain.com/photo.jpg，完全不知道背後是存在 Supabase。

B. 節省 Supabase 5GB 流量 (最重要的理由)
Supabase 免費版每月只有 5GB 流量。

直接連線：圖片被看 10 次，Supabase 就計費（扣流量）10 次。

透過 Worker：Worker 可以開啟 Cache（快取） 功能。圖片第一次被讀取後，會存在 Cloudflare 的節點裡。接下來的 9 次請求都由 Cloudflare 直接出貨，完全不消耗 Supabase 的流量。

C. 動態處理圖片
你可以在 Worker 裡面寫幾行 JavaScript，自動把上傳的圖片轉成體積更小的 WebP 格式，或者根據使用者裝置自動縮放大小。

D. 免費額度慷慨
Cloudflare Workers 的免費版每天提供 10 萬次請求，這對於個人專案來說幾乎是用不完的。


Supabase + Cloudflare Worker 的組合就是一個完美的「全類型檔案圖床與緩存方案」


# 網址
https://www.cloudflare.com/

使用 