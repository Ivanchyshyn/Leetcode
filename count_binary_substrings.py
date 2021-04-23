class Solution:
    """https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/"""

    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0

        arr = [[s[0], 0]]
        for num in s:
            last = arr[-1]
            if num == last[0]:
                last[1] += 1
            else:
                arr.append([num, 1])

        total = 0
        for first, second in zip(arr, arr[1:]):
            total += min(first[1], second[1])
        return total


if __name__ == '__main__':
    solution = Solution()

    assert solution.countBinarySubstrings('00110011') == 6
    assert solution.countBinarySubstrings('10101') == 4
