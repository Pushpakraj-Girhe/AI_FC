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

================================ByBFS=========================================
from collections import deque

def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    return True

def missionaries_cannibals_bfs(start, goal):
    visited = set()
    queue = deque()
    queue.append((start, [start]))  # (current_state, path_taken)

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue
        
        print(f"Step: {path}")
        if current_state == goal:
            print("Solution found!")
            return True
        
        visited.add(current_state)

        m_left, c_left, boat, m_right, c_right = current_state
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        for m, c in moves:
            if boat == 1:
                new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
            else:
                new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
            
            if min(new_state) >= 0 and max(new_state) <= 3 and is_valid(new_state):
                if new_state not in visited:
                    queue.append((new_state, path + [new_state]))

    print("No solution found.")
    return False

# Initial and goal states
start = (3, 3, 1, 0, 0)
goal = (0, 0, 0, 3, 3)
print("Solving Missionaries and Cannibals Problem using BFS:")
missionaries_cannibals_bfs(start, goal)

