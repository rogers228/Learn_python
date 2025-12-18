# API 安全代理

## 目標
1. 不暴露後端url, key, token 例如 Supabase URL、 API Key, 自訂 Token
2. 就算暴露url, key，也無法穿透自訂 Token，形成高強度的保護

## 後端 supabase
1. 後端採用 edge functions 作為接收請求，驗證，轉發。
2. 後端通過 urlParams的token 驗證才會轉發真實的url。 自訂驗證超安心。
3. 前端(netlify)與開發端(vite) 的fetch請求會透過後端代理轉發，附上header anonKey 及 urlParams的token 完全不暴露。
4. 前端js代碼僅寫 const proxyUrl = `/api/get_public_pd?pdno=${pdno}`; 完全不暴露。


## edge functions
請參閱 ispc_svelte專案 edge_functions/get_public_pd/index.ts

## vite 代理
請參閱
ispc_svelte/edge_functions/generate_env.py  建立環境變數檔
ispc_svelte/svelte/.env  環境變數
ispc_svelte/svelte/vite.config.js  建立代理

## netlify 代理 (netlify functions)
請參閱 python_green_env 專案
python_green_env/netlify/functions/proxy.js 建立代理
python_green_env/supabase_test/index/tml   測試網頁
