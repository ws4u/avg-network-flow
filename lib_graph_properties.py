import networkx as nx
import numpy as np

def degree_variance(G):
    degree_sequence = [d for n, d in G.degree()]
    return np.var(degree_sequence)
