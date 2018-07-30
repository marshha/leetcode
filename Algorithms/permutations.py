class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 1:
			return [ nums ]

		all_p = set()

		val_count_map = {}
		for n in nums:
			if n not in val_count_map:
				val_count_map[n] = 0

			val_count_map[n] += 1

		vals = val_count_map.keys()

		for x in vals:
			val = x

			rem = []
			for k,v in val_count_map.iteritems():
				if k == val:
					v = v - 1

				for x in xrange(0, v):
					rem.append(k)

			for p in self.permute(rem):
				all_p.add( (val,) + tuple(p))

		return list(all_p)

test_case = []
for x in xrange(0, 8):
	test_case.append(1)

test_case.append(2)
test_case.append(3)
test_case  = [1,2,3]
print Solution().permute(test_case)
