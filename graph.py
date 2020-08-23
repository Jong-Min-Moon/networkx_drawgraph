import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

#이렇게 하면 matplotlib의 title axis의 한글이 정상적으로 나옴.
font_name = fm.FontProperties(fname = 'NanumBarunGothic.ttf').get_name()
rc('font', family = font_name)

 

#networkx의 node의 라벨은 따로 지정을 해줘야함.





G1 = nx.Graph()

words_and_weights = pd.read_csv('mytable.csv')
print(words_and_weights)
edges = [('김정은', word) for word in words_and_weights.words]
print(edges)
# add node/edge pairs
G1.add_edges_from(edges)
pos=nx.shell_layout(G1)
# draw the network G1
nx.draw_networkx(G1, pos = pos, with_labels = False)
nx.draw_networkx_labels(G1, pos, font_family = font_name, font_size=10)
plt.show()