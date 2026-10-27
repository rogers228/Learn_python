# sveltekit 的資料取得


pywebview 桌面應用 的 sveltekit 不使用 +page.js, +page.server.js
直接使用 onMount window.pywebview.api


```html
<script>
    import { onMount } from 'svelte';

    // 1. 使用 Svelte 5 的 $state 宣告響應式狀態
    let tableData = $state([]);
    let isLoading = $state(true);
    let errorMessage = $state('');

    // 2. 當頁面掛載（Mount）完成後向 Python 請求資料
    onMount(async () => {
        try {
            // 確保 pywebview 已經準備好，再呼叫 Python API
            await waitForPywebview();
            
            // 直接透過 pywebview 橋樑呼叫 Python 端函數拿到 Pandas 轉好的 records JSON
            tableData = await window.pywebview.api.get_sales_data();
        } catch (error) {
            console.error("載入資料失敗:", error);
            errorMessage = "無法取得後端數據";
        } finally {
            isLoading = false;
        }
    });

    // 輔助函數：等待 pywebview API 載入完成
    function waitForPywebview() {
        return new Promise((resolve) => {
            if (window.pywebview && window.pywebview.api) {
                resolve();
            } else {
                window.addEventListener('pywebviewready', resolve, { once: true });
            }
        });
    }
</script>

<div class="p-6">
    <h1 class="text-2xl font-bold mb-4">銷售數據報表</h1>

    {#if isLoading}
        <p class="text-gray-500">正在從 Pandas 載入數據...</p>
    {:else if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
    {:else}
        <!-- 渲染表格 -->
        <div class="border rounded-lg overflow-hidden">
            <table class="w-full text-left border-collapse">
                <thead>
                        <th class="p-3">訂單編號</th>
                    <tr class="bg-gray-100 border-b">
                        <th class="p-3">客戶名稱</th>
                        <th class="p-3">金額</th>
                    </tr>
                </thead>
                <tbody>
                    {#each tableData as row}
                        <tr class="border-b hover:bg-gray-50">
                            <td class="p-3">{row.id}</td>
                            <td class="p-3">{row.customer}</td>
                            <td class="p-3">{row.amount}</td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    {/if}
</div>

```