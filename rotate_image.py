"""
3 x 3
2,0   0,2  -2, 0   0,-2
1,1  -1,1  -1,-1   1,-1


4 x 4
1 circle - start 0,0
3,0   0,3  -3, 0   0,-3
2,1  -1,2  -2,-1   1,-2
1,2  -2,1  -1,-2   2,-1
2 circle - start 1,1
1,0   0,1  -1, 0   0,-1
"""


class Solution:
    """https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3720/"""

    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # My solution - keep rotating the circles from outermost to innermost.
        # Every circle rotate each value to its correct position
        # After 4 rotations every value will be in its correct position.
        for border_counter in range(len(matrix) // 2):
            # inner circle always has 2 less cells
            lo, hi = 0, len(matrix) - 2 * border_counter - 1
            # we have to go through num_of_cell length - 1
            # cause last one was already changed and in needed place
            for counter in range(hi):
                # x - how much to go right (or left if x negative)
                # y - how much to go down (or up if y negative)
                x, y = hi - counter, lo + counter
                i, j = border_counter, border_counter + counter
                # Save in temp where we start
                temp = matrix[i][j]
                for _ in range(4):
                    i, j = y + i, x + j
                    matrix[i][j], temp = temp, matrix[i][j]
                    x, y = -y, x


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
