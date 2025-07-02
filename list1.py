
# notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# moyenne = sum(notes) / len(notes)

# notes_sup = []

# for note in notes:
#     if note > moyenne:
#         notes_sup.append(note)

# print(moyenne)
# print(notes_sup)

######################

# Ch1 = "Le langage Python est très populaire"
# Ch2 = "Python est un langage puissant"

# Ch1_words = set(Ch1.split())
# Ch2_words = set(Ch2.split())
# common = Ch1_words & Ch2_words
# print(common)

#########################
# stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]
# InitialValue = stock[0]
# print(InitialValue)

# data = []
# for a in stock:
#     if isinstance(a , str):
#         data.append(a)
# print(data)

# data2 = []
# for b in stock:
#     if isinstance(b ,int):
#         data2.append(b)
# print(data2)


# data2.sort()
# print(data2)

# data.sort()
# print(data)

##############################

def ElementSearch(element, lst):
    if element in lst:
        return True
    else:
        return False

names = ["saad", "anas", "ayoub"]
print(ElementSearch("saad", names))

data = [1, "raja", 3, 4]
print(ElementSearch("raja", data))  
print(ElementSearch(10, data))       

    
