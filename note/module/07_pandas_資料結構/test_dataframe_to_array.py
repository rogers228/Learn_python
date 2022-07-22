# https://appdividend.com/2022/03/15/how-to-convert-pandas-dataframe-to-list/

# app.py

import pandas as pd

# Creating Dictionary
dict = {
    'series': ['Stranger Things', 'Money Heist', 'House of Cards'],
    'episodes': [25, 40, 45],
    'actors': ['Millie', 'Alvaro', 'Kevin']
}

# Creating Dataframe
df = pd.DataFrame(dict)
print(df)

# get the values
print('---------------------')
print('Use df.values property to get NumPy array')

vals = df.values

print(vals)
# Output
# python3 app.py
#             series  episodes  actors
# 0  Stranger Things        25  Millie
# 1      Money Heist        40  Alvaro
# 2   House of Cards        45   Kevin
# ---------------------
# Use df.values property to get NumPy array
# [['Stranger Things' 25 'Millie']
#  ['Money Heist' 40 'Alvaro']
#  ['House of Cards' 45 'Kevin']]