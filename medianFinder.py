from heapq import heapify, heappush, heappop, heappushpop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max = []
        self.min = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.min, -heappushpop(self.max, num))

        if len(self.max) < len(self.min):
            heappush(self.max, -heappop(self.min))
        return

    def findMedian(self):
        """
        :rtype: float
        """
        median = self.max[0] if len(self.max) > len(self.min) else \
                 (self.max[0] - self.min[0]) * 0.5
        return median
