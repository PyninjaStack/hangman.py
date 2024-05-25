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

word_list =["camel","baboon","elephant","lion","crocodile","kangaroo"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6

#create blanks

display = []
#for letter in chosen_word:
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter? ").lower()

    #for letter in chosen_word:
        #if letter == guess:
        #   print("Right")
        #else:
        #   print("Wrong")

    for position in range(word_lenght):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        '''else:
            print("No Match")'''
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(stages[lives])
