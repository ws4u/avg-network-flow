# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:10:42 2018

@author: WSi
"""

import networkx as nx

def communication_r(input_g):
    """Return the Communication Robustness
	
    This function is specially provided, since calculating node degree is
	quicker	than calculating degree centrality which is normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which CR is to be computed

    Returns
    -------
    CR : float
        The robustness metric CR of G.

    """

    total = 0
    seq = []  # Store the sequence of node removals
    G = input_g.copy()  # Avoid destroying the original graph
    n = G.number_of_nodes()
    for i in range(1, n) :
        node, max_deg = max(G.degree(), key=lambda x: x[1])
        seq.append(node)
        G.remove_node(node)
        for c in nx.connected_components(G):
            j = len(c)
            total += j*(j - 1) 
        CR = total / (n*n*(n-1))
    
    return CR
    #return total, seq   # For debugging purpose

def connection_r(input_g):
    """Return the sum of the remaining edges of all attack rounds
	
    This function is specially provided, since calculating node degree is
	quicker	than calculating degree centrality which is normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed

    Returns
    -------
    R : float
        The robustness metric R of G.

    """

    total = 0
    seq = []  # Store the sequence of node removals
    G = input_g.copy()  # Avoid destroying the original graph
    n = G.number_of_nodes()
    m = G.number_of_edges()
    dview = G.degree()
    for i in range(1, n) :
        node, max_deg = max(G.degree(), key=lambda x: x[1])
        seq.append(node)
        m = m - dview[node]
        total = total + m 
        G.remove_node(node)
    
    return total
    #return total, seq   # For debugging purpose


def metric_r_degree(input_g):
    """Return the metric R with node degree as node importance measure.
	
    This function is specially provided, since calculating node degree is
	quicker	than calculating degree centrality which is normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed

    Returns
    -------
    R : float
        The robustness metric R of G.

    """

    total = 0
    seq = []  # Store the sequence of node removals
    G = input_g.copy()  # Avoid destroying the original graph
    n = G.number_of_nodes()
    for i in range(1, n) :
        node, max_deg = max(G.degree(), key=lambda x: x[1])
        seq.append(node)
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    
    R = total / (n * n)
    return R
    #return total, seq   # For debugging purpose

def metric_r_btwn(G):
    """Return the metric R with betweenness centrality as node importance measure.
	
    This function is specially provided, since betweenness centrality sets 
    endpoints=False by default and is also normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed

    Returns
    -------
    R : float
        The robustness metric R of G.

    """

    total = 0
    seq = []
    n = G.number_of_nodes()
    for i in range(1, n):
        dict=nx.betweenness_centrality(G, normalized=False, endpoints=True)
        node, max_val = max(dict.items(), key=lambda x: x[1])
        seq.append(node)
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    #R = total / (n * n)
    return total, seq


def metric_r(G, centrality_func=None):
    """Return the metric R with given centrality as node importance measure.

    This function allows the flexible use of different centralities to 
	calculate R.
	
    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed
    centrality_func : function
        The function for calculating a centality (e.g., betweenness_centrality)

    Returns
    -------
    R : float
        The robustness metric R of G.

    """
    total = 0
    seq = []
    n = G.number_of_nodes()
    if centrality_func is None:
        centrality_func = nx.degree_centrality
    for i in range(1, n) :
        node, max_cen = max(centrality_func(G).items(), key=lambda x: x[1])
        seq.append(node)
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    R = total / (n * n)
    return R, seq

# The largest component strategy
def metric_r_giant(G, centrality_func=None):
    """Return the R of G by using the centrality of the giant component

    Parameters
    ----------
    G : graph
        The graph for which R is to be computed

    """
    total = 0
    n = G.number_of_nodes()
    if centrality_func is None:
        centrality_func = nx.degree_centrality
    for i in range(1, n) :
        giant = max(nx.connected_component_subgraphs(G), key=len)
        node, max_cen = max(centrality_func(giant).items(), key=lambda x: x[1])
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    R = total / (n * n)
    return R

def isolation_ratio(G):
    """Return the approx vertex cover number / n 
	
    This function is specially provided, since calculating node degree is
	quicker	than calculating degree centrality which is normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed

    Returns
    -------
    R : float
        The robustness metric R of G.

    """

    total = 0
    n = G.number_of_nodes()
    while True:
        node, max_deg = max(G.degree(), key=lambda x: x[1])
        if max_deg > 0:
            G.remove_node(node)
            total += 1
        else:
            break
    return total/n
