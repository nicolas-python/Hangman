#hangman
import random

word_liste = ["hangman"]
wort = random.choice(word_liste)


print("Viel Spaß mit dem Spiel Galgenmännchen")

buchstabe = input("Rate einen Buchstaben:")

if buchstabe in wort:
    print("Richtig")

else:
    print("Falsch")