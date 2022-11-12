chars = {}
# Read and set the frequency of each character
with open("data.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        for letter in line.lower():
            chars[letter] = chars.get(letter, 0) + 1

# Sort the dictionary by value (for printing)
chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

# Print the results
print("Character frequency report:")
print("|\tCh\t| |\tFrq\t|")
for charName, freq in chars.items():
    print('|\t{}\t| |\t{}\t|'.format(charName, freq))
