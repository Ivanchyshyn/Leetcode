from collections import defaultdict


class Solution:
    """https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3717/ - Accepted"""

    def leastBricks(self, wall: list) -> int:
        if not wall or not wall[0]:
            return 0

        totals = defaultdict(int)
        for i, row in enumerate(wall):
            total = 0
            for j, num in enumerate(row[:-1]):
                total += num
                totals[total] += 1
        if not totals:
            return len(wall)
        return len(wall) - max(totals.values())


if __name__ == '__main__':
    solution = Solution()

    wall = [
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]
    ]
    assert solution.leastBricks(wall) == 2

    wall = [
        [1, 2, 2, 1],
        [1, 1, 2, 2],
    ]
    assert solution.leastBricks(wall) == 0

    wall = [[1], [1], [1]]
    assert solution.leastBricks(wall) == 3
