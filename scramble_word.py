import random
words = ["python","java","javascript","pytest","Automation","guvi","selenium"]
word= random.choice(words)
scramble_word = (".join(random.sample(word,len(word)))"
                 "print(scramble_word)")
guess_word = "none"
while guess_word != word:
   guess_word = input("Enter the word")
   if guess_word == word:
         print("your guess is correct,you won")
   else:
         print("your guess is wrong...Try again")