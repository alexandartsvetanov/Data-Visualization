# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx
import graphviz
import re
import matplotlib.pyplot as plt
from math import log
import matplotlib.pyplot as plt
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    G = nx.Graph()
    pattern = r'\d+'
    def load_edge_list(file_path, G):
        with open(file_path, 'r') as file:
            for line in file:
                #print(line, len(line))
                if "--" not in line:
                    continue
                #print(line.strip().split())
                node1, a, node2, weight = line.strip().split()
                numbers = re.findall(pattern, weight)
                #print(int(numbers[0]))

                G.add_edge(node1, node2, weight=int(numbers[0]))


    load_edge_list(b'C:\Users\Alexs\PycharmProjects\pythonProject48\LesMiserables.dot\LesMiserables.dot', G)
    for (u, v, wt) in G.edges.data('weight'):
        print(f"({u}, {v}, {wt})")
        
    pos = nx.shell_layout(G, [list(G.nodes)])

    nx.draw(G, pos, with_labels=True)

    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
