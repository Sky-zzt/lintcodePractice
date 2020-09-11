class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    '''
    看视频学一下
    '''
    def numDecodings(self, s):
        # write your code here
        if not s or s is None : return 0

        if (int(s[0])==0 and len(s)==1):
            return 0
        if '0' in s:return 0
        l=len(s)
        f=[0]*(l+1)
        f[0]=1
        f[1]=1
        #f[2]=1

        if len(s)>=2 and int(s[0:2])<=26 and int(s[0:2])!=10 :
            f[2]=2
        for i in range(2,l+1):
            f[i] = f[i - 1]
            if  int(s[i-2:i])<=26 and int(s[0:2])!=10 :
                f[i]=f[i]+f[i-2]
        return f[l]


s=Solution()
print(s.numDecodings("19261001"))

