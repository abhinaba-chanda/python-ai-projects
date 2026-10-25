"""
Tic-tac-toe against an unbeatable AI using the Minimax algorithm.

Minimax tries every possible future move, assuming both players
play perfectly, and picks the move with the best guaranteed result.
Score: +1 if the AI wins, -1 if you win, 0 for a draw.

Run:  python tictactoe.py
"""
import math

AI, HUMAN, EMPTY = "O", "X", " "
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def minimax(board, is_ai_turn, depth=0):
    """Return the score of this board for the AI."""
    w = winner(board)
    if w == AI:
        return 10 - depth   # win faster = better
    if w == HUMAN:
        return depth - 10   # lose later = less bad
    if is_full(board):
        return 0

    best = -math.inf if is_ai_turn else math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI if is_ai_turn else HUMAN
            score = minimax(board, not is_ai_turn, depth + 1)
            board[i] = EMPTY
            best = max(best, score) if is_ai_turn else min(best, score)
    return best


def best_move(board):
    best_score, move = -math.inf, None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score, move = score, i
    return move


def show(board):
    rows = []
    for r in range(3):
        cells = [board[r * 3 + c] if board[r * 3 + c] != EMPTY else str(r * 3 + c + 1) for c in range(3)]
        rows.append(" " + " | ".join(cells))
    print("\n" + "\n---+---+---\n".join(rows) + "\n")


def main():
    board = [EMPTY] * 9
    print("Tic-tac-toe! You are X, the AI is O. Pick a square 1-9.")
    while True:
        show(board)
        try:
            choice = input("Your move (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return
        if not choice.isdigit() or not 1 <= int(choice) <= 9 or board[int(choice) - 1] != EMPTY:
            print("Invalid move, try again.")
            continue
        board[int(choice) - 1] = HUMAN
        if winner(board) or is_full(board):
            break
        board[best_move(board)] = AI
        if winner(board) or is_full(board):
            break
    show(board)
    w = winner(board)
    print("You win! 🎉 (that should be impossible...)" if w == HUMAN
          else "AI wins! 🤖" if w == AI else "It's a draw! 🤝")


if __name__ == "__main__":
    main()
