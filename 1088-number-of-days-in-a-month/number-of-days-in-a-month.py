class Solution(object):
    def numberOfDays(self, year, month):
        """
        :type year: int
        :type month: int
        :rtype: int
        """
        def is_leap_year(y):
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = days_in_month[month]
        if month == 2 and is_leap_year(year):
            days = 29
        return days
if __name__ == "__main__":
    sol = Solution()
    result1 = sol.numberOfDays(1992, 7)
    print('Input: year = 1992, month = 7')
    print('Output: {}'.format(result1))
    assert result1 == 31
    print('PASSED\n')
    result2 = sol.numberOfDays(2000, 2)
    print('Input: year = 2000, month = 2')
    print('Output: {}'.format(result2))
    assert result2 == 29
    print('PASSED\n')
    result3 = sol.numberOfDays(1900, 2)
    print('Input: year = 1900, month = 2')
    print('Output: {}'.format(result3))
    assert result3 == 28
    print('PASSED\n')
    assert sol.numberOfDays(2024, 2) == 29  
    assert sol.numberOfDays(2100, 2) == 28  
    assert sol.numberOfDays(2400, 2) == 29  
    assert sol.numberOfDays(2023, 4) == 30
    assert sol.numberOfDays(1583, 1) == 31  
    print('All extra edge case tests PASSED')
print(__name__)