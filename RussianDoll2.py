import bisect
import sys


class Doll(object):

    def __init__(self, envelop):
        self.w = envelop[0]
        self.h = envelop[1]

    def __lt__(self, other):
        if self.w != other.w:
            return self.w < self.w
        else:
            return self.h > other.h


class Solution(object):
    @classmethod
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        dolls = [Doll(env) for env in envelopes]
        dolls.sort()
        tmp = [sys.maxsize] * len(dolls)
        for i, doll in enumerate(dolls):
            idx = bisect.bisect_left(tmp, doll.h, hi=i)
            tmp[idx] = dolls[idx].h
        for i, t in enumerate(tmp[::-1]):
            if t != sys.maxsize:
                result = len(tmp) - i
                break
        return result

if __name__ == "__main__":
    inp = input()
    envelopes = eval(inp)
    print(Solution.maxEnvelopes(envelopes))
