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
jug1_capacity = 4
jug2_capacity = 3
target = 2
print("Solving Water Jug Problem using DFS:")
water_jug_dfs(0, 0, target)
