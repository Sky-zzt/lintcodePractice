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
        q = Queue()
        q.put(start)
        s = set()
        s.add(start)
        length = 0
        while q:
            length += 1
            size = len(q)
            for i in range(size):
                word = q.get()
                if word == end:
                    return length
                words = self.getNextWords(word, dict)
                for j in words:
                    q.put(j)

    def getNextWords(self, word, dict):
        res = []
        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in range(len(word)):
                if word[j] == i: continue
                word = word.replace(word[j], i)
                if word in dict:
                    res.append(word)
        return res


from queue import Queue

q = Queue()

print(q.qsize())
print(len(q))
