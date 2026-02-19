class GridSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    # Depth Limited Search
    def dls(self, x, y, target, depth, visited):
        if depth < 0:
            return False

        if (x, y) == target:
            return True

        if depth == 0:
            return False

        visited.add((x, y))

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy

            if self.is_valid(nx, ny) and (nx, ny) not in visited:
                if self.dls(nx, ny, target, depth - 1, visited):
                    return True

        visited.remove((x, y))  # backtrack
        return False

    # Iterative Deepening DFS
    def iddfs(self, start, target, max_depth):
        for depth in range(max_depth + 1):
            print(f"Searching at depth: {depth}")
            visited = set()
            if self.dls(start[0], start[1], target, depth, visited):
                return True
        return False


# Example Usage
grid = [
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

search = GridSearch(grid)

start = (0, 0)
target = (4, 4)
max_depth = 10

found = search.iddfs(start, target, max_depth)

if found:
    print("Target found.")
else:
    print("Target not found within depth limit.")
