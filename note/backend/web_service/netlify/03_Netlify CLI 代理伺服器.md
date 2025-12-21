此檔案未經過驗證，已經有更好的替代方案，請參閱 api安全代理

# Netlify CLI 代理伺服器

用來在本地建立一個netlify環境，開發web時可以讀取環境變數(在實際網路netlify中設定的環境變數)

解決如何讓本地的 Svelte 應用程式在呼叫 /admin-api/products-secret 時，
能夠像在 Netlify 上部署一樣安全地注入 Service Key？

讓 Svelte 代碼保持一致，避免暴露金鑰，這樣一來就不會暴露api url，這是最大的好處



## 使用方式

安裝本地 Netlify CLI，在專案下 'npm install -g netlify-cli'
使用vite開發 svelte，但是啟動方式改為 'netlify dev' 就開啟了本地開發伺服器，我的理解正確嗎?



## 設定本地

### 本地環境
建立 .env 檔案（確保它被 .gitignore 忽略）
```
# .env (會被 netlify dev 讀取)
VITE_SUPABASE_URL="https://test"
SUPABASE_KEY="test"

```

### 安裝安裝 Netlify CLI
```
安裝
npm install -g netlify-cli
檢查
netlify --version
```

### 建立本地netlify代理伺服器
建立 public/_redirects
```py
# _redirects (放置在專案根目錄)

# 核心代理配置：將 /api/supabase/* 轉發到 Supabase API
# 並注入隱藏的環境變數 (VITE_SUPABASE_URL 和 SUPABASE_KEY)
/api/supabase/* :VITE_SUPABASE_URL/rest/v1/:splat 200! \
  Authorization=Bearer :SUPABASE_KEY \
  apikey=:SUPABASE_KEY

# SPA 路由 fallback 規則 (必須，讓所有路徑都指向 index.html)
/* /index.html   200
```

建立 netlify.toml 放在跟目錄
```py
# netlify.toml
[dev]
  #指定實際埠號。
  targetPort = 5173 
```

### 執行

```
netlify dev
```
選擇 vite 按 enter 將執行 dev server

### 退出
Ctrl + C 將正確退出，釋放埠號


## 隱藏 API URL 完整範例

### 1.Netlify 環境變數設置 (伺服器端)

netlify > 專案 > Project configuration Environment variables
設定以下 key, value
SUPABASE_URL
SUPABASE_SERVICE_KEY







### 2. 配置重新導向
建立 '_redirects' 通常放在根目錄 本地與雲端皆有作用


```
# _redirects
# ----------------------------------------------------------------------
# 1. Svelte SPA Fallback Rule (確保路由正常運作)
# ----------------------------------------------------------------------
/* /index.html    200

# ----------------------------------------------------------------------
# 2. 安全 API 代理規則 (隱藏真實 URL 與金鑰)
# ----------------------------------------------------------------------
# 來源路徑: /api/admin/products (前端呼叫的乾淨路徑)
# 目標路徑: 透過環境變數組合成的真實 Supabase 查詢 URL
#
# 使用 200 狀態碼進行伺服器端重寫 (反向代理)
# ${SUPABASE_URL} 和 ${SUPABASE_SERVICE_KEY} 會被安全替換。
/api/admin/products    ${SUPABASE_URL}/rest/v1/products?select=*&apikey=${SUPABASE_SERVICE_KEY}    200
```

### 3.前端代碼

```js
async function fetchAdminProducts() {
    try {
        // 核心重點：只呼叫本地的、乾淨的代理路徑
        const response = await fetch('/api/admin/products', {
            method: 'GET',
            // 注意：如果 Supabase 需要，可能需要傳遞 Content-Type
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            // 處理 API 錯誤
            throw new Error(`API request failed with status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Admin Products Data:', data);
        return data;

    } catch (error) {
        console.error('Error fetching admin products:', error);
        // 可以在這裡處理錯誤顯示給用戶
        return [];
    }
}
```

### 4.使用代理伺服器開啟vite
```
netlify dev
```