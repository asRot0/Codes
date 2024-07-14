from random import randint
name = raw_input("Enter your name:")
print "hello", name
print "* * * Welcome to the game 'Battleship' * * *"
print " There's a battleship hidden in the ocean and you have to destroy it to win the game"
print "How to play:"
print "1. The position of the ship is unknown to the player so you have to guess where it's hidden."
print "2. You choose the position but gessing a row and collum"
print " the counting starts from 0 so the first row or first collum is 0"
print "3. You will have 3 guesses. If you guess the possion aquirately you destroy."
print "4. If you cann't destoy the ship within 3 guesses you lose the game"
win = 0
lose = 0
start = raw_input("Do you want to start the game? Y/N")
while start.upper() == "Y":
    board = []
    df=int(raw_input("Select Difficulty: 1.Pussy 2.Tough guy 3.Badass"))

    if (df == 1):
        for n in range(0, 5):
            board.append(["~"] * 5)
        def random_row(board):
            return randint(0,len(board)-1)
        def random_col(board):
            return randint(0,len(board)+4)
    elif(df==2):
        for n in range(0, 5):
            board.append(["~"] * 10)
        def random_row(board):
            return randint(0,len(board)-1)
        def random_col(board):
            return randint(0,len(board)+4)
    elif(df==3):
        for n in range(0, 5):
            board.append([" "] * 10)
        def random_row(board):
            return randint(0,len(board)-1)
        def random_col(board):
            return randint(0,len(board)+4)
    
    def print_board(board): 
       for x in board:
        print " ".join(x)
        
    print_board(board)
    
    
    
    ship_row = random_row(board)
    ship_col = random_col(board)
    #print ship_row
    #print ship_col
    for turn in range(3):
        print "turn:" , turn + 1
    
        guess_row = int(raw_input("guess a row:"))
        guess_col = int(raw_input("guess a col:"))

        if guess_row == ship_row and guess_col == ship_col:
          print ("Nice job! you destroyed the ship and everyone in it!")
          board[guess_row][guess_col] = "X"
          break
        else:
            if (df == 1) and (guess_row not in range(5) or guess_col not in range(5)):
              print "Wow! Your aim sucks so much it was not even in the ocean!"
            elif guess_row not in range(5) or guess_col not in range(10):
                n=0
                while True:
                    
                  print "Wow! Your aim sucks so much it was not even in the ocean!"
                  print "sike nigga!! you thought!! (" , n , ")"
                  n=n+1
            elif board[guess_row][guess_col] == "X":
                print "Already guessed that one you moron!"
            else:
                print "Your aim sucks"
                board[guess_row][guess_col] = "X"
            if (turn == 2):
                print "game over, loser!"
            print_board(board)

    if guess_row == ship_row and guess_col == ship_col:
        win = win + 1
    else:
        lose = lose + 1
    print "Total win:" , win
    print "Total lose:", lose
    start = raw_input("do you want to start again? Y/N")
    
print("Alright then,Keep Your Game,Pussy ")
print "Total win:" , win
print "Total lose:", lose
