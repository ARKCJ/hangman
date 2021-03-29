def hangman(word):
    wrong = 0
    stage = ["",
             "________      ",
             "|             ",
             "|       |     ",
             "|       O     ",
             "|      /|\\    ",
             "|      / \\    ",
             "|             "
            ]
    rletters = list(word)
    board = ["_"]*len(word)
    win  = False
    print("Welcome to Hangman")
    while wrong < len(stage):
        print("\n")
        char = input("Guess a word: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '&'
        else:
            wrong = wrong + 1
        print(" ".join(board))
        print("\n".join(stage[0:wrong + 1]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stage[0:wrong]))
        print("You lose! It was {}".format(word))
hangman("cat")