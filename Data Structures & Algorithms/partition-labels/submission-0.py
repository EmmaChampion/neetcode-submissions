class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        left = 0
        right = 0
        while left < len(s):
            inGroup = set()
            inGroup.add(s[right])
            while len(inGroup) > 0 and right < len(s):
                counts[s[right]] -= 1
                if counts[s[right]] == 0:
                    inGroup.discard(s[right])
                else:
                    inGroup.add(s[right])
                right += 1
            result.append(right - left)
            left = right
            right = left
        
        return result