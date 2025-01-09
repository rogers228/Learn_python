#https://stackoverflow.com/questions/28986489/how-to-replace-text-in-a-string-column-of-a-pandas-dataframe
df['range'] = df['range'].str.replace(',','-')