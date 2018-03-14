class Solution(object):
    def largestBanner(self, hist):
        hist.append(0)
        stack = [-1]
        area = 0
        for i in range(len(hist)):
            while hist[i] < hist[stack[-1]]:
                h = hist[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
        return area

    def largestArea(self, matrix):
        hist = [0 for i in range(len(matrix[0]))]
        area = 0
        for row in matrix:
            hist = [h + 1 if elem == 1 else 0 for h, elem in zip(hist, row)]
            area = max(area, self.largestBanner(hist))
        return area

if __name__ == "__main__":
    hist = eval(input())
    solution = Solution()
    print(solution.largestBanner(hist))
