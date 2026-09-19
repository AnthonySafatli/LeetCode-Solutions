class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        value = 0
        is_pos = True

        checked_whitespace = False
        checked_signedness = False
        checked_leading_0 = False

        for letter in s:
            if not checked_whitespace:
                if letter == ' ':
                    continue
                else:
                    checked_whitespace = True
            
            if not checked_signedness:
                checked_signedness = True
                if letter == '-':
                    is_pos = False
                    continue
                elif letter == '+':
                    continue
            
            if not checked_leading_0 and letter == '0':
                continue
            checked_leading_0 = True

            try:
                letter_val = int(letter)
                value = (value * 10) + letter_val
            except:
                break

        if not is_pos:
            value *= -1

        if value < -(2**31):
            return -(2**31)
        
        if value > (2**31) - 1:
            return (2**31) - 1

        return value
                    
                

                    
            

        

        
