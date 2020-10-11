class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        pass

    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True

        while num >= 2 and num % 2 == 0:
            num /= 2
        while num >= 3 and num % 3 == 0:
            num /= 3
        while num >= 5 and num % 5 == 0:
            num /= 5

        return num == 1
