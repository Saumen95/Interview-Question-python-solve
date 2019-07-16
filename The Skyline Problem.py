import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        delete = {}

        for building in buildings:
            tmp1 = [building[0], -building[2]]
            tmp2 = [building[1], building[2]]
            points.append(tmp1)
            points.append(tmp2)

        points.sort(key = lambda x: (x[0], x[1]))
        print(points)
        max_value = 0
        heap = []
        heapq.heappush(heap, max_value)
        ret = []

        for point in points:
            if point[1] < 0:
                heapq.heappush(heap, point[1])
