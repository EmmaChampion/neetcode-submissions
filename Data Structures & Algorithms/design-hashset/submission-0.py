class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hashset)):
            if self.hashset[i] == key:
                self.hashset[i], self.hashset[len(self.hashset) - 1] = self.hashset[len(self.hashset) - 1], self.hashset[i]
                self.hashset.pop()
                return

    def contains(self, key: int) -> bool:
        for item in self.hashset:
            if item == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)