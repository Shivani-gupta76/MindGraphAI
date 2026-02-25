from keybert import KeyBERT
import os

DATA_PATH = "data/student_answers"

kw_model = KeyBERT()

# Ideal ML syllabus concepts
ideal_concepts = [
    "supervised learning",
    "unsupervised learning",
    "linear regression",
    "logistic regression",
    "classification",
    "overfitting",
    "cross validation",
    "regularization",
    "model evaluation"
]


def load_student_answers():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents


def extract_concepts(text):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )
    return [kw[0] for kw in keywords]


docs = load_student_answers()

student_concepts = []

for doc in docs:
    student_concepts.extend(extract_concepts(doc))

student_concepts = list(set(student_concepts))


strong = []
missing = []

for concept in ideal_concepts:
    if any(concept in sc for sc in student_concepts):
        strong.append(concept)
    else:
        missing.append(concept)


print("\n🎓 KNOWLEDGE ANALYSIS REPORT")

print("\n✅ Strong Concepts:")
print(strong)

print("\n❌ Missing Concepts:")
print(missing)