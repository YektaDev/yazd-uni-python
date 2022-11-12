# Get
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.get('age'))
print(dic.get('mother', 25))
# print(dic['mother']) Error!

# Items
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.items())

# Keys
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.keys())

powTable = {1: None, 2: None, 3: None, 4: None, 5: None}
for i in powTable.keys():
    powTable[i] = int(i) ** 2
print(powTable.items())

# Pop(key)
# Removes the item with the key and returns its value.
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.pop('age'))

# Popitem
# Removes the last item and returns it as a tuple
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
a = dic.popitem()
print(a)

# setdefault
# Returns the value of the item with the specified key. If the key does not exist, inserts the key, with the specified
# value. If no value is specified, the value will be None.
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.setdefault('age'))
print(dic.setdefault('mother', 25))

# update
# Updates the dictionary with the specified key-value pairs.
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
dic.update({'age': 32, 'mother': 25})
dic.update({'name': 'Kotlin', 'mother': 25})
print(dic)

# values
# Returns a list of all the values in the dictionary.
dic = {
    'name': 'Python',
    'age': 31,
    'father': 'Guido van Rossum'
}
print(dic.values())

# ====================================================== Exercise ======================================================
text = """
At JetBrains, code is our passion.
Ever since we started.
back in 2000.
we have strived to make the strongest, most effective developer tools on earth.
By automating routine checks and corrections, our tools speed up production, freeing developers to grow and create.
Dogfooding is not just a philosophy at JetBrains but a way of life.
We are in a position to use the tools we develop to develop our own tools.
This provides us with unique insight into our products.
We make sure to do something about it, even if that means creating a new product.
"""
wordsCount = {}
wordsList = text.split(sep=' ')
sentences = text.split('.')
sentencesWithRepetitiveWords = []
threshold = 5
for word in wordsList:
    wordsCount[word] = wordsCount.get(word, 0) + 1
for word in wordsCount.copy():
    if wordsCount[word] < threshold:
        wordsCount.pop(word)
for sentence in sentences:
    for word in wordsCount:
        if sentence.split(' ').__contains__(word) and not sentencesWithRepetitiveWords.__contains__(sentence):
            sentencesWithRepetitiveWords.append(sentence)
print(sentencesWithRepetitiveWords)
