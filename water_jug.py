from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            print(f"Solution found: Jug1 = {jug1}, Jug2 = {jug2}")
            return True

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        queue.append((capacity1, jug2))
        queue.append((jug1, capacity2))
        queue.append((0, jug2))
        queue.append((jug1, 0))

        transfer = min(jug1, capacity2 - jug2)
        queue.append((jug1 - transfer, jug2 + transfer))

        transfer = min(jug2, capacity1 - jug1)
        queue.append((jug1 + transfer, jug2 - transfer))

    print("No solution found")
    return False

capacity1 = 4
capacity2 = 3
target = 2
water_jug_bfs(capacity1, capacity2, target)
