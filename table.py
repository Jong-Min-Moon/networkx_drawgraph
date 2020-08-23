import pandas as pd

table = pd.DataFrame()

words = ['강아지', '고양이', '토끼', '거북이', '호랑이']
weights = [0.2, 0.3, 0.4, 0.5, 0.3]

table['words'] = words
table['weights'] = weights

table.to_csv('mytable.csv', index = False)