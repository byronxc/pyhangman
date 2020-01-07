import random

draw = ["""
  ______
  |    |      
  |    o     
  |   /|\    
  |    |
  |   / \ 
 _|_
""",
"""
  ______
  |    |      
  |    o     
  |   /|\    
  |    |
  |   /  
 _|_
""",
"""
  ______
  |    |      
  |    o      
  |   /|\    
  |    |
  |     
 _|_
""",
"""
  ______
  |    |      
  |    o      
  |   /|\     
  |    
  |    
 _|_
""",
"""
  ______
  |    |      
  |    o      
  |   /|     
  |    
  |     
 _|_
""",
"""
  ______
  |    |      
  |    o      
  |    |     
  |    
  |     
 _|_
""",
"""
  ______
  |    |      
  |    o      
  |        
  |    
  |     
 _|_
""",
"""
  ______
  |    |      
  |          
  |         
  |    
  |     
 _|_
""",
"""
  ______
  |          
  |          
  |        
  |    
  |     
 _|_
"""]

wordsList = ["python", "computer", "barcelona", "java", "integer", "joy", "college", "california"]
cogratWordsList = ["Nice", "Great", "Wonderful", "Magnificent", "Good job", "Incredible", "Super"]
word2= ""
finalWord = ""
life = 8
flag = False
answer = []



print("Hangman Game\n")
print("1. Choose a word")
print("2. Random word \n")
option = input()
if(option == "1"):
    word = input("Enter the word: ")
else:
    word = random.choice(wordsList)

for x in range(len(word)):
        answer.insert(x, '_')
        
name = input("Enter your name: ")
print("Welcome " + name + "!!\n\n" )

while(life != 0):
    congratWord = random.choice(cogratWordsList)
    print(draw[life])
    print(answer)
    letter = input("Enter a letter: ")
    if(letter[0] not in word):
        print("Wrong letter! ")
        life -=1
        if life == 0: 
            print("Game Over")
            print("The word was " + word)
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
