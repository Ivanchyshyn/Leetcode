class Solution:
    def total_occurrences(self, nums, k):
        if not nums:
            return 0

        first_index = self.binary_search(nums, k)
        if first_index == -1:
            return 0
        last_index = self.binary_search(nums, k, is_first=False)
        return last_index - first_index + 1

    def binary_search(self, nums, k, is_first=True):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == k:
                if is_first:
                    if mid == 0:
                        return mid
                    if nums[mid - 1] == k:
                        hi = mid - 1
                    else:
                        return mid
                else:
                    if mid == len(nums) - 1:
                        return mid
                    if nums[mid + 1] == k:
                        lo = mid + 1
                    else:
                        return mid

            elif nums[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()

    assert solution.total_occurrences([1, 1, 1, 2, 3], 1) == 3
    assert solution.total_occurrences([1, 2, 3, 4, 5], 3) == 1
    assert solution.total_occurrences([], 1) == 0
    assert solution.total_occurrences([5, 7, 7, 8, 8, 10], 8) == 2
