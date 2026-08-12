class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(center):
            nonlocal count
            #Odd length
            left = center
            right = center
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1

            #Even length
            left = center
            right = center + 1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand(i)
        return count