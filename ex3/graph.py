#!/usr/bin/env python3

import matplotlib.pyplot as plt
import networkx as nx
import random
from to_line_graph import to_line_graph

def graph():
  nodes = 60
  edges = 130
  G = nx.generators.random_graphs.gnm_random_graph(nodes, edges)
  nx.draw_networkx(G)
  plt.title("random sparse graph")
  plt.tight_layout()
  plt.axis('off')
  graph_name = "random_sparse_graph"
  plt.savefig(graph_name+".pdf")
  plt.close()

  LG = to_line_graph(list(G.edges), list(G.nodes))
  nx.draw_networkx(LG, font_size=5)
  plt.title("line graph")
  plt.tight_layout()
  plt.axis('off')
  graph_name = "line_graph"
  plt.savefig(graph_name+".pdf")
  plt.close()
