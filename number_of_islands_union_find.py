from collections import defaultdict


class Cell:
    def __init__(self, num, size, marked=False):
        self.num = num
        self.size = size
        self.marked = marked

    def __str__(self):
        return str(self.num)

    def __eq__(self, other):
        if isinstance(other, Cell):
            other = other.num
        return self.num == other

    def __repr__(self):
        return 'Cell({}, {}, {})'.format(self.num, self.size, self.marked)


class UnionFind:
    def __init__(self, rows, cols):
        self.matrix = []

        count = 0
        for i in range(rows):
            for j in range(cols):
                self.matrix.append(Cell(count, 1))
                count += 1

    def root(self, i):
        while self.matrix[i] != i:
            self.matrix[i].num = self.matrix[self.matrix[i].num].num
            i = self.matrix[i].num
        return self.matrix[i]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        first = self.root(p)
        second = self.root(q)
        if first == second:
            return

        if first.size < second.size:
            self.matrix[first.num].num = second.num
            second.size += first.size
        else:
            self.matrix[second.num].num = first.num
            first.size += second.size

    def mark(self, i):
        self.matrix[i].marked = True

    def is_marked(self, i):
        return self.matrix[i].marked

    def root_to_cells(self):
        num_to_cells = defaultdict(list)
        for i in range(len(self.matrix)):
            res = self.root(self.matrix[i].num)
            num_to_cells[res.num].append(res)
        return num_to_cells


class Solution:
    """https://leetcode.com/problems/number-of-islands/  - Accepted"""

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows, cols)
        for i, row in enumerate(grid):
            prev = None
            for j, num in enumerate(row):
                if num == '1':
                    res = i * cols + j
                    uf.mark(res)
                    if prev is not None:
                        uf.union(prev, res)
                    if i > 0 and grid[i - 1][j] == '1':
                        prev_row_res = (i - 1) * cols + j
                        uf.union(prev_row_res, res)
                    prev = res
                else:
                    prev = None
        num_to_cells = uf.root_to_cells()
        islands = 0
        for val, cells in num_to_cells.items():
            if len(cells) > 1:
                islands += 1
            elif uf.is_marked(val):
                islands += 1
        return islands


if __name__ == '__main__':
    solution = Solution()

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.numIslands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution.numIslands(grid) == 3

    grid = [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"]
    ]
    assert solution.numIslands(grid) == 1
