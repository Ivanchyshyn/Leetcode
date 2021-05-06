class Solution:
    """https://leetcode.com/problems/regular-expression-matching/submissions/"""

    def isMatch(self, string: str, pattern: str, i=0, j=0) -> bool:
        if pattern == string:
            return True
        if j >= len(pattern):
            return not string[i:]
        if not string:
            return pattern[-1] == '*' and all(x == '*' for x in pattern[j + 1::2])

        star_index = pattern.find('*', j)
        if star_index == -1:
            return self.match_without_star(string, pattern, i, j)

        first_match = self.match_without_star(string, pattern, i, j, stop=star_index-1)
        i, j = i + star_index - 1 - j, star_index + 1
        return first_match and (
            self.isMatch(string, pattern, i, j) or
            self.check_is_in(pattern, string, i, j-2) and self.isMatch(string, pattern, i+1, j-2)
        )

    def match_without_star(self, string, pattern, i, j, stop=None):
        if stop is None:
            if not len(string) - i == len(pattern) - j:
                return False
            stop = len(pattern)

        while j < stop:
            if not self.check_is_in(pattern, string, i, j):
                return False
            i += 1
            j += 1
        return True

    def check_is_in(self, pattern, string, i, j):
        try:
            return pattern[j] in (string[i], '.')
        except IndexError:
            return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.isMatch('aaa', 'ab*ac*a')
    assert solution.isMatch('aaa', 'a.a')
    assert solution.isMatch('aaab', 'a.a.')
    assert not solution.isMatch('aa', 'a')
    assert solution.isMatch('aa', 'a*')
    assert solution.isMatch('aab', 'c*a*b')
    assert solution.isMatch('ab', '.*')
    assert not solution.isMatch('mississippi', 'mis*is*p*.')
    assert solution.isMatch('mississippi', 'mis*is*ip*.')
    assert not solution.isMatch('ab', 'abc')
    assert solution.isMatch('aaa', 'a*a')
    assert not solution.isMatch("ab", ".*c")
    assert not solution.isMatch("a", "ab*a")
    assert solution.isMatch("aa", "ab*a")
    assert solution.isMatch("abbbbba", "ab*a")
    assert solution.isMatch("", ".*")
    assert not solution.isMatch("ad", "a*b*c*")
