class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n)初级写法
        if not nums:
            return True
        for i in range(len(nums) - 1):
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False
        return True
        # O(n)高级写法
        # 检查相邻元素的奇偶性是否不同
        # return all((nums[i] % 2) != (nums[i + 1] % 2) for i in range(len(nums) - 1))


if __name__ == '__main__':
    print(Solution().isArraySpecial([1]))  # True
    print(Solution().isArraySpecial([2, 1, 4]))  # True
    print(Solution().isArraySpecial([4, 3, 1, 6]))  # False
    print(Solution().isArraySpecial([2, 4, 6]))  # False
