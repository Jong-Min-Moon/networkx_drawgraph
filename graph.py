import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

#이렇게 하면 matplotlib의 title axis의 한글이 정상적으로 나옴.
font_name = fm.FontProperties(fname = 'NanumBarunGothic.ttf').get_name()
rc('font', family = font_name)







G1 = nx.Graph()

words_and_weights = pd.read_csv('mytable.csv')
weights = (words_and_weights.weights * 600).astype('int')
weights = pd.concat( [pd.Series([3000]), weights] )
weights = weights.to_numpy()
print(weights)
edges = [('김정은', word) for word in words_and_weights.words]
G1.add_edges_from(edges)# add node/edge pairs

#node attributes
# node_attr = words_and_weights.set_index('words').to_dict('index')
# node_attr['김정은'] = {'weights' : 300}
# nx.set_node_attributes(G1, node_attr)

#position
pos = nx.spring_layout(G1)

# draw the network G1
nx.draw_networkx(G1, pos = pos, node_size = weights, with_labels = False)
nx.draw_networkx_labels(G1, pos, font_family = font_name, font_size=10) #networkx의 node의 라벨은 따로 지정을 해줘야함.

plt.show()