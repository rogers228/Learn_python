# PL/pgSQL

簡單來說它就是可程式化的SQL

1. 它不只是SQL，添加了可程式化的語法
2. 它是可以執行在資料庫內部執行
3. PL/pgSQL 主要用於創建兩種資料庫物件 函數 (Functions) 觸發器函數 (Trigger Functions)



## 尋找 Functions

supabase dashboard 左側導航 > database > functions / Triggers

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