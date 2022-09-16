# -*- coding: utf-8 -*-

import networkx as nx
import itertools

def network_flow_betweenness_centrality(
        G, normalized=True, weight='capacity'):
    
    betweenness = dict.fromkeys(G, 0.0)  # b[v]=0 for v in G
    for s in G:
        node_list = list(g.nodes())
        node_list.remove(s)
        for u,v in itertools.combinations(node_list,2):
            flow_value, flow_dict = nx.maximum_flow(G, u, v, capacity= weight)
            for nb in G[s]:
                betweenness[s] += flow_dict[s][nb]
     
    return betweenness
   
#g=nx.complete_graph(10)
g=nx.cycle_graph(6)
attr = {(u, v): {"capacity": u+v} for (u, v) in g.edges()}
nx.set_edge_attributes(g, attr)
cfb = nx.current_flow_betweenness_centrality(g, weight="capacity")  
nfb = network_flow_betweenness_centrality(g, weight="capacity")  

print(cfb)
print(nfb)
