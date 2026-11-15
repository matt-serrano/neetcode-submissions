class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        length = len(self.MinStack)
        item = self.MinStack[length - 1]

        if (type(item) != int):
            return null
        else:
            return item

    def getMin(self) -> int:
        if (len(self.MinStack) == 0):
            return null

        min = self.MinStack[0]
        for i in self.MinStack:
            if i < min:
                min = i

        return min
