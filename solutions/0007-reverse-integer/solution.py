from math import log10, pow

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0

        is_neg = x < 0
        abs_x = abs(x)
        digit_amount = int(log10(abs_x)) + 1

        value = 0
        for i in range(digit_amount):
            digit = abs_x % 10
            abs_x //= 10

            value += digit * pow(10, (digit_amount - i - 1))

        value = int(value)
        if is_neg:
            value *= -1

        if value > (pow(2, 31) - 1):
            value = 0
        
        if value < -pow(2, 31):
            value = 0

        return value




