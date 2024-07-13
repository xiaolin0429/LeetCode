"""
假定一段路径记作字符串 path，其中以 "." 作为分隔符。现需将路径加密，加密方法为将 path 中的分隔符替换为空格 " "，请返回加密后的字符串。

示例 1：
输入：path = "a.aef.qerf.bb"

输出："a aef qerf bb"

限制：
0 <= path.length <= 10000
"""


class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        for i in path:
            if i == ".":
                path = path.replace(i, " ")
        return path


if __name__ == '__main__':
    path = "a.aef.qerf.bb"
    print(Solution().pathEncryption(path))
