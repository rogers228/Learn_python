# Cloudflare KV

它就是一個全域的 key values，可以急速取值

保護後端：不用每個請求都去問 Supabase 資料庫，節省 API 流量與資料庫負擔。



## 使用
第一步：在 Cloudflare Dashboard 建立 KV 空間
登入 Cloudflare Dashboard。

在左側選單點擊 「Workers & Pages」 > 「KV」。

點擊 「Create a namespace」。

輸入名稱（例如：PORTAL_CACHE），然後點擊 Add。

這時候你就會得到一個 Namespace ID，但我們通常不需要背它。

第二步：將 KV 綁定到你的 Worker (ispc_portal)
這一步是關鍵，它讓你的 Worker 程式碼能透過 env 變數看到這個空間。

做法 A：透過 Dashboard (視覺化)
進入你的 Worker 專案頁面。

切換到 「Settings」 標籤。

找到 「Bindings」 部分，點擊 「Add binding」。

選擇 「KV namespace」。

Variable name：輸入 MY_KV (這就是程式碼裡 env.MY_KV 的由來)。

KV namespace：選擇你剛才建立的 PORTAL_CACHE。

儲存並部署。

做法 B：透過 wrangler.toml (