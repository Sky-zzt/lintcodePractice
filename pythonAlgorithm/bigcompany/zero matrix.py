'''

给定一个非负二维矩阵MatrixMatrix，元素均大于等于0
问是否存在c行d列 元素都为0 的子矩阵

2 \leq n \leq 20002≤n≤2000
2 \leq m \leq 20002≤m≤2000
2 \leq c \leq 5002≤c≤500
2 \leq d \leq 5002≤d≤500
0 \leq Matrix[i][j] \leq 10 \quad 0 \leq i \leq n-1 \quad 0 \leq j \leq m-10≤Matrix[i][j]≤100≤i≤n−10≤j≤m−1
n为矩阵行数，m为矩阵列数

Have you met this question in a real interview?
Example
输入:[[0,0,0],[1,0,0]]
2
2
输出：true
你可以选择(0,1),(0,2),(1,1),(1,2) 这四个点

题目要求是否存在一个c行d列全零子矩阵，
又因为矩阵元素都是非负的
那一个子矩阵元素元素全是零的充要条件一个子矩阵所有元素相加得到的和是零
枚举子矩阵左上角位置，通过c行d列算出右下角位置 通过前缀和算出子矩阵的元素和，如果元素和为0，则是全零子矩阵
'''