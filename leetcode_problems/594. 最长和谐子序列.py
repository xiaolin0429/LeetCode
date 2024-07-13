"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]
示例 2：

输入：nums = [1,2,3,4]
输出：2
示例 3：

输入：nums = [1,1,1,1]
输出：0
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：
        # from collections import Counter
        # counter = Counter(nums)
        # res = 0
        # for key in counter:
        #     if key + 1 in counter:
        #         res = max(res, counter[key] + counter[key + 1])
        # return res

        # 方法二（leetcode官方答案）：
        nums.sort()
        res, begin = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                res = max(res, end - begin + 1)
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    print(Solution().findLHS(nums))
if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    print(Solution().findLHS(nums))
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().findLHS(nums))