# supabase Edge_Functions

1. 它是使用js編寫，能夠在supabase上運行。
2. 觸發他執行的方式有2 外部http請求與資料庫事件觸發。
3. 免費用戶也可以使用，雖然有限制但是引響不大。
4. 需要啟動時間，但是比傳統web server啟動得更快。
5. 它會有一個啟動時間，我應該使用異步、或 多線程/多進程方式來避開gui主線程。
6. 雖然不能完全取代 web servers，但是他可以勝任接收API請求、執行運算、交換數據。
7. 直接使用supabase Dashboard 來開發

