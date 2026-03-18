#hangman
import random

word_liste = ["hangman", "python", "computer", "spiel","programm","creatin","auto","sonnenuntergang",
              "Vogel","bienenstock","waschmaschine","schule"]
word = random.choice(word_liste)
guessed_letters = []



#funkton
def hangman():
    attempts = 5  # versuche

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
            attempts -= 1
            print("Falsch""Versuche übrig:",attempts)
            if attempts <= 0:
                print("Game over" "\n" "Das wort wahr:",word)
                break

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

