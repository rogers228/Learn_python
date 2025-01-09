import pandas as pd

bList = [
        ['Rogers',32,'A'],
        ['Allen',5,'A'],
        ['Jessis',28,'B'],
        ['Jay',18,'O'],
        ]

col_s = ['Name','Age','Bud'] #

#create table
df = pd.DataFrame(bList, columns = col_s) # 指定欄標籤名稱

#print(df)
#print(df.head(1))
#print(df.shape)
#print(df.columns)
#print(len(df.index))

for i in range(len(df.index)):
    print(df.iloc[i, 0])


#Filter with index
Ftext = '0,2'
i_list = [int(x) for x in Ftext.split(',')]
#filter_df = df.loc[i_list , : ]
#filter_df = df.loc[i_list , 'Name']
filter_df = df.loc[i_list , ['Name','Bud']]
print(filter_df)

#Filter with value
print('---')
filter_df = df[df['Bud'] == 'A']
print(filter_df)

#是否為Nan
#if pd.isna(m_df.iloc[i, 3]):

