class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        for word in strs:
            anagram_found = False
            for anagram_list in grouped:
                if self.isAnagram(word, anagram_list[0]):
                    anagram_found = True
                    anagram_list.append(word)
                    break
            if not anagram_found:
                grouped.append([word])
        return grouped
    
    def isAnagram(self, s, t):
        s_hash = {}
        t_hash={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1
            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
        return s_hash == t_hash