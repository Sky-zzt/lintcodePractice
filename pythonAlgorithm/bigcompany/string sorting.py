'''

给定一些由,隔开的字符串，请将他们按字典序排列。

- 字符串仅包含小写字母。 - 字符串数量$\leq 1\,000$且总长度$\leq 10^5$
样例
样例 1

输入: "bb,aa,lintcode,c"
输出: "aa,bb,c,lintcode"
说明: 在字典序中，"aa" < "bb" < "c" < "lintcode"

'''

a=['acad,','abc','abcd']

def sot(str):
    return (i for i in str)

print(sot('acd'))
a=sorted(a,key= lambda x:[x[0],x[2]])
print(a)