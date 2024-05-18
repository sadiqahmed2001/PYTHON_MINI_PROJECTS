import random

class SudokuSolver:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]

    def generate_sudoku(self):
        # Fill the diagonal 3x3 subgrids
        for i in range(0, 9, 3):
            self.fill_subgrid(i, i)

        # Solve the puzzle
        self.solve_sudoku()

    def fill_subgrid(self, row, col):
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(digits)
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = digits.pop()

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Puzzle solved
        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku():
                    return True
                self.grid[row][col] = 0  # Backtrack

        return False  # No solution found

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None  # No empty cell found

    def is_valid_move(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False
        # Check column
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def display_sudoku(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

def main():
    print("Welcome to the Sudoku Solver!")

    solver = SudokuSolver()
    solver.generate_sudoku()

    print("\nGenerated Sudoku Puzzle:")
    solver.display_sudoku()

    print("\nSolving Sudoku Puzzle...")
    solver.solve_sudoku()

    print("\nSolved Sudoku Puzzle:")
    solver.display_sudoku()

if __name__ == "__main__":
    main()
