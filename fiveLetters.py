import string
import random
import nltk
from random_word import RandomWords
nltk.download('words')

#english checker
from nltk.corpus import words as nltk_words
def is_english_word(check):
    # creation of this dictionary would be done outside of
    #     the function because you only need to do it once.
    dictionary = dict.fromkeys(nltk_words.words(), None)
    try:
        x = dictionary[check]
        return True
    except KeyError:
        return False
def game():
  guessNum = 0
  #word = str(input("Enter a five letter word: "))
  #if len(word) != 5:
    #print("Your word is not five letters")
    #word = str(input("Enter a five letter word: "))
  word = ""
  r = RandomWords()
  if is_english_word(word) == True or word == "":
    if len(word) == 5:
      word = word
    elif len(word) > 5:
      word = word.replace(word[5:],"")
      if is_english_word(word) == False:
        word = r.get_random_word()
        while len(word) != 5:
          word = r.get_random_word()
    elif len(word) < 5:
      while len(word) < 5:
        word = word + random.choice(string.ascii_letters)
        if is_english_word(word) == False:
          word = r.get_random_word()
          while len(word) != 5:
            word = r.get_random_word()
  elif is_english_word(word) == False:
    word = r.get_random_word()
    while len(word) != 5:
      word = r.get_random_word()
  word = word.upper()
  print("You have 5 guesses remaining.")
  while guessNum < 5:
    guess = str(input("Enter your guess: "))
    guess = guess.upper()
    if len(guess) == 5: #and is_english_word(guess) == True:
      if guess == word:
        print("Correct!")
        break
      else:
        guessNum += 1
        for i, j in zip(word, guess):
          if i in word and i in j:
            print("{} ✔️".format(j))
          elif j in word:
            print("{} 😶".format(j))
          else:
            print("  ❌")
        if 5 - guessNum != 0:
          print("You have {} guesses remaining.".format(5 - guessNum))
    else:
      print("Please enter a valid, five letter word.")
      guess = str(input("Enter your guess: "))
      guess = guess.upper()
      if len(guess) == 5:
        if guess == word:
          print("Correct!")
          break
        else:
          guessNum += 1
          for i, j in zip(word, guess):
            if i in word and i in j:
              print("{} ✔️".format(j))
            elif j in word:
              print("{} 😶".format(j))
            else:
              print("  ❌")
          if 5 - guessNum != 0:
            print("You have {} guesses remaining.".format(5 - guessNum))
  if guessNum == 5:
    print("Game over. The correct word was {}.".format(word))

game()
