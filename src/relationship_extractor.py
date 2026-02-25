import re

def extract_relationships(text, concepts):

    relations = []

    text = text.lower()

    for c1 in concepts:
        for c2 in concepts:

            if c1 == c2:
                continue

            pattern = rf"{c1} (includes|uses|prevents|reduces|improves|predicts|measures|contains|affects) {c2}"

            match = re.search(pattern, text)

            if match:
                relations.append((c1, c2, match.group(1)))

    return relations