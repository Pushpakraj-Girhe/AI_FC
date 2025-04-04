def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    return True

def missionaries_cannibals_dfs(state, goal, visited, path):
    if state in visited:
        return False
    
    print(f"Step: {path + [state]}")
    
    if state == goal:
        print("Solution found!")
        return True
    
    visited.add(state)
    path.append(state)
    m_left, c_left, boat, m_right, c_right = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for m, c in moves:
        if boat == 1:
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
        else:
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
        
        if min(new_state) >= 0 and max(new_state) <= 3 and is_valid(new_state):
            if missionaries_cannibals_dfs(new_state, goal, visited, path.copy()):
                return True
    
    return False

# Initial and goal states
start = (3, 3, 1, 0, 0)
goal = (0, 0, 0, 3, 3)
print("Solving Missionaries and Cannibals Problem using DFS:")
missionaries_cannibals_dfs(start, goal, set(), [])
