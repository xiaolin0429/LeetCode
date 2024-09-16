class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start
        sum1 = sum(distance[start:destination])
        sum2 = sum(distance) - sum1
        return min(sum1, sum2)


if __name__ == '__main__':
    sol = Solution()
    distance = [1, 2, 3, 4]
    start = 0
    destination = 1
    print(sol.distanceBetweenBusStops(distance, start, destination))
    distance = [1, 2, 3, 4]
    start = 0
    destination = 2
    print(sol.distanceBetweenBusStops(distance, start, destination))
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    print(sol.distanceBetweenBusStops(distance, start, destination))
