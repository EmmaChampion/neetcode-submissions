class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        to_compare = "".join(sorted(s1))
        left = 0
        for right in range(len(s1), len(s2) + 1):
            section = s2[left : right]
            section = "".join(sorted(section))
            if section == to_compare:
                return True
            left += 1
        return False