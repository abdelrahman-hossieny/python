import random

def choose_square(x):
    if x >= 1 and x <= 9:  
        row = (x - 1) // 3  
        col = (x - 1) % 3  
        return row, col
    else:
        return None, None

def print_board():
    for row in game_list:
        print("|", row[0], "|", row[1], "|", row[2], "|")

def check_winner(board, player):
    # التحقق من الصفوف
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # التحقق من الأعمدة
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # التحقق من الأقطار
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if type(cell) == int:  # إذا كان هناك خلية تحتوي على رقم، اللعبة لم تنتهي بعد
                return False
    return True

# ===================MAIN()========================

game_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_board()


while True:
    # PLAYER TURN
    user_input = int(input("enter number(1-9): "))
    row, col = choose_square(user_input)

    if row is not None and col is not None:
        game_list[row][col] = "O"
    else:
        print("enter AGIAN[from(1-9)]: ")
        continue
    
    print_board()
    print()

    if check_winner(game_list, "O"):
        print("!!!!!!<YOU WIN>!!!!!")
        break
    
    if check_draw(game_list):
        print("!!!!!!<DRAW>!!!!!")
        break

    # COMPUTER TURN
    available_squares = []
    for row in game_list:
        for cell in row:
            if type(cell) == int:
                available_squares.append(cell)

    computer_input = random.choice(available_squares)
    row, col = choose_square(computer_input)
    game_list[row][col] = "X"

    print_board()
    print()

    if check_winner(game_list, "X"):
        print("COMPUTER WINS")
        break
    
    if check_draw(game_list):
        print("!!!!!!<DRAW>!!!!!")
        break
