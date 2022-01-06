import pickle
import lib_seq_graphs as sg
import networkx as nx

folder = "data800_2400"
n=800
m=2400
d=2*m // n  # average degree
num_graphs = 50

dd_graphs = sg.generate_graph_list(n, m, num_graphs)
ba_graphs = []
er_graphs = []
sw_graphs = []

for i in range(num_graphs):
    # make sure to generate a connected graph
    while True:
        G=nx.barabasi_albert_graph_my(n, d // 2)
        if nx.is_connected(G):
            break
    ba_graphs.append(G)

    while True:
        G=nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            break
    er_graphs.append(G)

    G=nx.connected_watts_strogatz_graph(n, d, 0.2)
    sw_graphs.append(G)

outf = open(folder + "/graphs4.pkl", "wb")
graph_dict = {'dd': dd_graphs, 'ba': ba_graphs, 'er': er_graphs, 'sw': sw_graphs }
pickle.dump(graph_dict, outf)
outf.close()
