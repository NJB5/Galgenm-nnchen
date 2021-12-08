play = input("Möchtest du eine Runde Galgenmännchen spielen? (Ja/Nein)").upper()
while play == "JA":   
    with open ("galgenmaennchen.txt", "r") as text_datei:
            words = text_datei.read()
            word_list = words.split("\n")

    from random import randint
    a = len(word_list)-1
    x = randint(0,a)
    solution = word_list[x] #Auswahl des Wortes
    solution = solution.upper()

    lWord = len(solution)
    striche = lWord * "_ " #Ausgabe der Striche anhand der Anzahl der Buchstaben im ausgewählten Wort
    stricheTwo =lWord *"_"
    print(striche)
    

    #Variablen
    right = []
    wrong = []
    tries = 0
    level = 0
    solution_list = list(solution)
    striche_list = list(stricheTwo)
    win = "false"

    #Schwierigkeitsgrad
    difficulty = input("Welchen Schwierigkeitsgrad wählst du? (Leicht/Mittel/Schwer) \n").upper()
    while level == 0:
        if difficulty == "LEICHT":
            level = 1
            tries = 7
            print("Du spielst auf dem Level Leicht (1) und hast", tries,"Versuche!")
        elif difficulty == "MITTEL":
            level = 2
            tries = 6
            print("Du spielst auf dem Level Mittel (2) und hast", tries,"Versuche!")
        elif difficulty == "SCHWER":
            level = 3
            tries = 5
            print("Du spielst auf dem Level Schwer (3) und hast", tries ,"Versuche!")
        else:
            print("Du hast keinen gültigen Schwierigkeitsgrad gewählt. Versuche es nochmal!")
            difficulty = input("Welchen Schwierigkeitsgrad wählst du? (Leicht/Mittel/Schwer)").upper()
            
    #Raten der Buchstaben
    while tries > 0:
        if win == "false":
            guess = input("Gib einen Buchstaben ein:")
            guess = guess.upper()
            print("Das ist der Buchstabe, den du eingegeben hast:", guess)
            print("\n")
            if guess in solution:
                counter = 0
                right += guess
                print(guess, "war richtig!")
                print("Du hast noch", tries, "Versuche übrig.")
                print("\n")
                print("Das sind deine richtig geratenen Buchstaben:", right)
                print("Das sind deine falsch geratenen Buchstaben:", wrong)
                while counter != lWord:
                    if solution_list[counter] == guess:
                        striche_list[counter] = guess
                    counter +=1
                print(striche_list)    
            else:
                wrong += guess
                print(guess, "war falsch!")
                tries -= 1
                print("Du hast noch", tries, "Versuche übrig.")
                print("\n")
                print("Das sind deine richtig geratenen Buchstaben:", right)
                print("Das sind deine falsch geratenen Buchstaben:", wrong)
                print("\n")
            if solution_list == striche_list:
                solution = "".join(solution_list)
                print(solution)
                print("Du hast gewonnen! Das Wort ist", solution)
                exit()
    if tries == 0:
        print("Du hast keiner Versuche mehr übrig. Das Wort wäre", solution, "gewesen.")
        exit()
                
   
        



