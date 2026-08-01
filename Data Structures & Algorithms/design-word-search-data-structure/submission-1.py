class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        trie = self.root
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        if "End" not in trie:
            trie["End"] = None

    def search(self, word: str, trie="root") -> bool:
        if trie == "root":
            trie = self.root
        for i in range(len(word)):
            if word[i] ==".":
                tempWord = word[i+1:]
                for char in trie:
                    if char == "End":
                        continue
                    if self.search(tempWord, trie[char]):
                        return True
                return False
            else:
                if word[i] not in trie:
                    return False
                trie = trie[word[i]]
        if "End" not in trie:
            return False
        return True