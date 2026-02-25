from semantic_mapper import map_to_ideal

student_concepts = [
    "model memorizes training data and fails on test data"
]

mapped = map_to_ideal(student_concepts)

print("\n🧠 MAPPED CONCEPTS:\n")
print(mapped)