from queue import Queue

def ac3(csp):
    """Executa o algoritmo AC-3 em um CSP dado."""
    queue = Queue()
    for arc in csp.constraints:
        queue.put(arc)
    while not queue.empty():
        (xi, xj) = queue.get()
        if revise(csp, xi, xj):
            if len(csp.domains[xi]) == 0:
                return False
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.put((xk, xi))
    return True

def revise(csp, xi, xj):
    """Revisa o domínio de xi para satisfazer a restrição entre xi e xj."""
    revised = False
    for x in csp.domains[xi]:
        if not any([csp.is_satisfied(x, y) for y in csp.domains[xj]]):
            csp.domains[xi].remove(x)
            revised = True
    return revised

class Sudoku:
    """Classe que representa um problema de Sudoku como um CSP."""
    def __init__(self, board):
        self.variables = [(row, col) for row in range(9) for col in range(9)]
        self.domains = {}
        self.constraints = []
        self.neighbors = {}
        for var in self.variables:
            row, col = var
            if board[row][col] == 0:
                self.domains[var] = [i for i in range(1, 10)]
            else:
                self.domains[var] = [board[row][col]]
            self.neighbors[var] = []
        for var in self.variables:
            row, col = var
            for i in range(9):
                if i != col:
                    self.constraints.append((var, (row, i)))
                    self.neighbors[var].append((row, i))
                if i != row:
                    self.constraints.append((var, (i, col)))
                    self.neighbors[var].append((i, col))
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if i != row and j != col:
                        self.constraints.append((var, (i, j)))
                        self.neighbors[var].append((i, j))

    def is_satisfied(self, x, y):
        """Verifica se a restrição entre x e y é satisfeita."""
        return x != y

def solve_sudoku(board):
    """Resolve um problema de Sudoku usando o algoritmo AC-3."""
    csp = Sudoku(board)
    ac3(csp)
    for row in range(9):
        for col in range(9):
            if len(csp.domains[(row,col)]) == 1:
                board[row][col] = csp.domains[(row,col)][0]
    return board

board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0],
]
solved_board = solve_sudoku(board)
for row in solved_board:
    print(row)
