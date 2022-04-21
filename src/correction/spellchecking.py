from autocorrect import Speller

spell = Speller(lang='ru')

with open("query.txt", 'r') as f:
    corrected = []
    words = f.read().split()
    for word in words:
        corrected.append(spell(word))
    with open('corrected.txt', 'w') as cor:
        cor.write(" ".join(corrected))