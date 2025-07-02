
# notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# moyenne = sum(notes) / len(notes)

# notes_sup = []

# for note in notes:
#     if note > moyenne:
#         notes_sup.append(note)

# print(moyenne)
# print(notes_sup)

Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"

Ch1_words = set(Ch1.split())
Ch2_words = set(Ch2.split())
common = Ch1_words & Ch2_words
print(common)
