def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    return not ((m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0))

def missionaries_cannibals_game():
    state = (3, 3, 1, 0, 0)
    goal = (0, 0, 0, 3, 3)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    print("Welcome to the Missionaries and Cannibals Game!")
    print("You need to move all missionaries and cannibals safely to the other side.")
    
    while state != goal:
        print(f"Current state: Left({state[0]}M, {state[1]}C) | Boat: {'Left' if state[2] else 'Right'} | Right({state[3]}M, {state[4]}C)")
        print("Choose a move: (Missionaries, Cannibals)")
        for i, (m, c) in enumerate(moves, 1):
            print(f"{i}. Move {m} Missionary(ies) and {c} Cannibal(s)")
        print("6. Quit")
        
        choice = int(input("Enter your choice: "))
        if choice == 6:
            print("Game Over!")
            return
        
        if 1 <= choice <= 5:
            m, c = moves[choice - 1]
            if state[2] == 1:
                new_state = (state[0] - m, state[1] - c, 0, state[3] + m, state[4] + c)
            else:
                new_state = (state[0] + m, state[1] + c, 1, state[3] - m, state[4] - c)
            
            if min(new_state) >= 0 and max(new_state) <= 3 and is_valid(new_state):
                state = new_state
            else:
                print("Invalid move! Try again.")
        else:
            print("Invalid choice! Enter a number between 1-6.")
    
    print("Congratulations! You solved the puzzle!")

# Start the game
missionaries_cannibals_game()
