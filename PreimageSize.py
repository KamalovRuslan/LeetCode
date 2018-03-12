class Solution(object):
    def preimageSizeFZF(self, K):
        if K == 0:
            return 5
        k = K << 2
        tmp = self._count_zero(k)
        while tmp < K:
            k += 5
            tmp = self._count_zero(k)
        result = 0 if tmp != K else 5
        return result

    def _count_zero(self, K):
        base = 5
        count = 0
        while K / base:
            count += K / base
            base *= 5
        return count

if __name__ == "__main__":
    K = int(input())
    solution = Solution()
    print(solution.preimageSizeFZF(K))
