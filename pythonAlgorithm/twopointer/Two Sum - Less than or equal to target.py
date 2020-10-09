'''


给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。

样例
例1:

输入: nums = [2, 7, 11, 15], target = 24.
输出: 5.
解释:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
排序后双指针即可
  public int twoSum5(int[] nums, int target) {
        // Write your code here
        if (nums == null || nums.length < 2)
            return 0;

        Arrays.sort(nums);
        int cnt = 0;
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int v = nums[left] + nums[right];
            if (v > target) {
                right --;
            } else {
                cnt += right - left;
                left ++; # todo
            }
        }
        return cnt;
    }
'''
