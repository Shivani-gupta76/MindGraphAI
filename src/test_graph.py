from graph_builder import build_graph

concepts = [
    "overfitting problem in machine learning",
    "model generalization ability",
    "regularization method"
]

relationships = [
    ("overfitting problem in machine learning", "reduces", "model generalization ability"),
    ("regularization method", "prevents", "overfitting problem in machine learning")
]

G = build_graph(concepts, relationships)

print("\n🧠 GRAPH INFO")
print("Nodes:", G.nodes())
print("Edges:", G.edges(data=True))