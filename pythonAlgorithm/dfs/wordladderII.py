"""
从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。 
然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

这里寻找下一个变换单词的方法是建立 index，即，如果有一个单词 abc，分别去掉第1,2,3个字符之后，
把 abc 这个单词分别扔进 %bc, a%c, ab% 这三个不同的 key 的 hash 里。hash 里的 key 是去掉一个字符之后的 pattern，value 是一个 set，
保存满足这个 pattern 的所有单词。
"""


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string

    """

    # todo     可以start-》end bfs，然后dfs，也可以，end-》start，bfs，然后，start-》end dfs
    # 图上 a->B 有多少种路径/打印所有路径---回溯的dfs  有多少种路径也可以dp做
    ##
    '''
    图上的dfs 遍历
        public static void dfs(Node node,HashSet<Node> set) {
        set.add(node);
        System.out.println(node.value);
        for (Node next : node.nexts) {
            if (!set.contains(next)) {
                dfs(next,set);
            }
        }
    }
    
    对比看 dfs的写法，结束条件等，树也是dfs遍历的，树也可以 for (Node next : node.nexts):只不过树只有 left和right，所以不用for 直接写 而图不确定有几个next

    一般求具体方案的，因为你已经把这个方案放进去了，所以，递归的时候需要回溯，就是把这个方案再拿出来呗
   
    '''

    def findLadders(self, start, end, dict):
        dict.add(end)
        ladder = []
        path = []
        map = {}
        distance = {}
        self.bfs(start, end, dict, map, distance)
        self.dfs(ladder, path, start, map, distance, end)

    def dfs(self, ladder, path, crt, map, distance, end):
        path.append(crt)
        if crt == end:
            ladder.append(path)
        else:
            for next in map.get(crt):
                if distance.get(next) == distance.get(crt) + 1:
                    self.dfs(ladder, path, next, map, distance, end)
        path.pop()

    def bfs(self, start, end, dict, map, distance):
        from queue import Queue
        q = Queue()
        q.put(start)
        distance.update({start: 0})
        for i in dict:
            map.update({i: []})

        while q.qsize() != 0:
            size = q.qsize()
            for i in range(size):
                ele = q.get()
                words = self.getNextWords(ele, dict)
                for w in words:
                    map.get(ele).append(w)
                    if w not in distance: distance.update({w: distance.get(ele) + 1})  # todo 图的遍历要去重 基本 的知识点
                    q.put(w)

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
s.findLadders('a', 'c', {"a", "b", "c"})
