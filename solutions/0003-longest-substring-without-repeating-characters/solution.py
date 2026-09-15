class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        longest_substring = 0
        for i in range(len(s)):
            substring = s[i:]
            if len(substring) <= longest_substring:
                break
            
            starting_substring = substring[:longest_substring]
            letters = set(starting_substring)
            substring_length = longest_substring

            if len(letters) < len(starting_substring):
                continue

            while True:
                curr_letter = substring[substring_length]
                if curr_letter in letters:
                    break

                letters.add(curr_letter)
                substring_length += 1

                if len(substring) <= substring_length:
                    break

            if substring_length > longest_substring:
                longest_substring = substring_length

        return longest_substring



