# 如何在supabase web 來設定 RLS?

1. 進入 supabase > 左側選單 table editer > 選擇table > 右上方 Add RLS policy
2. 進入 RLS 頁面 > 右側 create policy
3. 選擇右側 的動作



讓結果如下

任何人只要拿到 anon key 就可以讀、寫、刪所有資料

不適合存敏感資料


## 允許讀取
CREATE POLICY "allow anon select all"
ON public.rec_bookmarks
FOR SELECT
TO anon
USING (true);

## 允許新增讀取
CREATE POLICY "allow anon insert all"
ON public.rec_bookmarks
FOR INSERT
TO anon
WITH CHECK (true);

## 允許更新
CREATE POLICY "allow anon update all"
ON public.rec_bookmarks
FOR UPDATE
TO anon
USING (true)
WITH CHECK (true);

## 允許刪除
CREATE POLICY "allow anon delete all"
ON public.rec_bookmarks
FOR DELETE
TO anon
USING (true);

