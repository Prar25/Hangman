
import random
from Hangman_art import stages,logo
import Hangman_words
import os

print(logo)
chosen_word = random.choice(Hangman_words.word_list)
lives=6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display=[]
for i in range (len(chosen_word)):
  display.append("_")
print(display)


already_guessed=[]
#matching guess
while "_" in display and lives>=0:
  guess = input("\n\nGuess a letter: ").lower()
  os.system('cls')
  if guess in already_guessed:
           print("You already guessed this letter")
           print(display)
  else:
    for position in range (len(chosen_word)):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
              already_guessed.append(guess)
    print(display)
    

  if guess not in chosen_word:
    if guess in already_guessed:
       pass
    else:
      already_guessed.append(guess)
      print("You guessed wrong, you loose a life")
      print(stages[lives])
      lives-=1
  
  
res="".join(display)
if lives==-1:
  print("You lose.\nBetter luck next time")
elif res==chosen_word:
  print("You won.\nCongratulations!")
 