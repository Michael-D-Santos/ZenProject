import matplotlib.pyplot as plt
import networkx as nx

# list of tuples go here
edges = []

# create empty graph
G = nx.Graph()

# add edges to the graph
for edge in edges:
    G.add_edge(edge[0][0], edge[0][1], weight=edge[1])

# use the circular layout for the graph
pos = nx.circular_layout(G)

# draw the graph
nx.draw(G, pos, edge_color="red", with_labels=True)

# show the plot
plt.show()
