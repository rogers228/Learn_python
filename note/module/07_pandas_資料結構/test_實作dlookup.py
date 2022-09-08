    def dlookup_gid(self, gid, column):
        # 從 gid 找對應的 column欄位名稱的值value
        result = None
        df = self.df_bom
        if gid in df['gid'].tolist():
            result = df.loc[df['gid']==gid][column].item()

        return result