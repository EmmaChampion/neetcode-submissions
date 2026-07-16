class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.ordered) == 0:
            self.ordered.append(val)
        else:
            self.ordered.append(min(self.ordered[-1], val))

    def pop(self) -> None:
        self.ordered.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[-1]
