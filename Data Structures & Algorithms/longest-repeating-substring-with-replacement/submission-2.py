class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        in_window = {}
        max_freq = 0

        for right in range(len(s)):
            #Update counts
            if s[right] in in_window:
                in_window[s[right]] += 1
            else:
                in_window[s[right]] = 1
            
            #Update count of most frequent letter
            if in_window[s[right]] > max_freq:
                max_freq = in_window[s[right]]
            
            #If window is too big, shrink from left
            while right - left + 1 > max_freq + k:
                in_window[s[left]] -= 1
                left += 1
            
            if right - left + 1 > max_length:
                max_length = right - left + 1
        return max_length
            