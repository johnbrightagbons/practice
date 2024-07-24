
   for character in secret_word: # Search for the word in the secret
       if character in answer.lower():
          print (character, end=" ") # Print the secret word on a straight line
       elif character not in answer:
          print(character, end="")
   for i in range (len(answer)):
      if len == secret_word:
          print()
      elif  answer_length == secret_word:
            print(secret_word)
      else:
            print("Sorry, the guess must have the same number of letters as the secret word.") 