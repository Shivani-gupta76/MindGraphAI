from keybert import KeyBERT
import spacy

kw_model = KeyBERT()
nlp = spacy.load("en_core_web_sm")

def extract_concepts(text):

    keybert_keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=10
    )

    keybert_concepts = [kw[0] for kw in keybert_keywords]

    doc = nlp(text)
    spacy_concepts = [chunk.text.lower() for chunk in doc.noun_chunks]

    all_concepts = list(set(keybert_concepts + spacy_concepts))

    return all_concepts