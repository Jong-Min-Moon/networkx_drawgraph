import pandas as pd

table = pd.DataFrame()

words = ['강아지', '고양이', '토끼', '거북이', '호랑이']
words = [word + str(i) for word in words for i in range(10)]

weights = [0.1, 0.2, 0.3, 0.4, 0.5] * 10
sentiment = [-0.1, -0.2, -0.3, -0.4, -0.5, 0, 0.1, 0.2, 0.3, 0.4] * 5
table['words'] = words
table['weights'] = weights
table['sentiment'] = sentiment

print(table)
table.to_csv('mytable.csv', index = False)