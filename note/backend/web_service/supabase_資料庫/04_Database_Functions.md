# 資料庫函數 Database Functions

這是儲存在 Supabase (PostgreSQL) 內部的程式碼片段（通常使用 PL/pgSQL )語言撰寫）。你可以把它想像成資料庫裡的「小程式」。

運行在dababase裡面，僅能處理資料庫，例如維護特定欄位，版本號更新。

通常由 Database Trigger 觸發事件後 執行 Database Functions
例如新增資料前，處理欄位。
