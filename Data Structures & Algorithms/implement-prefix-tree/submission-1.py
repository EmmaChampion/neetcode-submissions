class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        trie = self.root
        for char in word:
            if char in trie:
                trie = trie[char]
            else:
                trie[char] = {}
                trie = trie[char]
        if "End" not in trie:
            trie["End"] = None

    def search(self, word: str) -> bool:
        trie = self.root
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        if "End" in trie:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True