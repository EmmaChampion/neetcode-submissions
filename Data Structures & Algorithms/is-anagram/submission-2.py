class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for char in s:
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1
        for char in t:
            if char in t_hash:
                t_hash[char] += 1
            else:
                t_hash[char] = 1
        for key, value in s_hash.items():
            if (key not in t_hash) or (t_hash[key] != value):
                return False
            del t_hash[key]
        if t_hash:
            return False
        return True
        