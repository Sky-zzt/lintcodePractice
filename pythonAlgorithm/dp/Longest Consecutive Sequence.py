'''

算法： 1. 把所有元素放入哈希表。 2. 遍历哈希表，对每个元素依次值加（减）一，并检查是否在哈希表中。如果存在，移出哈希表。
func longestConsecutive (nums []int) int {
    // write your code here
    m := make(map[int]bool)
	for _, v := range nums {
		m[v] = true
	}
	res, down, up := 1, 0, 0
	for k := range m {
		for i := k + 1; m[i]; i++ {
			up++
			delete(m, i)
		}
		for i := k - 1; m[i]; i-- {
			down++
			delete(m, i)
		}
		delete(m, k)
		if 1+up+down > res {
			res = 1 + up + down
		}
		down, up = 0, 0 // important
	}

	return res
}
'''
