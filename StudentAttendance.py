import numpy as np


class Solution(object):

    def __init__(self):
        self.MOD = 1e9 + 7
        self.TransMatrix = np.array([[1, 0, 0, 0, 0, 0],
                                     [1, 1, 0, 0, 0, 0],
                                     [0, 1, 1, 0, 0, 0],
                                     [1, 0, 0, 1, 0, 0],
                                     [0, 1, 0, 1, 1, 0],
                                     [0, 0, 1, 0, 1, 1]])
        self.ThirdState = np.array([1, 3, 3, 3, 6, 1]).reshape(6, 1)

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        elif n == 2:
            return 9
        elif n == 3:
            return 17
        else:
            return int(self._bin_pow(n).dot(self.ThirdState).sum())

    def _bin_pow(self, n):
        result = np.eye(6)
        mul = self.TransMatrix
        n -= 3
        while n:
            if n % 2:
                result = result.dot(mul) % self.MOD
            mul = mul.dot(mul) % self.MOD
            n >>= 1
        return result

if __name__ == "__main__":
    n = int(input())
    solution = Solution()
    print(solution.checkRecord(n))
