#Step 1 
import random
from hangman_art import logo,stages
from hangman_word_list import word_list
lives = 6

#word_list = ["aardvark", "baboon", "camel"]
print(logo)

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
        
        
    
    
    
