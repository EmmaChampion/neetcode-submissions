class DLLNode():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeTable = {}
        self.keyValTable = {}
        #Head: Least recently used
        self.head = None
        #Tail: Most recently used
        self.tail = None
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.nodeTable:
            return -1
        temp = self.nodeTable[key]
        if temp.next is None:
            return self.keyValTable[temp.val]
        if temp.prev is None:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = self.tail.next
            return self.keyValTable[temp.val]
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = self.tail.next
        
        return self.keyValTable[temp.val]
        

    def put(self, key: int, value: int) -> None:
        if self.length == 0:
            self.head = DLLNode(key)
            print(self.head.val)
            self.tail = self.head
            self.nodeTable[key] = self.head
            self.keyValTable[key] = value
            self.length += 1
        elif key in self.nodeTable:
            temp = self.nodeTable[key]
            if temp.next is None:
                #Already at tail
                self.keyValTable[key] = value
            elif temp.prev is None:
                #At head
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
                self.tail.next = temp
                temp.prev = self.tail
                self.tail = self.tail.next
                self.keyValTable[key] = value
            else:
                #Anywhere in the middle
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = self.tail
                self.tail.next = temp
                self.tail = self.tail.next
                self.keyValTable[key] = value
        elif self.length < self.capacity:
            temp = DLLNode(key)
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = self.tail.next
            self.nodeTable[key] = temp
            self.keyValTable[key] = value
            self.length += 1
            print(self.length, self.head.val)
        else:
            temp = DLLNode(key)
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = self.tail.next
            print(self.length, self.head.val)
            del self.nodeTable[self.head.val]
            del self.keyValTable[self.head.val]
            self.head = self.head.next
            self.head.prev = None
            self.nodeTable[key] = temp
            self.keyValTable[key] = value