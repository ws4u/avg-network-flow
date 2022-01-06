import pickle
import lib_metric_r as rlib
import lib_robust_metrics as rm
import lib_flow_metrics as flib
import networkx as nx

num_graphs = 50

folder = "data800_2400"
inf = open(folder + "/graphs4.pkl", "rb")
graph_dict = pickle.load(inf)
inf.close()

# Initialization
value_dict = {}
for type in ['dd', 'ba', 'er', 'sw']:
    value_dict[type] = {}
    for metric in ['nodec', 'cf', 'ac', 'natc', 'nst', 'egr', 'sr', 'r', 'anf']:
        value_dict[type][metric] = []
        
for type in ['dd', 'ba', 'er', 'sw']:
    for i in range(num_graphs):
        g = graph_dict[type][i]

        v = nx.node_connectivity(g)
        value_dict[type]['nodec'].append(v)

        v = rm.critical_fraction(g)
        value_dict[type]['cf'].append(v)

        v = nx.algebraic_connectivity(g, method='tracemin_lu')
        value_dict[type]['ac'].append(v)
        
        v = rm.natural_connectivity(g)
        value_dict[type]['natc'].append(v)
 
        v = rm.number_spt(g)
        value_dict[type]['nst'].append(v)

        v = rm.effective_graph_resistance(g)
        value_dict[type]['egr'].append(v)
 
        v = rm.spectral_radius(g)
        value_dict[type]['sr'].append(v)

        v = rlib.metric_r_degree(g)
        value_dict[type]['r'].append(v)
     
        #v = flib.average_network_flow(g)
        v = 3.4
        value_dict[type]['anf'].append(v)


outf = open(folder + "/value_metrics.pkl", "wb")
pickle.dump(value_dict, outf)
outf.close()

