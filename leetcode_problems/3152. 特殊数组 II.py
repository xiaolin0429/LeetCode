"""
如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
你有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助你检查
子数组
 nums[fromi..toi] 是不是一个 特殊数组 。
返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。

示例 1：
输入：nums = [3,4,1,2,6], queries = [[0,4]]
输出：[false]
解释：
子数组是 [3,4,1,2,6]。2 和 6 都是偶数。

示例 2：
输入：nums = [4,3,1,6], queries = [[0,2],[2,3]]
输出：[false,true]

解释：
子数组是 [4,3,1]。3 和 1 都是奇数。因此这个查询的答案是 false。
子数组是 [1,6]。只有一对：(1,6)，且包含了奇偶性不同的数字。因此这个查询的答案是 true。

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""


class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        判断数组中指定范围内的元素是否具有特定的奇偶性差异。

        :type nums: List[int]
        :param nums: 输入的整数数组。
        :type queries: List[List[int]]
        :param queries: 查询数组，每个查询由起始和结束索引组成。
        :rtype: List[bool]
        :return: 返回一个布尔值列表，指示每个查询范围内是否存在连续的奇偶性差异。
        """
        # 检查输入数组是否为空
        if not nums or not queries:
            return []

        # 预处理奇偶性差异
        # parity数组记录了nums中每个位置与前一位置的奇偶性是否不同
        parity = [0] * len(nums)
        for i in range(1, len(nums)):
            parity[i] = 1 if (nums[i] % 2) != (nums[i - 1] % 2) else 0

        # 计算前缀和数组
        # 前缀和数组用于快速计算任意区间内的奇偶性差异数量
        prefix_sum = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + parity[i]

        # 初始化答案列表
        ans = []
        # 遍历查询数组
        for i, j in queries:
            # 检查查询范围是否有效
            if i < 0 or j >= len(nums) or i > j:
                ans.append(False)
            else:
                # 查询范围内奇偶性不同的位置数量
                count = prefix_sum[j] - prefix_sum[i]
                # 如果查询范围内的奇偶性差异数量等于范围大小，则所有元素的奇偶性都不同
                is_special = (count == (j - i))
                ans.append(is_special)

        return ans


if __name__ == '__main__':
    nums = [3, 4, 1, 2, 6]
    queries = [[0, 4]]
    print(Solution().isArraySpecial(nums, queries))
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]
    print(Solution().isArraySpecial(nums, queries))
