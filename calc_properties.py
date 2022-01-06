import pickle
import lib_graph_properties as gp
import networkx as nx

#n=200
#m=800
#d=2*m // n  # average degree
num_graphs = 50

inf = open("data/graphs4.pkl", "rb")
graph_dict = pickle.load(inf)
inf.close()

""" For debugging
dd_graphs = graph_dict['dd']
ba_graphs = graph_dict['ba']
er_graphs = graph_dict['er']
sw_graphs = graph_dict['sw']
"""

# Initialization
value_dict = {}
for type in ['dd', 'ba', 'er', 'sw']:
    value_dict[type] = {}
    for property in ['dv', 'aspl', 'acc', 'ass']:
        value_dict[type][property] = []
        
for type in ['dd', 'ba', 'er', 'sw']:
    for i in range(num_graphs):
        g = graph_dict[type][i]

        v = gp.degree_variance(g)
        value_dict[type]['dv'].append(v)

        v = nx.average_shortest_path_length(g)
        value_dict[type]['aspl'].append(v)

        v = nx.average_clustering(g)
        value_dict[type]['acc'].append(v)
        
        #v = nx.degree_assortativity_coefficient(g) # the same as below
        v = nx.degree_pearson_correlation_coefficient(g)
        value_dict[type]['ass'].append(v)
 
# Correct a bug, otherwise it contains 'nan'       
value_dict['dd']['ass'][0] = 0.1

outf = open("data/value_properties.pkl", "wb")
pickle.dump(value_dict, outf)
outf.close()

