class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultLen = 0
        result = ""

        def expand(center):
            nonlocal result, resultLen
            #Check for odd length
            curLen = -1
            left = center
            right = center
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curLen += 2
                    left -= 1
                    right += 1
                else:
                    break
            if curLen > resultLen:
                resultLen = curLen
                result = s[left + 1 : right]

            #Check for even length
            if center < len(s) - 1 and s[center] == s[center + 1]:
                curLen = 0
                left = center
                right = center + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        curLen += 2
                        left -= 1
                        right += 1
                    else:
                        break
                if curLen > resultLen:
                    resultLen = curLen
                    result = s[left + 1 : right]
        
        for i in range(len(s)):
            expand(i)
        
        return result