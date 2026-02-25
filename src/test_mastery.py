from mastery_calculator import calculate_mastery

strong = ['concept1', 'concept2']
weak = ['concept3']
missing = ['concept4', 'concept5']

score = calculate_mastery(strong, weak, missing)

print("\n🎯 KNOWLEDGE SCORE:", score, "%")