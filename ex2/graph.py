#!/usr/bin/env python3

import matplotlib.pyplot as plt
import networkx as nx
import random

nodes = 60

def draw(G, graph_colors):
    nx.draw_networkx(G, node_color=graph_colors)
    plt.title("graph ex2")
    plt.tight_layout()
    plt.axis('off')
    plt.savefig("graph_ex2.png")
    plt.close()

def get_color(nodeDict, n):
    if nodeDict[n] == {}:
        return ""
    return nodeDict[n]

def get_possible_color(color_neighbors, colors):
    possible_colors = list(set(colors) - set(color_neighbors))
    possible_colors.sort(reverse=True)
    return possible_colors[0]

def coloring_algorythm(G, colors):
    nodeDict = dict(G.nodes(data=True))
    i = 0
    graph_colors = []
    color_neighbors = []
    while i < nodes:
        for n in G.neighbors(i):
            color_neighbors.append(get_color(nodeDict, n))
        actual_color = get_possible_color(color_neighbors, colors)
        nodeDict[i] = actual_color
        graph_colors.append(actual_color)
        color_neighbors = []
        i = i + 1
    return graph_colors

def graph():
  edges = 130
  G = nx.generators.random_graphs.gnm_random_graph(nodes, edges)
  colors = ["gray", "red", "gold", "yellow", "blue", "green", "orange", "black", "white"]
  graph_colors = coloring_algorythm(G, colors)
  draw(G, graph_colors)
