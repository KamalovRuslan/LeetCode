import bisect


class Solution(object):
    @classmethod
    def kthSmallestPrimeFraction(self, A, K):
            l, r, N = 0, 1, len(A)
            while True:
                m = (l + r) / 2
                border = [bisect.bisect(A, A[i] / m) for i in range(N)]
                cur = sum(N - i for i in border)
                if cur > K:
                    r = m
                elif cur < K:
                    l = m
                else:
                    return max([(A[i], A[j]) for i, j in \
                        enumerate(border) if j < N], key=lambda x: x[0] / x[1])

if __name__ == "__main__":
    # A = [1, 2, 3, 5]
    # K = 3
    A = list(map(int, input().split()))
    K = int(input())
    print(Solution.kthSmallestPrimeFraction(A, K))
