#hangman
import random

word_liste = ["hangman", "python", "computer", "spiel","programm","creatin","auto","sonnenuntergang",
              "Vogel","bienenstock","waschmaschine","schule"]
word = random.choice(word_liste)

guessed_letters = []


def hangman():

    print("Viel Spaß mit dem Spiel Galgenmännchen")

    while True :
        letter = input("Rate einen Buchstaben:")
        guessed_letters.append(letter)

        if letter in word:
            print("Richtig")

        else:
            print("Falsch")

        for letter in word:
            if letter in guessed_letters:
                print(letter,end="")    #end="" verhindert die zeilen brüche von print

            else :
                print("_",end="")


hangman()

