class Solution:
    int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]

    def intToRoman(self, num: int) -> str:
        result = ''
        for val, roman in self.int_to_roman:
            times = num // val
            if not times:
                continue
            num %= val
            result += roman * times
        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.intToRoman(3) == 'III'
    assert solution.intToRoman(4) == 'IV'
    assert solution.intToRoman(9) == 'IX'
    assert solution.intToRoman(58) == 'LVIII'
    assert solution.intToRoman(1994) == 'MCMXCIV'
