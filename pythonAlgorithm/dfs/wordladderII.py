from collections import deque

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

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        indexes = self.build_indexes(dict)

        distance = self.bfs(end, indexes)

        results = []
        self.dfs(start, end, distance, indexes, [start], results)

        return results

    def build_indexes(self, dict):
        indexes = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = {word}
        return indexes

    def bfs(self, end, indexes):
        distance = {end: 0}
        queue = deque([end])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
        return distance

    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words

    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, indexes):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()