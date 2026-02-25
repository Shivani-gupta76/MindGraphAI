import streamlit as st

from src.load_data import load_student_answers
from src.text_preprocessor import preprocess
from src.concept_extractor import extract_concepts
from src.semantic_mapper import map_to_ideal
from src.relationship_extractor import extract_relationships
from src.ideal_graph import build_ideal_graph
from src.graph_comparator import compare_graphs
from src.mastery_calculator import calculate_mastery
from src.graph_builder import build_graph
from src.graph_visualizer import show_graph

# ===============================
# 🎨 PAGE CONFIG
# ===============================
st.set_page_config(page_title="MindGraph AI", layout="wide")
st.markdown("""
<style>

/* 🌌 MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #ffffff;
    font-size: 18px;
}

/* 📦 MAIN CONTAINER */
.block-container {
    background: rgba(0, 0, 0, 0.35);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(12px);
}

/* 🔠 HEADINGS */
h1, h2, h3 {
    color: #00FFE0;
    font-weight: 700;
}

/* 📝 ALL TEXT FIX */
p, label, div, span {
    color: #ffffff !important;
    font-size: 18px !important;
}

/* ✍ TEXT AREA */
textarea {
    background-color: #020617 !important;
    color: #00FFE0 !important;
    border-radius: 12px !important;
    font-size: 17px !important;
    border: 1px solid #00FFE0 !important;
}

/* 🎯 METRIC CARD */
[data-testid="stMetric"] {
    background: rgba(0,0,0,0.55);
    border-radius: 15px;
    padding: 18px;
    border: 1px solid #00FFE0;
}

/* 🟢 STRONG CARD */
.stSuccess {
    background-color: rgba(0, 255, 170, 0.15);
    border-left: 5px solid #00ffcc;
}

/* 🟡 WEAK CARD */
.stWarning {
    background-color: rgba(255, 200, 0, 0.15);
    border-left: 5px solid #ffd700;
}

/* 🔴 MISSING CARD */
.stError {
    background-color: rgba(255, 0, 90, 0.15);
    border-left: 5px solid #ff4d6d;
}

/* 🔘 BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #00FFE0, #00BFFF);
    color: black;
    font-size: 16px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
}

/* 🧠 GRAPH AREA */
iframe {
    background-color: white !important;
    border-radius: 12px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("🧠 MindGraph AI – Student Knowledge Analyzer")
st.markdown("### 🎓 AI-Powered Student Knowledge Understanding System")
st.markdown("---")

# ===============================
# ✍ INPUT
# ===============================
st.subheader("✍ Enter Student Answer")

if st.button("✨ Use Sample Answer"):
    user_input = """
    Machine learning includes supervised and unsupervised learning.
    Supervised learning uses labeled data and includes classification and regression.
    Linear regression predicts continuous values and logistic regression is used for classification.
    Overfitting reduces model generalization and is prevented using regularization.
    Model evaluation is done using cross validation.
    """
else:
    user_input = st.text_area("Paste the answer here")

documents = [user_input] if user_input else load_student_answers()

# ===============================
# 🚀 PROCESSING PIPELINE
# ===============================
if documents:

    all_concepts = []
    all_relations = []

    for doc in documents:

        clean_text = preprocess(doc)

        concepts = extract_concepts(clean_text)

        mapped_concepts = map_to_ideal(concepts)

        relations = extract_relationships(clean_text, mapped_concepts)

        all_concepts.extend(mapped_concepts)
        all_relations.extend(relations)

    # 🧠 BUILD STUDENT GRAPH
    student_graph = build_graph(all_concepts, all_relations)

    # 🎓 IDEAL GRAPH
    ideal = build_ideal_graph()

    # 📊 ANALYSIS
    strong, weak, missing = compare_graphs(student_graph, ideal)

    score = calculate_mastery(strong, weak, missing)

    # ===============================
    # 🧠 UNDERSTANDING LEVEL
    # ===============================
    if score < 40:
        level = "Beginner"
    elif score < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    # ===============================
    # 📊 SCORE DISPLAY
    # ===============================
    st.subheader("🎯 Knowledge Score")
    st.metric(label="Score", value=f"{score:.2f} %")

    st.subheader("🧠 Understanding Level")

    if level == "Beginner":
        st.error("Beginner")
    elif level == "Intermediate":
        st.warning("Intermediate")
    else:
        st.success("Advanced")

    # ===============================
    # 📚 CONCEPT DISPLAY
    # ===============================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🟢 Strong")
        st.success(strong if strong else "None")

    with col2:
        st.markdown("### 🟡 Weak")
        st.warning(weak if weak else "None")

    with col3:
        st.markdown("### 🔴 Missing")
        st.error(missing if missing else "None")

    # ===============================
    # 🤖 AI FEEDBACK
    # ===============================
    st.markdown("### 🤖 AI Feedback")

    if strong:
        st.write("✅ Strong in: " + ", ".join(strong))

    if weak:
        st.write("⚠ Improve: " + ", ".join(weak))

    if missing:
        st.write("📚 Learn: " + ", ".join(missing))

    # ===============================
    # 🕸 GRAPH
    # ===============================
    st.markdown("---")
    st.subheader("🧠 Knowledge Graph Visualization")

    if len(student_graph.nodes()) > 0:
        show_graph(student_graph)
    else:
        st.info("No concepts detected to display the graph.")

# ===============================
# 🧾 FOOTER
# ===============================
st.markdown("---")
st.markdown("🚀 Built using NLP • Knowledge Graphs • Semantic AI • Explainable AI")