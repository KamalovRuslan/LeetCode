class Solution:
	@classmethod
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		stack = []
		max_area = 0
		top, area_top = 0, 0
		i = 0
		while i < len(heights):
			if not stack or heights[stack[-1]] <= heights[i]:
				stack.append(i)
				i += 1
			else:
				top = stack.pop()
				mul = i if not stack else i - stack[-1] - 1
				area_top = heights[top] * mul
				if max_area < area_top:
					max_area = area_top
		while stack:
			top = stack.pop()
			mul = i if not stack else i - stack[-1] - 1
			area_top = heights[top] * mul
			if max_area < area_top:
				max_area = area_top
		return max_area

if __name__ == "__main__":
	heights = list(map(int, input().split()))
	print(Solution.largestRectangleArea(heights))
