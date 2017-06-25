class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word == word.upper():
            return True

        if word == word.lower():
            return True

        first_char = word[0]
        following_chars = word[1:]
        if first_char.upper() == first_char:
            if following_chars == following_chars.lower():
                return True

        return False

sol = Solution()
print sol.detectCapitalUse("USA")
print sol.detectCapitalUse("FlaG")
print sol.detectCapitalUse("I")
print sol.detectCapitalUse("i")
