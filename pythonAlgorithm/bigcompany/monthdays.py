class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """
        # todo 学习写法 优雅
    def getTheMonthDays(self, year, month):
        NORMAL_YEAR = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        LEAP_YEAR = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if month == 2 and self.isLeapYear(year):
            return LEAP_YEAR[month]
        else:
            return NORMAL_YEAR[month]

    def isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0