import numpy as np


class Solution:

	@classmethod
	def price(self, a, b):
		if a == b:
			return 0
		else:
			return 1
	@classmethod
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		M, N = len(word1), len(word2)
		if M == 0:
			return N
		elif N == 0:
			return M
		dist_matrix = np.zeros((M + 1, N + 1))
		for i in range(N + 1):
			dist_matrix[0, i] = i
		for i in range(M + 1):
			dist_matrix[i, 0] = i
		for i in range(1, M + 1):
			for j in range(1, N + 1):
				dist_matrix[i, j] = min(dist_matrix[i - 1, j] + 1,
										dist_matrix[i, j - 1] + 1,
										dist_matrix[i - 1, j - 1] +
										self.price(word1[i - 1], word2[j - 1]))
		return dist_matrix[M, N]


if __name__ == "__main__":
	word1 = input()
	word2 = input()
	print(Solution.minDistance(word1, word2))
