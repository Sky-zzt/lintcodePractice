import queue


class Solution:
    """
    @param elements: A list of recommended elements.
    @param n: [picture P] can appear at most 1 in every n
    @return: Return the scattered result.
    """

    def scatter(self, elements, n):
        # write your code here
        #  定义双队列，分别存储图片元素 P, 视频元素 V
        queueP = queue.Queue()
        queueV = queue.Queue()

        #  第 1 个图片 P 出现的位置
        firstP = -1
        for i in range(0, len(elements)):
            if elements[i][0] == 'P':
                #  第 1 个图片 P
                if firstP == -1:
                    firstP = i
                #  该元素加入 P 队列
                queueP.put(elements[i])
            else:
                #  该元素加入 V 队列
                queueV.put(elements[i])

        # 定义打散后的结果序列
        result = []

        # 将出现第 1 个 P 前的 V 元素存入结果序列
        while firstP > 0:
            firstP -= 1
            result.append(queueV.get())

        while queueP.empty() == False:
            #  每 n 个元素中需要恰好有 1 个 P
            result.append(queueP.get())

            # 辅助变量
            step = n

            # 将 n-1 个 V 元素存入结果序列
            while queueV.empty() == False and step > 1:
                result.append(queueV.get())
                step -= 1

            # 若当前已经无法满足打散要求，直接结束
            if step > 1:
                break

        return result
