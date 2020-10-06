from Book import Word

def accueil():
    print("Hey There, wants to learn Something ?")
    print("--------")
    print("To Play, press >>>>> p")
    print("To Add a word, press >>>>> a")
    print("To Remove a word, press >>>>> r")
    print("To Quit, press >>>>> q")
    print("--------")
    wahl = input("So What ?: ")

    if wahl == "p":
        play()
    elif wahl == "a":
        add()
    elif wahl == "r":
        remove()
    elif wahl == "q":
        print("Bye Bye")
        pass
    else:
        print("You should use one of this 3 letters ...")
        wahl = input("So What ?: ")

def play():
    run = True
    while run:
        b = Word()
        question = b.pickWord()
        print("HERE IS THE GUESS: {}".format(question[0]))
        answer = input("GIVE YOUR ANSWER BITCH: ")
        result = b.compareWord(question[0],answer)
        if result:
            print("YEAH")
        else:
            print("NOOOOOOOOoOOOOOoooOoOOooOO")
        b.updateWord(question[0], result)
        whatsNext = input("What do you want next: Enter = Play, q+Enter=Quit: ")
        if whatsNext == "q":
            print("You will be redirected to Main")
            run = False
            accueil()

def add():
    run = True
    while run:
        print("Ok you want to add a Word ...")
        de = input("Please add AUF DEUTSCH: ")
        fr = input("Please add AUF FRANZÖSISCH: ")
        b = Word()
        b.newWord(de,fr)
        print("OK your word is now in the database...")
        answer = input("Do you want to add an other word? (y/n)")
        if answer == "n":
            print("You will be redirected to Main")
            run = False
            accueil()
        elif answer == "y":
            pass
        else:
            print("You should use y or n ...")
        
        
def remove():
    run = True
    while run:
        print("OK you want to remove a Word ...")
        print("Which one would you like to remove ?")
        print("If you want to see a list of the entire database, enter DB")
        print("Otherwise, type the word to be removed...")
        answer = input("Then what ?: ")
        b = Word()
        listDataBase = b.getDico()
        if answer == "DB":
            print(listDataBase.keys())
        else:
            b.deleteWord(answer)
        print("OK your word is now out of the database...")
        answer = input("Do you want to remove an other word? (y/n)")
        if answer == "n":
            print("You will be redirected to Main")
            run = False
            accueil()
        elif answer == "y":
            pass
        else:
            print("You should use y or n ...")
        

accueil()
