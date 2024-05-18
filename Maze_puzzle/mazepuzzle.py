import random

class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[1] * cols for _ in range(rows)]

    def generate_maze(self):
        def dfs(row, col):
            self.maze[row][col] = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions)
            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.maze[new_row][new_col]:
                    self.maze[row + drow // 2][col + dcol // 2] = 0
                    dfs(new_row, new_col)

        dfs(0, 0)

    def display_maze(self):
        for row in self.maze:
            print(' '.join('#' if cell else ' ' for cell in row))

def main():
    print("Welcome to the Maze Generator!")

    # Input maze dimensions from the user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create a MazeGenerator instance and generate the maze
    generator = MazeGenerator(rows, cols)
    generator.generate_maze()

    # Display the generated maze
    print("\nHere's your randomly generated maze:")
    generator.display_maze()

if __name__ == "__main__":
    main()
