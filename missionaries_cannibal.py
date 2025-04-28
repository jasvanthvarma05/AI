from collections import deque

def is_valid(state):
    m1, c1, m2, c2, boat = state
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    if m1 > 0 and m1 < c1:
        return False
    if m2 > 0 and m2 < c2:
        return False
    return True

def get_successors(state):
    m1, c1, m2, c2, boat = state
    moves = []
    if boat == 1:
        directions = [(-2, 0), (-1, -1), (0, -2), (-1, 0), (0, -1)]
    else:
        directions = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1)]
    for dm, dc in directions:
        new_state = (m1 + dm, c1 + dc, m2 - dm, c2 - dc, 1 - boat)
        if is_valid(new_state):
            moves.append(new_state)
    return moves

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for successor in get_successors(state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))
    return None

def display_solution(solution):
    for step in solution:
        print(f"Left Bank -> Missionaries: {step[0]}, Cannibals: {step[1]} | "
              f"Right Bank -> Missionaries: {step[2]}, Cannibals: {step[3]} | "
              f"Boat: {'Left' if step[4] == 1 else 'Right'}")

start = (3, 3, 0, 0, 1)
goal = (0, 0, 3, 3, 0)
solution = bfs(start, goal)
if solution:
    display_solution(solution)
else:
    print("No solution found")
