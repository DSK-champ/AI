import heapq


class UniformCostSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != -1

    def ucs(self, start, target):
        pq = []  # priority queue
        heapq.heappush(pq, (self.grid[start[0]][start[1]], start))

        cost_so_far = {start: self.grid[start[0]][start[1]]}

        while pq:
            current_cost, (x, y) = heapq.heappop(pq)

            if (x, y) == target:
                return current_cost

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if self.is_valid(nx, ny):
                    new_cost = current_cost + self.grid[nx][ny]

                    if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                        cost_so_far[(nx, ny)] = new_cost
                        heapq.heappush(pq, (new_cost, (nx, ny)))

        return float("inf")  # if unreachable


# Example Grid (cost grid)
grid = [
    [1, 1, 2, -1, 3],
    [2, 3, -1, 4, 2],
    [1, 1, 1, 2, -1],
    [3, -1, -1, 1, 1],
    [2, 2, 1, 1, 1],
]

ucs_solver = UniformCostSearch(grid)

start = (0, 0)
target = (4, 4)

result = ucs_solver.ucs(start, target)

if result != float("inf"):
    print("Minimum cost to reach target:", result)
else:
    print("Target not reachable.")
