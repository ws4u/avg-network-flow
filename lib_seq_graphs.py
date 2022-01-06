# -*- coding: utf-8 -*-
"""
Created on Oct 24 13:10:42 2018

@author: WSi
"""

import networkx as nx
import math
import numpy as np

def generate_graph_list(n, m, num_graphs):  
    """
        Parameters
        ----------
        n: total number of nodes, should be an even number
        m : total number of edges, should be a multiple of n
        num_graphs: total number of connected graphs to generate
            
    """

    # Average node degree
    mean = round(2*m/n)
    # All nodes have the same degree initially
    array = [mean] * n
    graphs=[]
    g=nx.random_degree_sequence_graph(array)
    while not nx.is_connected(g):
        g=nx.random_degree_sequence_graph(array)
    graphs.append(g)

    # Partition nodes into left side and right side;
    # Each side has half_n nodes
    half_n = round(n/2)
    # Available degrees to move from left to right
    avail = m - half_n
    # Number of degrees to move in generating each graph
    moves = math.floor(avail / num_graphs)    
    for i in range(num_graphs - 1):
        for j in range(moves):
            index = np.random.randint(0, half_n)
            # check if it is already degree 1
            while array[index] == 1:
                index = np.random.randint(0, half_n)
            array[index] -= 1

            index = np.random.randint(0, half_n)
            # check if it is already max degree
            while array[index+half_n] == n-1:
                index = np.random.randint(0, half_n)
            array[index+half_n] += 1
        
        # Make sure the sequence is graphical
        while not nx.is_graphical(array):
            k = np.random.randint(0, half_n)
            array[k+half_n] -= 1

            k = np.random.randint(0, half_n)
            # check if it is already max degree
            while array[k+half_n] == n-1:
                k = np.random.randint(0, half_n)
            array[k+half_n] += 1
            
        g=nx.random_degree_sequence_graph(array)
        while not nx.is_connected(g):
            g=nx.random_degree_sequence_graph(array)
        graphs.append(g)

    return graphs

