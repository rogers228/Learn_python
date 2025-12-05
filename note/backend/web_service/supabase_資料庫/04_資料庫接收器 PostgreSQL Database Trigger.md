# 資料庫接收器 PostgreSQL Database Trigger

1. 資料庫事件，可設定 INSERT, UPDATE, DELETE 動作來觸發執行 edge functions
2. 使用 supabase dashboard SQL Edit 來建立或查詢

PostgreSQL 資料庫本身不能發出 HTTP 請求到外部網路。它必須透過 pg_notify 通知 Supabase 的 Realtime Service，由 Realtime Service 扮演中間人的角色，將通知轉換成您 Edge Function 可以接收的 Webhook (HTTP 請求)。



## 尋找觸發器
```
SELECT
    t.tgname AS trigger_name,
    c.relname AS table_name,
    pg_get_triggerdef(t.oid) AS definition
FROM
    pg_trigger t
JOIN
    pg_class c ON t.tgrelid = c.oid
WHERE
    c.relname = 'rec_pd' -- 鎖定您的目標表格
    AND t.tgisinternal = FALSE;
```