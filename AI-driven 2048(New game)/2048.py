import random
import copy


class AI2048:
    def __init__(self, board):
        self.board = board

    def get_empty_cells(self):
        empty_cells = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def get_max_tile(self):
        return max(map(max, self.board))

    def move_left(self):
        merged = []
        for row in self.board:
            new_row = [tile for tile in row if tile != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
                    merged.append(new_row[i])
            new_row = [tile for tile in new_row if tile != 0]
            new_row.extend([0] * (len(row) - len(new_row)))
            self.board[self.board.index(row)] = new_row
        return merged

    def move_right(self):
        self.flip_board()
        merged = self.move_left()
        self.flip_board()
        return merged

    def move_up(self):
        self.transpose_board()
        merged = self.move_left()
        self.transpose_board()
        return merged

    def move_down(self):
        self.transpose_board()
        merged = self.move_right()
        self.transpose_board()
        return merged

    def get_score(self):
        return sum(map(sum, self.board))

    def get_heuristic_score(self):
        max_tile = self.get_max_tile()
        empty_cells = len(self.get_empty_cells())
        smoothness = self.calculate_smoothness()
        monotonicity = self.calculate_monotonicity()

        # Weighted sum of different heuristics
        return 0.1 * self.get_score() + 2.7 * empty_cells + 1.0 * smoothness + 1.5 * monotonicity + 3.0 * max_tile

    def calculate_smoothness(self):
        smoothness = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    value = math.log2(self.board[i][j])
                    for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < len(self.board) and 0 <= y < len(self.board[i]) and self.board[x][y] != 0:
                            neighbor_value = math.log2(self.board[x][y])
                            smoothness -= abs(value - neighbor_value)
        return smoothness

    def calculate_monotonicity(self):
        monotonicity = [0, 0, 0, 0]
        for i in range(len(self.board)):
            current = 0
            next = current + 1
            while next < 4:
                while next < 4 and self.board[i][next] == 0:
                    next += 1
                if next >= 4:
                    next -= 1
                current_value = 0 if self.board[i][current] == 0 else math.log2(
                    self.board[i][current])
                next_value = 0 if self.board[i][next] == 0 else math.log2(
                    self.board[i][next])
                if current_value > next_value:
                    monotonicity[0] += next_value - current_value
                elif next_value > current_value:
                    monotonicity[1] += current_value - next_value
                current = next
                next += 1

        for j in ra
