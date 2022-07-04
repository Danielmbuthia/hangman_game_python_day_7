#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
    
while "_" in display and lives >= 0: 
    guess = input("Guess a letter: ").lower()
    for index,item in enumerate(chosen_word):
        if guess == item:
            display[index] =item
    print(display)
    if guess not in chosen_word:
        print(stages[lives])
        lives -=1
        if lives < 0:
            print("You lose")
    if "_" not in display:
        print("You won")
        
        
    
    
    
