class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    很容易想到的方法是：从1起检验每个数是否为丑数，直到找到n个丑数为止。但是随着n的增大，绝大部分数字都不是丑数，
    我们枚举的效率非常低。因此，换个角度思考，如果我们只生成丑数，且生成n个，这道题就迎刃而解。
不难发现生成丑数的规律：如果已知丑数ugly，那么ugly * 2，ugly * 3和ugly * 5也都是丑数。
既然求第n小的丑数，可以采用最小堆来解决。每次弹出堆中最小的丑数，然后检查它分别乘以2、3和 5后的数是否生成过，
如果是第一次生成，那么就放入堆中。第n个弹出的数即为第n小的丑数。

https://blog.csdn.net/chandelierds/article/details/91357784
    """

    def nthUglyNumber(self, n):
        # write your code here
        import heapq
        heap=[]
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        curr_ugly = 1

        for _ in range(n):
            # 每次弹出当前最小丑数
            curr_ugly = heapq.heappop(heap)
            # 生成新的丑数
            for f in factors:
                new_ugly = curr_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly

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
