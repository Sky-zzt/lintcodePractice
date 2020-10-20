class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    '''

    https://www.jiuzhang.com/solutions/powx-n/
    '''

    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans


s = Solution()
print(s.myPow(2, -4))
