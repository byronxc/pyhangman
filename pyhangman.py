import random

wordsList = ["python", "computer", "barcelona", "java", "integer", "joy", "college", "california"]
cogratWordsList = ["Nice", "Great", "Wonderful", "Magnificent", "Good job", "Incredible", "Super"]

word = random.choice(wordsList)
word2= ""
finalWord = ""
life = 5
flag = False
answer = []

for x in range(len(word)):
        answer.insert(x, '_')

print("Hangman Game\n")
name = input("Enter your name: ")
print("Welcome " + name + "!!\n\n" )

while(life != 0):
    congratWord = random.choice(cogratWordsList)
    print(answer)
    letter = input("Enter a letter: ")
    if(letter[0] not in word):
        print("Wrong letter! ")
        life -=1
        if life == 0: 
            print("Game Over")
            print("The word was " + word)
        else:
            print("You have " + str(life) + " more chances")
    elif letter[0] not in finalWord:
        for x in range(len(word)):
            if letter[0] == word[x]:
                answer[x] = letter[0]
        print(congratWord + "!!")
        finalWord = word2.join(answer)
        if(finalWord == word):
                life = 0
                print("You win!!\n")
                print(answer)
    else:
        print("You already guessed that letter!")
    print()