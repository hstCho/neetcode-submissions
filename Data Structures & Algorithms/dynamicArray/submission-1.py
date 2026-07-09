class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        
        for i in range(self.capacity):
            if self.array[i] is None:
                self.array[i] = n
                return

    def popback(self) -> int:
        for i in range(self.capacity - 1, -1, -1):
            if self.array[i] is not None:
                elem = self.array[i]
                self.array[i] = None
                return elem

    def resize(self) -> None:
        self.array += [None] * self.capacity
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        size = 0
        for i in range(self.capacity):
            if self.array[i] is not None:
                size += 1
        return size
    
    def getCapacity(self) -> int:
        return self.capacity
    