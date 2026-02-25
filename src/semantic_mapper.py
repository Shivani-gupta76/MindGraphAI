from sentence_transformers import SentenceTransformer, util

# 🔹 Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🎓 FULL IDEAL CONCEPT ONTOLOGY (concept-level, not long phrases)
ontology = [
    "machine learning",
    "supervised learning",
    "unsupervised learning",
    "linear regression",
    "logistic regression",
    "classification",
    "model evaluation",
    "cross validation",
    "overfitting",
    "regularization",
    "generalization"
]

# 🔹 Precompute ontology embeddings
ontology_embeddings = model.encode(ontology, convert_to_tensor=True)


def map_to_ideal(concepts):

    mapped = set()

    for concept in concepts:

        concept_embedding = model.encode(concept, convert_to_tensor=True)

        similarities = util.cos_sim(concept_embedding, ontology_embeddings)[0]

        best_idx = similarities.argmax()

        # ✅ Correct threshold for student natural language
        if similarities[best_idx] > 0.50:
            mapped.add(ontology[best_idx])

    return list(mapped)