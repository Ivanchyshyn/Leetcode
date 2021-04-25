class Solution:
    """https://leetcode.com/problems/3sum/"""

    def threeSum(self, nums: list) -> list:
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()
        for i, target in enumerate(nums):
            need_nums = {}
            for j, num in enumerate(nums[i+1:]):
                if num in need_nums:
                    result.add(tuple([nums[i], need_nums[num], num]))
                need_nums[-target - num] = num

        return [list(vals) for vals in result]


if __name__ == '__main__':
    solution = Solution()

    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum([]) == []
    assert solution.threeSum([0]) == []
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([0, 0, 0, 1, 2]) == [[0, 0, 0]]
    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
