class Solution:
    """https://leetcode.com/discuss/interview-question/356433/"""

    def min_diff(self, loads):
        """0/1 Knapsack problem - Dynamic programming"""

        total = sum(loads)
        max_weight = total // 2
        row_length, col_length = len(loads), max_weight + 1
        dp = [[0 for _ in range(col_length)] for _ in range(row_length)]
        dp[0] = [loads[0] if i >= loads[0] else 0 for i in range(col_length)]
        for i in range(1, row_length):
            load = loads[i]
            for j in range(col_length):
                if j < load:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-load] + load)

        return total - 2 * dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    assert solution.min_diff([1, 2, 3, 4, 5]) == 1
    assert solution.min_diff([10, 10, 9, 9, 2]) == 0
    assert solution.min_diff([1, 2, 3, 10]) == 4
    assert solution.min_diff([2, 9, 10]) == 1
