# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		out_rev = []
		carry_val = 0
		while True:
			l1_val = l1.val if l1 else 0
			l2_val = l2.val if l2 else 0

			if not l1 and not l2 and not carry_val:
				break


			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

			append_val = l1_val + l2_val + carry_val

			carry_val = 0
			if append_val > 9:
				carry_val = 1
				append_val = append_val - 10

			out_rev.append(append_val)

		out_list = None
		out_iter = None
		for x in out_rev:
			if out_list == None:
				new_entry = ListNode(x)
				out_list = new_entry
			else:
				new_entry = ListNode(x)
				out_iter.next = new_entry

			out_iter = new_entry

		return out_list

def NumToListNode(val):
	out_list = None
	for x in reversed(str(val)):
		x = int(x)
		if out_list == None:
			new_entry = ListNode(x)
			out_list = new_entry
		else:
			new_entry = ListNode(x)
			out_iter.next = new_entry

		out_iter = new_entry
	return out_list

def ListNodeToNum(val):
	out_str = ""
	while val:
		out_str = str(val.val) + out_str
		val = val.next

	return int(out_str)

t1 = NumToListNode(4)
t2 = NumToListNode(6)
s = Solution()
print ListNodeToNum(s.addTwoNumbers(t1, t2))
