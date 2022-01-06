import networkx as nx
import numpy as np
import itertools

"""
from networkx.algorithms.flow import build_residual_network
from networkx.algorithms.connectivity import local_edge_connectivity
from networkx.algorithms.connectivity.utils import build_auxiliary_edge_connectivity

# Is below the same as average flow?
def average_edge_connectivity(G, flow_func=None):
    #Returns the average edge connectivity of a graph G.

    if G.is_directed():
        iter_func = itertools.permutations
    else:
        iter_func = itertools.combinations

    # Reuse the auxiliary digraph and the residual network
    H = build_auxiliary_edge_connectivity(G)
    R = build_residual_network(H, 'capacity')
    kwargs = dict(flow_func=flow_func, auxiliary=H, residual=R)

    num, den = 0, 0
    for u, v in iter_func(G, 2):
        num += local_edge_connectivity(G, u, v, **kwargs)
        den += 1

    if den == 0:  # Null Graph
        return 0
    return num / den

"""

# Time consuming by calling maximum_flow() for each pair of nodes
def total_flow_naive(G):
    """
    Return the total flow of all node pairs in G.
    --- Parameters ---
    G : the graph for which total flow is to be computed
    """

    nx.set_edge_attributes(G, 1, 'capacity')
    total=0
    for u,v in itertools.combinations(G,2):
        flow_value, flow_dict = nx.maximum_flow(G, u, v)
        total+=flow_value
    return total


def min_edge_weight_in_shortest_path(T, u, v):
    path = nx.shortest_path(T, u, v, weight='weight')
    return min((T[u][v]['weight'], (u,v)) for (u, v) in zip(path, path[1:]))


# Time consuming by calling shortest_path() for each pair of nodes
def total_flow_GH_naive(G):

    nx.set_edge_attributes(G, 1, 'capacity')
    T=nx.gomory_hu_tree(G)

    total=0
    n=G.number_of_nodes()
    for i in range(n-1):
        for j in range(i+1,n):
            maxflow, edge=min_edge_weight_in_shortest_path(T, i, j)
            total=total+maxflow
    return total


# Efficient by being integrated with DFS
def average_network_flow(G):

    nx.set_edge_attributes(G, 1, 'capacity')
    T=nx.gomory_hu_tree(G)

    n=G.number_of_nodes()
    # Initialize a 2D flow array to store the calculation results
    flow_array=np.zeros((n,n))

    def single_source_flow(T, parent, current):
        nonlocal flow_array
        # source node
        nonlocal source
        
        # loop through the neighbor nodes of the current node
        for nbr in T[current]:
            # skip the neighbor which is the parent 
            if nbr==parent:
                continue
            
            # decide flow_array[source][nbr]
            if current==source:
                flow_array[source][nbr] = T[source][nbr]['weight']
            elif T[current][nbr]['weight'] < flow_array[source][current]:
                flow_array[source][nbr] = T[current][nbr]['weight']
            else:
                flow_array[source][nbr] = flow_array[source][current]
            
            # DFS visit next node
            single_source_flow(T, current, nbr)
        
    # using each node in T as a source node
    for source in T:
        single_source_flow(T, -1, source)
        
    total=0
    for i in range(n-1):
        for j in range(i+1,n):
            total+=flow_array[i][j]
    avg = 2*total/n/(n-1)
    
    return avg

"""
# Testing
g=nx.gnm_random_graph(10,30)
n=g.number_of_nodes()
tfn=total_flow_GH_naive(g)
tf=total_flow_GH_DFS(g)
print("Naive:", tfn, " Efficient:", tf)
#con_n=nx.average_node_connectivity(g) * n * (n-1) / 2
#con_e=average_edge_connectivity(g) * n * (n-1) / 2
#print("tf:", tf, "con_e:", con_e)
#print("con_e - con_n =", con_e - con_n)
"""