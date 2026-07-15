class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        last_seen = {}
        max_streak = 0
        current_streak = 0
        for i in range(len(s)):
            if s[i] not in last_seen:
                last_seen[s[i]] = i
                current_streak += 1
            else:
                if current_streak > max_streak:
                    max_streak = current_streak
                potential_streak = i - last_seen[s[i]]
                if potential_streak <= current_streak:
                    current_streak = potential_streak
                else:
                    current_streak += 1
                last_seen[s[i]] = i
        if current_streak > max_streak:
            max_streak = current_streak
        return max_streak
                
        