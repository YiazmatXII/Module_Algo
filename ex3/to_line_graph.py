#!/usr/bin/env python3

import matplotlib.pyplot as plt
import networkx as nx
import random

def to_line_graph(edges, nodes):
    lene = len(edges)
    LG = nx.Graph()
    for edge in edges:
        LG.add_node(edge)
        #v3
        for nod in LG.nodes:
            if (edge[0] in nod or edge[1] in nod) and nod != edge:
                LG.add_edge(nod, edge)
    return LG
