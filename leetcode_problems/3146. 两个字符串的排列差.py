"""
给你两个字符串 s 和 t，每个字符串中的字符都不重复，且 t 是 s 的一个排列。
排列差 定义为 s 和 t 中每个字符在两个字符串中位置的绝对差值之和。
返回 s 和 t 之间的 排列差 。

示例 1：
输入：s = "abc", t = "bac"
输出：2
解释：
对于 s = "abc" 和 t = "bac"，排列差是：
"a" 在 s 中的位置与在 t 中的位置之差的绝对值。
"b" 在 s 中的位置与在 t 中的位置之差的绝对值。
"c" 在 s 中的位置与在 t 中的位置之差的绝对值。
即，s 和 t 的排列差等于 |0 - 1| + |2 - 2| + |1 - 0| = 2。

示例 2：
输入：s = "abcde", t = "edbac"
输出：12
解释： s 和 t 的排列差等于 |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12。

提示：
1 <= s.length <= 26
每个字符在 s 中最多出现一次。
t 是 s 的一个排列。
s 仅由小写英文字母组成。
"""


class Solution(object):
    """
    该类提供了一个静态方法来计算两个字符串排列之间的差异。
    """

    @staticmethod
    def findPermutationDifference(s, t):
        """
        计算字符串s和t之间的排列差异。

        :type s: str
        :type t: str
        :rtype: int
        """
        # 初始化差异值为0
        diff = 0

        # 创建字典来存储 t 中每个字符的位置
        index_map_t = {char: idx for idx, char in enumerate(t)}

        # 遍历字符串 s
        for idx_s, char_s in enumerate(s):
            if char_s in index_map_t:
                # 如果字符存在于 t 中，则计算其位置差的绝对值
                idx_t = index_map_t[char_s]
                diff += abs(idx_s - idx_t)

        return diff


# 示例代码执行
if __name__ == '__main__':
    s = "abc"
    t = "bac"
    print(Solution.findPermutationDifference(s, t))  # 输出：2
    s = "abcde"
    t = "edbac"
    print(Solution.findPermutationDifference(s, t))  # 输出：12
