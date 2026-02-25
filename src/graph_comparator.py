def compare_graphs(student_graph, ideal_graph):

    strong = []
    weak = []
    missing = []

    student_nodes = set(student_graph.nodes())
    ideal_nodes = set(ideal_graph.nodes())

    # 🔴 Missing concepts
    for node in ideal_nodes:
        if node not in student_nodes:
            missing.append(node)

    # 🟢 / 🟡 Present concepts
    for node in student_nodes:

        if node in ideal_nodes:

            student_connections = set(student_graph.edges(node))
            ideal_connections = set(ideal_graph.edges(node))

            if len(student_connections) >= len(ideal_connections):
                strong.append(node)
            else:
                weak.append(node)

    return strong, weak, missing