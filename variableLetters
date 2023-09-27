#no defined length version
def game2():
  word1 = "Walk"
  word1 = word1.upper()
  guessNum1 = len(word1)
  while guessNum1 > 0:
    guess1 = str(input("Enter your guess:" ))
    guess1 = guess1.upper()
    if guess1 == word1:
      print("Correct!")
      break
    else:
      PosDifference = len(word1) - len(guess1)
      NegDifference = len(guess1) - len(word1)
      guessNum1 -= 1
      if len(guess1) > len(word1):
        print("Your guess is {} letters too long".format(NegDifference))
        for i_word, j_guess in zip(word1, guess1):
          if i_word in word1 and i_word in j_guess:
            print("{} ✔️".format(j_guess))
          elif j_guess in word1:
            print("{} 😶".format(j_guess))
          else:
            print("  ❌")
      if len(guess1) < len(word1):
        print("Your guess is {} letters too short".format(PosDifference))
        for i_word, j_guess in zip(word1, guess1):
          if i_word in word1 and i_word in j_guess:
            print("{} ✔️".format(j_guess))
          elif j_guess in word1:
            print("{} 😶".format(j_guess))
          else:
            print("  ❌")
      if len(guess1) == len(word1):
        for i_word, j_guess in zip(word1, guess1):
          if i_word in word1 and i_word in j_guess:
            print("{} ✔️".format(j_guess))
          elif j_guess in word1:
            print("{} 😶".format(j_guess))
          else:
            print("  ❌")
      print("You have {} guesses remaining.".format(guessNum1))

game2()
