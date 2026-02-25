import os

DATA_PATH = "data/student_answers"

def load_student_answers():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents