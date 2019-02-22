import networkx as nx
import matplotlib.pyplot as plt


author = ''

#  Create an empty graph with no nodes and no edges.
G = nx.Graph()

# G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2, edge_color='r')
# adds node "spam"
G.add_node("spam", node_color='b',)        
# adds 4 nodes: 's', 'p', 'a', 'm'
G.add_nodes_from("spam") 
# add edge from 's' to 'm' 
G.add_edge('s', 'm')
print(G['m'])
nx.draw(G, with_labels=True)

plt.axis('off')
plt.show() # display