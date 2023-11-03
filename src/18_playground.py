words = ['amor', 'sol', 'piedra', 'dia']
words_v2 = ['rosa', 'gol', 'dia', 'pez', 'gafas']

def filter_by_length(wordList):
    return list(filter(lambda word: len(word) >= 4, wordList))

print(filter_by_length(words_v2))