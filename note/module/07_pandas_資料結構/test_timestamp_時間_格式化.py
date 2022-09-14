    def get_sy002(self): #顯示日期
        # ma004 部門id
        s = "SELECT sy002 FROM rec_sy WHERE sy001=1"
        df = pd.read_sql(s, self.cn) #轉pd
        return df.iloc[0]['sy002'].strftime('%Y-%m-%d') if len(df.index) > 0 else ''