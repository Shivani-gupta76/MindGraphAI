import networkx as nx

def build_graph(concepts, relations):

    G = nx.DiGraph()

    # ✅ add concept nodes
    for concept in concepts:
        G.add_node(concept)

    # ✅ add relationship edges
    for source, target, label in relations:
        G.add_edge(source, target, label=label)

    return G