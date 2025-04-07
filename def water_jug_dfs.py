def water_jug_dfs(jug1, jug2, target, visited=set()):
    print(f"Current state: ({jug1}, {jug2})")
    
    if (jug1, jug2) in visited:
        return False
    
    if jug1 == target or jug2 == target:
        print(f"Solution found: ({jug1}, {jug2})")
        return True
    
    visited.add((jug1, jug2))
    
    return (
        water_jug_dfs(4, jug2, target, visited) or  # Fill Jug1
        water_jug_dfs(jug1, 3, target, visited) or  # Fill Jug2
        water_jug_dfs(0, jug2, target, visited) or  # Empty Jug1
        water_jug_dfs(jug1, 0, target, visited) or  # Empty Jug2
        water_jug_dfs(min(jug1 + jug2, 4), max(0, jug1 + jug2 - 4), target, visited) or  # Pour Jug2 -> Jug1
        water_jug_dfs(max(0, jug1 + jug2 - 3), min(jug1 + jug2, 3), target, visited)  # Pour Jug1 -> Jug2
    )

# Example usage
//corrected::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def water_jug_dfs(jug1, jug2, target, visited=set()):
    print(f"Current state: ({jug1}, {jug2})")
    
    if (jug1, jug2) in visited:
        return False
    
    if jug1 == target or jug2 == target:
        print(f"Solution found: ({jug1}, {jug2})")
        return True
    
    visited.add((jug1, jug2))

    # Calculate pour amounts safely
    pour_to_jug1 = min(jug2, 4 - jug1)
    pour_to_jug2 = min(jug1, 3 - jug2)
    
    return (
        water_jug_dfs(4, jug2, target, visited) or  # Fill Jug1
        water_jug_dfs(jug1, 3, target, visited) or  # Fill Jug2
        water_jug_dfs(0, jug2, target, visited) or  # Empty Jug1
        water_jug_dfs(jug1, 0, target, visited) or  # Empty Jug2
        water_jug_dfs(jug1 + pour_to_jug1, jug2 - pour_to_jug1, target, visited) or  # Pour Jug2 -> Jug1
        water_jug_dfs(jug1 - pour_to_jug2, jug2 + pour_to_jug2, target, visited)  # Pour Jug1 -> Jug2
    )
    
jug1_capacity = 4
jug2_capacity = 3
target = 2
print("Solving Water Jug Problem using DFS:")
water_jug_dfs(0, 0, target)

jug1_capacity = 4
jug2_capacity = 3
target = 2
print("Solving Water Jug Problem using DFS:")
water_jug_dfs(0, 0, target)


===================ByBFS========================
from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Initial state
    queue.append((0, 0))  # (jug1, jug2)

    while queue:
        jug1, jug2 = queue.popleft()
        print(f"Current state: ({jug1}, {jug2})")

        # If target is reached
        if jug1 == target or jug2 == target:
            print(f"Solution found: ({jug1}, {jug2})")
            return True

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # All possible next states
        next_states = [
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution found.")
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
print("Solving Water Jug Problem using BFS:")
water_jug_bfs(jug1_capacity, jug2_capacity, target)

