def maxsubarrary(nums):
    s = set()
    import sys
    globalmax = -sys.maxsize
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1):
            for k in range(j + 1):
                s.add((k, j))
    return s


# [[6], [2], [1], [6, 2], [2, 1], [6, 2, 1]]

print(maxsubarrary([6, 2, 1]))
