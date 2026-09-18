class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_str = str(x)

        for i, letter in enumerate(x_str):
            opp_idx = -(i + 1) 
            if x_str[opp_idx] != letter:
                return False

        return True
