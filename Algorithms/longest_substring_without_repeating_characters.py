class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		char_last_idx = {}
		max_len = 0
		start_idx = -1
		curr_idx = 0

		for c in s:
			if c in char_last_idx:
				start_idx = max(start_idx, char_last_idx[c])

			char_last_idx[c] = curr_idx

			max_len = max(max_len, curr_idx-start_idx)
			curr_idx += 1

		print max_len
		return max_len

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
s.lengthOfLongestSubstring("bbbbb")
s.lengthOfLongestSubstring("pwwkew")
s.lengthOfLongestSubstring("C")
s.lengthOfLongestSubstring("au")
