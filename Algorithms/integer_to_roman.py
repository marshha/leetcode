class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val_dict = {
            1:        "I",
            4:        "IV",
            5:        "V",
            9:        "IX",
            10:       "X",
            40:       "XL",
            50:       "L",
            90:       "XC",
            100:      "C",
            400:      "CD",
            500:      "D",
            900:      "CM",
            1000:     "M",
        }

        val_list = sorted(val_dict.keys(), reverse=True)

        rem = num
        out_str = ""
        while rem > 0:
            for val in val_list:
                if (rem - val) < 0:
                    continue

                out_str += val_dict[val]
                rem -= val
                break

        return out_str

sol = Solution()
print sol.intToRoman(20)
