class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < len(grid) and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < len(grid[0]) and grid[i][j] == grid[i][j + 1]:
                    return False
        return True


if __name__ == '__main__':
    grid = [[1, 0, 2], [1, 0, 2]]
    print(Solution().satisfiesConditions(grid))
    grid = [[1, 1, 1], [0, 0, 0]]
    print(Solution().satisfiesConditions(grid))
    grid = [[1], [2], [3]]
    print(Solution().satisfiesConditions(grid))
    grid = [[0]]
    print(Solution().satisfiesConditions(grid))
