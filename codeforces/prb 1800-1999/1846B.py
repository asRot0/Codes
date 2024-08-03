'''
def check_win(field, symbol):
    for row in field:
        if row.count(symbol) == 3:
            return symbol
    for col in range(3):
        if field[0][col] == symbol and field[1][col] == symbol and field[2][col] == symbol:
            return symbol
    if field[0][0] == symbol and field[1][1] == symbol and field[2][2] == symbol:
        return symbol
    if field[0][2] == symbol and field[1][1] == symbol and field[2][0] == symbol:
        return symbol
    return None

def main():
    t = int(input())
    for _ in range(t):
        field = []
        for _ in range(3):
            field.append(input())
        winner = check_win(field, "X")
        if winner is not None:
            print(winner)
        elif check_win(field, "O") is not None:
            print("O")
        elif check_win(field, "+") is not None:
            print("+")
        else:
            print("DRAW")

if __name__ == "__main__":
    main()
'''


t = int(input())  # Number of test cases

# Function to check if a symbol has won the game
def check_winner(symbol):
    for i in range(3):
        # Check for horizontal wins
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True

        # Check for vertical wins
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True

    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

for _ in range(t):
    board = []

    # Read the game board
    for _ in range(3):
        row = list(input())
        board.append(row)

    x_wins = o_wins = plus_wins = False

    # Check for horizontal, vertical, and diagonal wins for each symbol
    for row in board:
        if row.count("X") == 3:
            x_wins = True
        elif row.count("O") == 3:
            o_wins = True
        elif row.count("+") == 3:
            plus_wins = True

    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count("X") == 3:
            x_wins = True
        elif column.count("O") == 3:
            o_wins = True
        elif column.count("+") == 3:
            plus_wins = True

    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        x_wins = True
    elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        o_wins = True
    elif board[0][0] == board[1][1] == board[2][2] == "+" or board[0][2] == board[1][1] == board[2][0] == "+":
        plus_wins = True

    # Determine the result of the game
    if x_wins and not o_wins and not plus_wins:
        print("X")
    elif o_wins and not x_wins and not plus_wins:
        print("O")
    elif plus_wins and not x_wins and not o_wins:
        print("+")
    elif not x_wins and not o_wins and not plus_wins:
        if "." in [cell for row in board for cell in row]:
            print("DRAW")
        else:
            print("DRAW")
