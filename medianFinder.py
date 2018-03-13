from heapq import heapify, heappush, heappop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max = heapify([])
        self.min = heapify([])

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.max, num)

        self.min.heappush(self.max[0])
        self.max.heappop()

        if len(self.max) < len(self.min):
            self.max.heappush(self.min[0])
            self.min.heappop()
        return

    def findMedian(self):
        """
        :rtype: float
        """
        median = self.max[0] if len(self.max) > len(self.min) else \
                 (self.max[0] + self.min[0]) * 0.5
        return median
