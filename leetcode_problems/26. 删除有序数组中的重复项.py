"""
给你一个 非严格递增排列 的数组 nums ，
请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。
然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

提示：
1 <= nums.length <= 3 * 10^4
-104 <= nums[i] <= 10^4
nums 已按 非严格递增 排列
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # 初始化唯一元素的索引
        unique_index = 0

        # 遍历列表中的每个元素
        for current_index in range(1, len(nums)):
            # 如果当前元素与前一个元素不同，则将其移动到下一个唯一元素的位置
            if nums[current_index] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[current_index]

        # 返回唯一元素的数量
        return unique_index + 1


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
