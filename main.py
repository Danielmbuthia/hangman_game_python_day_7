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
game_ends = False
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
    
while "_" in display and not game_ends and lives > 0: 
    guess = input("Guess a letter: ").lower()
    for index,item in enumerate(chosen_word):
        if guess == item:
            display[index] =item
            
    if guess not in chosen_word:
        print(stages[lives])
        lives -=1
        if lives == 0:
            game_ends = True
    if "_" not in display:
        game_ends = True
    print(display)
    if lives == 0 and "_" in display:
        print("You lose")
    elif game_ends:
        print("You won")
    
    
    
