def water_jug_game(jug1_capacity, jug2_capacity, target):
    jug1, jug2 = 0, 0
    
    print("Welcome to the Water Jug Game!")
    print(f"Jug1 Capacity: {jug1_capacity}, Jug2 Capacity: {jug2_capacity}, Target: {target}\n")
    
    while jug1 != target and jug2 != target:
        print(f"Current state: ({jug1}, {jug2})")
        print("Choose an action:")
        print("1. Fill Jug1")
        print("2. Fill Jug2")
        print("3. Empty Jug1")
        print("4. Empty Jug2")
        print("5. Pour Jug1 -> Jug2")
        print("6. Pour Jug2 -> Jug1")
        print("7. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            jug1 = jug1_capacity
        elif choice == 2:
            jug2 = jug2_capacity
        elif choice == 3:
            jug1 = 0
        elif choice == 4:
            jug2 = 0
        elif choice == 5:
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
        elif choice == 6:
            transfer = min(jug2, jug1_capacity - jug1)
            jug2 -= transfer
            jug1 += transfer
        elif choice == 7:
            print("Game Over!")
            return
        else:
            print("Invalid choice, try again.")
            continue
        
        if jug1 == target or jug2 == target:
            print(f"Solution found: ({jug1}, {jug2})")
            return
    
    print("No solution found.")

# Start the game
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_game(jug1_capacity, jug2_capacity, target)
