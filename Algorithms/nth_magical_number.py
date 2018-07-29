import math

class Solution(object):
	def nthMagicalNumber(self, N, A, B):
		"""
		:type N: int
		:type A: int
		:type B: int
		:rtype: int
		"""
		def gcd(x1, x2):
			if x1 > x2:
				x1, x2 = x2, x1

			rem = x2 % x1
			if rem == 0:
				return x1

			return gcd(x1, rem)

		def lcm(x1, x2):
			return (x1 * x2) / gcd(x1, x2)

		lcm_ab = lcm(A, B)

		# get the list of magical numbers before repeating
		vals = set()
		for x in xrange(1, (lcm_ab / A) + 1):
			vals.add(x * A)

		for x in xrange(1, (lcm_ab / B) + 1):
			vals.add(x* B)

		vals = sorted(list(vals))

		#print lcm(A, B), gcd(A, B), vals

		# the Nth value will be the Nth entry in vals, (vals + (1 * lcm)), (vals + (2 * lcm)) ...
		# the index N is 1-indexed, list is 0-indexes, so offset it
		n_vals = len(vals)
		n_iter = (N-1) / n_vals
		n_idx = (N-1) % n_vals

		return (vals[n_idx] + (lcm_ab * n_iter)) % int(math.pow(10,9) + 7)

print Solution().nthMagicalNumber(136, 556, 584)

