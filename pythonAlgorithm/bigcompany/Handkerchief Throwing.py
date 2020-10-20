class Solution:
    """
    @param to: The target of everyone will throw the handkerchief to.
    @return: Return the number of turns the game will stop.

    有 n 个人正在玩丢手绢。编号为0, 1 ... n-10,。
一开始，每个人手上都拿着一块自己手绢。接下来的每一轮，第 i 个人会把当前手里的手绢丢给一个固定的人toi
​​  。
当有人重新拿到自己的手绢时，游戏就会结束。
请求出游戏会在第几轮结束。

Example
样例输入：
to = [1, 2, 0, 4, 3, 0]
样例输出：
2
Clarification
0, 1, 2,号都要经过三轮拿到自己的手绢，但 3, 4号只要两轮就能拿到自己的手绢，所以 2轮后游戏结束。

Notice
1 <= n <= 10^31<=n<=10
​3
​​
0 <= to_i <= n - 10<=to
​i
​​ <=n−1, to_ito
​i
​​  可能和 i 相等，即丢给自己。
保证游戏一定会结束。
    """

    def gameTurns(self, to):
        # write your code here,
        n = len(to)
        min_turn = n

        for i in range(n):
            position = i
            turn_count = 0
            visited = set()

            position = to[position]
            turn_count += 1
            while position != i:
                position = to[position]
                turn_count += 1
                # 如果到了已访问过的点，代表这个手绢进入了死循环，到不了出发点
                if position in visited:
                    break
                visited.add(position)

            # 只有回到出发点的，才算作有效的值
            if position == i:
                min_turn = min(min_turn, turn_count)

        return min_turn
