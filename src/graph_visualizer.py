from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
import tempfile

def show_graph(graph):

    net = Network(height="500px", width="100%", directed=True)

    for node in graph.nodes():
        net.add_node(node, label=node)

    for source, target, data in graph.edges(data=True):
        net.add_edge(source, target, label=data.get("label", ""))

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    net.save_graph(tmp_file.name)

    HtmlFile = open(tmp_file.name, "r", encoding="utf-8")
    components.html(HtmlFile.read(), height=500)