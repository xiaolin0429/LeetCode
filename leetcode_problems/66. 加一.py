"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #代码1：
        """
        num = 0
        for i in digits:
            num = num * 10 + i
        num += 1
        return [int(i) for i in str(num)]
        """

        #代码2：
        # 从个位开始遍历
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # 如果所有位都是9，则需要在最前面添加一位1
        return [1] + digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([4, 3, 2, 1]))

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0]))
