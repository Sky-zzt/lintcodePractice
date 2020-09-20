def maxsima(start, end, arr, m):
    # m1, m2=0,0
    #m.append(11)
    if end==len(arr): return
    if arr[start] < arr[end]:
        m.append(arr[end])
    else:
        m.append(arr[start])
    maxsima(start+1, end+1, arr, m)


def f(start, end, arr):
    res = []
    maxsima(start, end, arr, res)
    return res

m=[]
print(maxsima(0, 1, [1, 2, 3],m))
print(m)
