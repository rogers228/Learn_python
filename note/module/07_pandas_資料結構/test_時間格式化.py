        df_g = df_w.copy()   # 要先複製 再修改格式 才不會報錯提示

        df_g['日期'] =  pd.to_datetime(df_g['日期'], format='Y-%m-%d') # 時間格式化  轉時間

        df_g['日期'] = df_g['日期'].dt.strftime('%Y-%m-%d')  #格式化後 再轉回文字  避免後續轉換 格式又跑掉





last_date = df_w["日期"].max().to_period('D') #時間戳 轉 日期