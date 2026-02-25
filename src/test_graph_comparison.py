from graph_builder import build_graph
from ideal_graph import build_ideal_graph
from graph_comparator import compare_graphs

# 🧠 Student graph
student_concepts = [
    "overfitting problem in machine learning",
    "model generalization ability",
    "regularization method"
]

student_relations = [
    ("overfitting problem in machine learning", "reduces", "model generalization ability")
]

student_graph = build_graph(student_concepts, student_relations)

# 🎓 Ideal graph
ideal_graph = build_ideal_graph()

# ⚖ Compare
strong, weak, missing = compare_graphs(student_graph, ideal_graph)

print("\n🧠 KNOWLEDGE ANALYSIS")
print("\n🟢 Strong:", strong)
print("\n🟡 Weak:", weak)
print("\n🔴 Missing:", missing)