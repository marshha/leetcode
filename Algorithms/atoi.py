class Solution(object):
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		val = 0
		sign = 1
		sign_set = False
		num_set = False
		MAX_INT = pow(2,31) - 1
		MIN_INT = -1 * pow(2,31)
		for c in str:
				if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
					num_set = True
					val = (val * 10) + (ord(c) - ord("0"))
					if val > MAX_INT:
						break

				elif (val == 0) and c in [" ", "\t"]:
					if num_set or sign_set:
						break
					continue

				elif (val == 0) and c in ["+", "-"]:
					if sign_set:
						break

					if num_set:
						break

					sign_set = True

					if c == "+":
						sign = 1
					else:
						sign = -1
				else:
					# junk chars
					if num_set or sign_set:
						break
					break

		out_val = sign * val
		if out_val > MAX_INT:
			return MAX_INT

		if out_val < MIN_INT:
			return MIN_INT

		return out_val

sol = Solution()
print sol.myAtoi("+-2")
print sol.myAtoi("123")
print sol.myAtoi("-123")
print sol.myAtoi("   -123")
print sol.myAtoi("   -123abc")
print sol.myAtoi("   -1231111111111111111111111abc")
