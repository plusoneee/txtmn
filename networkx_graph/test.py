import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import demjson

datas = pd.read_csv('./ptt.csv')
author = datas['author']
pushs = datas['pushs']

# only get id, dont want '(name)'
post_ids = [ author[idx].split(' (')[0] for idx in range(len(author))]
push_ids = []

# put ever push's id of every article  in list
for idx in range(len(pushs[:])):
    ids = []
    for article in demjson.decode(pushs[idx]):
        ids.append(article['push-userid'])
    push_ids.append(ids)

# draw graph
G = nx.Graph()
article_number = len(post_ids)
for index in range(article_number):
    data = [ (post_ids[index],ids) for ids in push_ids[index]]
    G.add_edges_from(data)
nx.draw(G, with_labels=False, node_size=10, font_size=3, node_color='r')
plt.show()
