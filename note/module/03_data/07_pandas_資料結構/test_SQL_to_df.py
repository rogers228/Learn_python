class Wpdb(): # 資料庫
    def __init__(self):
        config_conn_MAKE = '''
                    DRIVER={SQL Server};
                    SERVER=220.168.100.250;
                    DATABASE=YEOSHE_MAKE;UID=sa;
                    PWD=dsc80057052'''
        self.cn = pyodbc.connect(config_conn_MAKE) # connect str 連接字串

   def ger_wf_df(self):
        df = pd.read_sql("SELECT * FROM rec_wf ORDER BY wf01", self.cn) #轉pd
        return df