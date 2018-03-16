from bisect import bisect


class Solution(object):

    def kthSmallest(self, maxtrix, k):
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            middle = (left + right) >> 1
            count = sum([bisect(row, middle) for row in matrix])
            if count < k:
                left = middle + 1
            else:
                right = middle
        return left


if __name__ == "__main__":
    matrix = [[1,  5,  9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    solution = Solution()
    print(solution.kthSmallest(matrix, k))
