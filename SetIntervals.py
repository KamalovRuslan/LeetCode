class Interval(object):

    def __init__(self, interval):
        self.a = interval[0]
        self.b = interval[1]

    def __lt__(self, other):
        return self.b < other.b or self.b == other.b and self.a > other.a


class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ints = [Interval(interval) for interval in intervals]
        ints.sort()
        picks = []
        for interval in ints:
            if interval.b - 1 not in picks:
                picks.append(interval.b - 1)
                picks.append(interval.b)
            elif interval.b not in picks:
                picks.append(interval.b)
        return picks


if __name__ == "__main__":
    intervals = eval(input())
    solution = Solution()
    print(solution.intersectionSizeTwo(intervals))
