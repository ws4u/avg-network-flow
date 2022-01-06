import networkx as nx
import math
import numpy as np
import numpy.linalg as la
from networkx.exception import NetworkXError

# the following metrics are directly available
#nx.estrada_index(G)
#nx.algebraic_connectivity(G, method='tracemin_lu')

def critical_fraction(G):
    degs = [d for n, d in G.degree()]
    degs_square = [d*d for d in degs]

    ratio=(sum(degs_square)/sum(degs))
    cf = 1-(1/(ratio-1))
    
    return cf

def get_matrix_minor(arr,i,j):
    # ith row, jth column removed
    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1,arr.shape[1])))]


# Negligibly quicker than the number_spt_eigen() below
def number_spt(G):
    """Return the number of spanning trees.
	
    Parameters
    ----------
    G : Graph
        The graph for which the number of spanning trees is to be computed

    Returns
    -------
    num : integer
        The number of spanning trees in G.

    """
    m = nx.laplacian_matrix(G)
    arr = m.toarray()
    minor = get_matrix_minor(arr, 1, 1)
    # Calculating the determinant of the minor
    #num = round(la.det(minor))
    num = la.det(minor)
    return num


def number_spt_eigen(G):
    n=G.number_of_nodes()
    spec=nx.laplacian_spectrum(G)
    product=1
    for i in range(1, n):
        product *= spec[i]

    return product/n


def number_spt_eigen_log(G):
    n=G.number_of_nodes()
    spec=nx.laplacian_spectrum(G)
    sum=0
    for i in range(1, n):
        sum += math.log(spec[i])

    return sum


def effective_graph_resistance(G):
    n=G.number_of_nodes()
    spec=nx.laplacian_spectrum(G)
    sum=0
    for i in range(1, n):
        sum += 1/spec[i]

    # Return the inverse to make it positively correlated with robustness
    return 1/(sum*n)


def spectral_radius(G):
    eigens=nx.adjacency_spectrum(G)
    sr=max(eigens)
    # Return the inverse to make it positively correlated with robustness
    return 1/sr.real


def natural_connectivity(G):
    n=G.number_of_nodes()
    ei = nx.estrada_index(G)
    nc = np.log(ei/n)
    return nc