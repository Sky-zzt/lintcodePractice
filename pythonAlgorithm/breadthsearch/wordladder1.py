class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        from queue import Queue
        dict.append('cog')  # todo 必须将end加入dict
        q = Queue()
        q.put(start)
        s = set()
        s.add(start)
        length = 0
        while q.qsize() != 0:
            length += 1
            size = q.qsize()
            for i in range(size):
                word = q.get()
                if word == end:
                    return length
                words = self.getNextWords(word, dict)
                for j in words:
                    if j in s: continue
                    q.put(j)
                    s.add(j)
        return length

    def getNextWords(self, word, dict):
        res = []
        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in range(len(word)):
                if word[j] == i: continue
                #  word = word.replace(word[j], i)  todo it is big wrong
                newword = word.replace(word[j], i)
                if newword in dict:
                    res.append(newword)
        return res


s = Solution()
print(s.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
#
# ss='1,2'
# ss=ss.replace(ss[1],'e')
# print(ss)
