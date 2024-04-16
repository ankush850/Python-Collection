import heapq
import random


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)

    def get_neighbors(self, node):
        row, col = node
        neighbors = []
        if row > 0 and not self.maze[row - 1][col]:
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and not self.maze[row + 1][col]:
            neighbors.append((row + 1, col))
        if col > 0 and not self.maze[row][col - 1]:
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and not self.maze[row][col + 1]:
            neighbors.append((row, col + 1))
        return neighbors

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def solve(self):
        open_set = []
        closed_set = set()
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}
        heapq.heappush(open_set, (f_score[self.start], self.start))

        while open_set:
            _, current = heapq.heappop
