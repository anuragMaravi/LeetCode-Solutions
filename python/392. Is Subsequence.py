class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		if s == "":
			return True
		found_indices = []
		current_s_idx = 0
		for i, letter in enumerate(t):
			if s[current_s_idx] == letter:
				found_indices.append(i)
				current_s_idx += 1
			if len(s) == current_s_idx:
				break

		if len(found_indices) == len(s):
			return True
		else:
			return False
	    	

s = Solution()
ans = s.isSubsequence("b", "abc")
print(ans)