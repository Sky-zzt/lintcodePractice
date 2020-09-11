class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        n=len(nums)
        f=[[0]*(target+1) for _ in range(n)]
        '''
     这种要求正整数且 形参中一个是数字的，建议用 序列型的做，好做 也好解释
     两个都是数组左边的就用坐标型就很简单
     
     
     
     
        • 􃔉􁇊N个正整数：A0,A1, …, AN-1
        • 一个正整数Target
        • 求有多少种􃓴􀨸􀣐􄎧􁶕􁱟Target
        • 每个Ai只能用一次
        
        f[i][w] = 用前i个物品有多少种方式拼出重量w
        用作表型的写法忙碌这么久的问题在于f[0][0]=1，没有她就不对，可是f[i][j]中的i我是用坐标型的，j是按序列型的，
        那么这个f[0][0]=0 
        因为是正整数，还是 都用序列型的好解释，不然这个f[0][0]=1，着呢们解释呢。按理来说应该等于0 但是等于1
        '''
        #有1种组合能拼出0 （就是什么都不选）
        f[0][0]=1
        for i in range(target+1):
            if i==nums[0]:f[0][i]=1
        for i in range(n):
            if 0 == nums[i]: f[i][0] = 1

            
        for i in range(1,n):
            for j in range(target+1):
                #f[i][j] = f[i - 1][j]
                if j-nums[i]>=0:
                    f[i][j]=f[i-1][j]+f[i-1][j-nums[i]]
                else:
                    f[i][j] = f[i - 1][j]
        return f[n-1][target]
s=Solution()
print(s.backPackV([1,1,1,2], 4))
print(s.backPackV([1, 2, 3, 3, 7], 7))
print(s.backPackV([0],0))