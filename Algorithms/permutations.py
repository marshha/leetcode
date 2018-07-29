class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 1:
			return [ nums ]

		all_p = set()
		for x in xrange(0, len(nums)):
			val = nums[x]
			rem = list(nums)
			rem.pop(x)
			for p in self.permute(rem):
				all_p.add( (val,) + tuple(p))

		return list(all_p)

print Solution().permute([1,2,3])
