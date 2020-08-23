import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
#이렇게 하면 matplotlib의 title axis의 한글이 정상적으로 나옴.
font_name = fm.FontProperties(fname = 'NanumBarunGothic.ttf').get_name()
rc('font', family = font_name)







G1 = nx.Graph()



words = pd.read_csv('mytable.csv')

edges = [('김정은', word) for word in words.words]
G1.add_edges_from(edges)# add node/edge pairs

scaler = MinMaxScaler()
weights = words.weights.to_numpy()
weights = scaler.fit_transform(weights.reshape(-1,1))
weights = weights.flatten()
weights = (2000 * weights + 500).astype('int')
weights= np.insert(weights, 0, 3200)
print(weights)

scaler = MaxAbsScaler()
sentiment = words.sentiment.to_numpy()
sentiment = scaler.fit_transform(sentiment.reshape(-1,1))
sentiment = sentiment.flatten()
sentiment= np.insert(sentiment, 0, 0)
sentiment = -1 * sentiment
print(sentiment)


#node attributes
# node_attr = words_and_weights.set_index('words').to_dict('index')
# node_attr['김정은'] = {'weights' : 300}
# nx.set_node_attributes(G1, node_attr)

#position
pos = nx.spring_layout(G1)

# draw the network G1
nx.draw_networkx(G1, pos = pos, node_size = weights, node_color = sentiment, with_labels = False, cmap = plt.cm.get_cmap('coolwarm'))
nx.draw_networkx_labels(G1, pos, font_family = font_name, font_size=11) #networkx의 node의 라벨은 따로 지정을 해줘야함.

plt.show()