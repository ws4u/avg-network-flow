# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:20:30 2018

@author: 30033237
"""

import networkx as nx
import matplotlib.pyplot as plt

g = nx.gnm_random_graph(100, 400)
graph_pos = nx.random_layout(g)

#g = nx.barabasi_albert_graph_my(100, 4)
#graph_pos = nx.spring_layout(g)

#g= nx.watts_strogatz_graph(100, 4, 0.3)
#graph_pos = nx.circular_layout(g)

plt.figure(figsize=(18,18))
#nx.draw_networkx_nodes(g, graph_pos, node_size=10, node_color='blue', alpha=0.3)
nx.draw_networkx_nodes(g, graph_pos, node_color='blue')
nx.draw_networkx_edges(g, graph_pos)
#nx.draw_networkx_labels(g, graph_pos, font_size=8, font_family='sans-serif')
plt.savefig("topology_er.png")
plt.show()
