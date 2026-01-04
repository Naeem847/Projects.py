import random

# ---------------------------
# Board Setup
# ---------------------------
board = [' ' for _ in range(9)]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# ---------------------------
# Check Winner
# ---------------------------
def check_winner(board):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]

    if ' ' not in board:
        return 'Tie'

    return None

# ---------------------------
# Minimax Algorithm (with depth limit)
# ---------------------------
def minimax(board, depth, is_maximizing, max_depth=None):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Tie':
        return 0

    if max_depth is not None and depth >= max_depth:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False, max_depth)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True, max_depth)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# ---------------------------
# AI Move Based on Difficulty
# ---------------------------
def ai_move_difficulty(board, difficulty):
    available = [i for i in range(9) if board[i] == ' ']

    if difficulty == 'Easy':
        return random.choice(available)

    elif difficulty == 'Medium':
        best_score = -float('inf')
        move = None
        for i in available:
            board[i] = 'X'
            score = minimax(board, 0, False, max_depth=2)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
        return move

    else:  # Hard
        best_score = -float('inf')
        move = None
        for i in available:
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
        return move

# ---------------------------
# Player Move
# ---------------------------
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a valid number (0-8).")

# ---------------------------
# Game Loop
# ---------------------------
def play_game():
    global board
    board = [' ' for _ in range(9)]

    print("Tic-Tac-Toe: AI (X) vs Player (O)")
    difficulty = ""

    while difficulty not in ['Easy', 'Medium', 'Hard']:
        difficulty = input("Choose difficulty (Easy/Medium/Hard): ")

    print_board(board)

    while True:
        # Player move
        player_move(board)
        print_board(board)

        winner = check_winner(board)
        if winner:
            break

        # AI move
        move = ai_move_difficulty(board, difficulty)
        board[move] = 'X'
        print(f"AI chooses position {move}")
        print_board(board)

        winner = check_winner(board)
        if winner:
            break

    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

# ---------------------------
# Run Game
# ---------------------------
play_game()
