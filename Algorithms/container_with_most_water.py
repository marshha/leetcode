class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        start = 0
        end = len(height) - 1

        height_dict = {}

        idx = 0
        for h in height:
            height_dict[idx] = h
            idx += 1

        while (start < end):
            curr_area = (end - start) * min(height_dict[end], height_dict[start])
            if curr_area > max_area:
                max_area = curr_area

            if height_dict[start] < height_dict[end]:
                start += 1

            else:
                end -= 1

        return max_area

sol = Solution()
print sol.maxArea([9, 6, 8])
