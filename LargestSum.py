import numpy as np
import sys


class Solution(object):
    @classmethod
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        f = np.array([[sys.maxsize for _ in range(m + 1)] for _ in range(n + 1)])
        sub = np.array([0] * (n + 1))
        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        return f[n][m]

if __name__ == "__main__":
    # nums = [7, 2, 5, 10, 8]
    # m = 2
    nums = list(map(int, input().split()))
    m = int(input())
    print(Solution.splitArray(nums, m))
