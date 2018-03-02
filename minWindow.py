from collections import Counter
import sys

class Solution:
	@classmethod
	def minWindow(self, string, patch):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		patch_counter = Counter(patch)
		string_counter = Counter()
		len_patch = len(patch)

		count = 0
		start = 0
		start_index = None
		min_len = sys.maxsize
		for i, c in enumerate(string):
			string_counter[c] += 1
			if patch_counter[c] and string_counter[c] <= patch_counter[c]:
				count += 1
			if count == len_patch:
				while string_counter[string[start]] > patch_counter[string[start]] or \
												patch_counter[string[start]] == 0:
					if string_counter[string[start]] > patch_counter[string[start]]:
						string_counter[string[start]] -= 1
					start += 1
				len_window = i - start + 1
				if min_len > len_window:
					min_len = len_window
					start_index = start
		if start_index is None:
			return ""
		return string[start_index:start_index + len_window]

if __name__ == "__main__":
	string = input()
	patch = input()
	print(Solution.minWindow(string, patch))
