class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        hierarchy = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        pastI = False
        pastX = False
        pastC = False
        value = 0
        for i in range(len(s)):
            index = -(i+1)
            letter = s[index]

            if letter != 'I':
                pastI = True

            if hierarchy.index(letter) > hierarchy.index('X'):
                pastX = True

            if hierarchy.index(letter) > hierarchy.index('C'):
                pastC = True
            
            if letter == 'I':
                if pastI:
                    value -= 1
                else:
                    value += 1
            elif letter == 'V':
                value += 5
            elif letter == 'X':
                if pastX:
                    value -= 10
                else:
                    value += 10
            elif letter == 'L':
                value += 50
            elif letter == 'C':
                if pastC:
                    value -= 100
                else:
                    value += 100
            elif letter == 'D':
                value += 500
            elif letter == 'M':
                value += 1000

        return value



            

        
