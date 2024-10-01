def show_arr(arr):
    print("Current board:")
    for row in arr:
        print(" | ".join(cell if cell != "" else " " for cell in row))
        print("-" * 9)

def is_cell_empty(arr, row, col):
    return arr[row][col] == ""

def wincheck(arr):
    # Check rows
    for row in arr:
        if row[0] == row[1] == row[2] and row[0] != "":
            return "Win"
    
    # Check columns
    for col in range(3):
        if arr[0][col] == arr[1][col] == arr[2][col] and arr[0][col] != "":
            return "Win"
    
    # Check diagonals
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != "":
        return "Win"
    if arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] != "":
        return "Win"
    
    return "Not win"

def is_draw(arr):
    return all(cell != "" for row in arr for cell in row)

def tictactoe():
    arr = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    
    while True:
        show_arr(arr)
        print(f"Player {players[current_player]}'s turn.")
        
        # Get player input
        move = -1
        while move < 0 or move > 8:
            move_input = input("Enter your move (1-9): ")
            if move_input.isdigit():
                move = int(move_input) - 1
                row, col = divmod(move, 3)
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Invalid move. Please enter a number between 1 and 9.")
                elif not is_cell_empty(arr, row, col):
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")

        # Make the move
        arr[row][col] = players[current_player]

        # Check for a win
        if wincheck(arr) == "Win":
            show_arr(arr)
            print(f"Player {players[current_player]} wins!")
            break
        
        # Check for a draw
        if is_draw(arr):
            show_arr(arr)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 1 - current_player

if __name__ == "__main__":
    tictactoe()
