class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(t) == 0:
            return ""
        
        t_freqs = {}
        for char in t:
            if char in t_freqs:
                t_freqs[char] += 1
            else:
                t_freqs[char]  = 1
        unmatched = len(t_freqs)
        
        left = 0
        right = 0
        s_freqs = {}
        shortest = ""

        while right <= len(s):
            if unmatched != 0:
                if right == len(s):
                    break
                if s[right] in s_freqs:
                    s_freqs[s[right]] += 1
                else:
                    s_freqs[s[right]] = 1
                
                if s[right] in t_freqs and s_freqs[s[right]] == t_freqs[s[right]]:
                    unmatched -= 1
                right += 1
            else:
                if shortest == "":
                    shortest = s[left:right]
                if right - left < len(shortest):
                    shortest = s[left: right]
                s_freqs[s[left]] -= 1
                if s[left] in t_freqs:
                    if s_freqs[s[left]] < t_freqs[s[left]]:
                        unmatched += 1
                left += 1
        
        if unmatched == 0:
            if shortest == "":
                shortest = s[left:right]
            if right - left + 1 < len(shortest):
                shortest = s[left: right]
            
        return shortest
        