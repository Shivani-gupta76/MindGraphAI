def calculate_mastery(strong, weak, missing):

    total = len(strong) + len(weak) + len(missing)

    if total == 0:
        return 0

    score = (len(strong) * 1 + len(weak) * 0.5) / total * 100

    return round(score, 2)