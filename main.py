#hangman
import random

word_liste = ["hangman", "python", "computer", "spiel","programm","creatin","auto","sonnenuntergang",
              "Vogel","bienenstock","waschmaschine","schule"]
word = random.choice(word_liste)

guessed_letters = []

#funkton
def hangman():

    print("Viel Spaß mit dem Spiel Galgenmännchen")

    while True :
        user_letter = input("\n""Rate einen Buchstaben: ")

        # verhindert doppelte eingaben
        if user_letter in guessed_letters:
            print("Die Buchsaben ",guessed_letters, "hast du schon benutzt")
            continue
        else:
            guessed_letters.append(user_letter)

        #rückmeldung richtig falsch
        if user_letter in word:
            print("Richtig")
        else:
            print("Falsch")

        #wort anzeige
        for word_letter in word:
            if word_letter in guessed_letters:
                print(word_letter,end="")    #end="" verhindert die zeilenumbrüche von print

            else :
                print("_",end="")
        #prüfung ob gewonnen
        win = True
        for letter in word:
            if letter not in guessed_letters:
                win = False
                break
        if win :
            print("\n""Gewonnen du hast das Wort ", word, "erraten")
            break

#funktion starten
hangman()

