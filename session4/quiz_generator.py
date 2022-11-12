import random

score = 0
for i in range(1, 11):
    words = ["watermelon", "station", "generate", "discrimination"]
    randomWord = random.choice(words)
    randomChar = random.choice(randomWord)
    question = randomWord.replace(randomChar, "_", 1)

    letters = "abcdefghijklmnopqrstuvwxyz"

    answers = {randomChar}
    while len(answers) < 4:
        answers.add(random.choice(letters))
    answerList = list(answers)
    random.shuffle(answerList)
    print(f'[Question {i}]: {question}')
    for j in range(4):
        print(f'{j + 1}) {answerList[j]}')

    answer = input("Answer Number: ")
    if answerList[int(answer) - 1] == randomChar:
        score += 1

print("The test is over. Your score is", score)
