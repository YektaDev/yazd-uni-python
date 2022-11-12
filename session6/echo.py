word = input()
for i in range(len(word)):
    print(f'{word[i] * i}{word[i:]}')
