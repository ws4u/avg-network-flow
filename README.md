# avg-network-flow
Average Network Flow (ANF) is defined as the average of the maximum network flows among all pairs of nodes in a network. It's proposed as a network robustness metric in our paper "Measuring Network Robustness by Average Network Flow". The paper can be found at https://arxiv.org/abs/2012.00877.

This repository contains our implementation of ANF by leveraging Gomory-Hu trees. The implementations of some other robustness metrics compared in our paper are also included. Our implementation is based on NetworkX (https://networkx.org/), a Python package for analyzing Complex Networks.

The basic usage of our Python files is:
1. Run gen_four_graphs.py
2. Run calc_metrics.py and calc_properties.py
