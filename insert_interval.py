class Solution:
    """https://leetcode.com/problems/insert-interval/"""

    def insert(self, intervals: list, newInterval: list) -> list:
        new_interval_min, new_interval_max = newInterval
        for i, interval in enumerate(intervals):
            val_min, val_max = interval
            if new_interval_min < val_min:
                # new interval start is lower than current interval start
                if new_interval_max < val_min:
                    # new interval end doesn't intersect with current interval
                    # so we add it in between and break cycle
                    intervals = intervals[:i] + [newInterval] + intervals[i:]
                    break
                # else we can change start and end of interval
                val_min = new_interval_min
                val_max = max(val_max, new_interval_max)
            elif val_min <= new_interval_min <= val_max:
                val_max = max(val_max, new_interval_max)
                interval[:] = [val_min, val_max]
                break
            interval[:] = [val_min, val_max]
        else:
            # if the cycle didn't encounter 'break'
            # then we didn't add it to our interval
            # so we need to add it now
            intervals.append(newInterval)

        result = [intervals[0]]
        for interval in intervals[1:]:
            last = result[-1]
            if interval[0] <= last[1]:
                # we merge current interval with previous
                # because it starts in between last interval two points
                last[1] = max(last[1], interval[1])
            else:
                result.append(interval)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2], [3, 10], [12, 16]
    ]
    assert solution.insert([], [5, 7]) == [[5, 7]]
    assert solution.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert solution.insert([[1, 5]], [2, 7]) == [[1, 7]]
    assert solution.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert solution.insert([[1, 5]], [0, 3]) == [[0, 5]]
    assert solution.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
    assert solution.insert([[1, 5]], [0, 6]) == [[0, 6]]
    assert solution.insert([[1, 5], [6, 8]], [0, 9]) == [[0, 9]]
    assert solution.insert([[3, 5], [12, 15]], [6, 6]) == [[3, 5], [6, 6], [12, 15]]
    assert solution.insert([[3, 5], [12, 15], [17, 20]], [6, 17]) == [[3, 5], [6, 20]]
