import networkx as nx

def build_ideal_graph():

    G = nx.DiGraph()

    # Core ML concepts
    G.add_edge("machine learning", "supervised learning")
    G.add_edge("machine learning", "unsupervised learning")

    G.add_edge("supervised learning", "linear regression")
    G.add_edge("supervised learning", "logistic regression")
    G.add_edge("supervised learning", "classification")

    G.add_edge("model evaluation", "cross validation")
    G.add_edge("model evaluation", "generalization")

    G.add_edge("overfitting problem in machine learning", "model generalization ability")
    G.add_edge("regularization method", "overfitting problem in machine learning")

    return G