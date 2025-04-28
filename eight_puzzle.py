import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.blank_pos = board.index(0)
        self.g = 0 if parent is None else parent.g + 1
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(abs((num % 3) - (goal.index(num) % 3)) + abs((num // 3) - (goal.index(num) // 3)) for num in self.board)

    def get_neighbors(self):
        neighbors = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = self.blank_pos // 3, self.blank_pos % 3
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                new_board = self.board[:]
                new_board[self.blank_pos], new_board[new_pos] = new_board[new_pos], new_board[self.blank_pos]
                neighbors.append(PuzzleState(new_board, self, (row, col, new_row, new_col)))
        return neighbors

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __lt__(self, other):
        return self.f < other.f

def a_star(start_board):
    start_state = PuzzleState(start_board)
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            solution = []
            while current_state:
                solution.append(current_state)
                current_state = current_state.parent
            return solution[::-1]

        closed_list.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in closed_list:
                heapq.heappush(open_list, neighbor)

    return None

def print_solution(solution):
    for state in solution:
        print(f"Move: {state.move}")
        for i in range(0, 9, 3):
            print(state.board[i:i+3])
        print()

start_board = [5, 1, 2, 0, 4, 3, 8, 7, 6]
solution = a_star(start_board)
if solution:
    print_solution(solution)
else:
    print("No solution found")
