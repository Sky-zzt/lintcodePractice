class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)

    给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。
    """

    def twoSum(self, numbers, target):
        # write your code here

        numbers = sorted(numbers)
        i, j = 0, len(numbers) - 1
        while i < j:
            if target == numbers[i] + numbers[j]:
                return [i, j]
            if target > numbers[i] + numbers[j]:
                i += 1
            if target < numbers[i] + numbers[j]:
                j -= 1
        return -1

    # todo 用hashmap 这个很妙 先想想怎们做，再看  上面是Onlogn 这个是 On的 上面那个如果想返货index ，可以记录一下排序前后的index
    def twosum(self, numbers, target):

        # write your code here
        hashmap={}
        for i  in  range(len(numbers)):
            if target-numbers[i] in  hashmap:
                return [hashmap.get(target-numbers[i]),i]
            hashmap.update({numbers[i]:i})
        return -1


s = Solution()
print(s.twosum([1,1,2,45,46,46],47))


