class LinkedList:
    
    def __init__(self):
        self.arr = []
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        return self.arr[index][0]

    def insertHead(self, val: int) -> None:
        if self.length == 0:
            new_arr = [(val, None)]
        else:
            new_arr = [(val, self.arr[0][0])]
            # copy self.arr to new_arr
            for i in range(self.length):
                new_arr += [self.arr[i]]

        self.length += 1
        self.arr = new_arr

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            new_arr = [(val, None)]
        else:
            self.arr[-1] = (self.arr[-1][0], val)
            new_arr = self.arr + [(val, None)]

        self.arr = new_arr
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        
        if index > 0:
            self.arr[index-1] = (self.arr[index-1][0], self.arr[index][1])

        new_arr = []
        for i in range(index):
            new_arr += [self.arr[i]]

        for i in range(index+1, self.length):
            new_arr += [self.arr[i]]

        self.arr = new_arr
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        new_arr = []
        for i in range(self.length):
            new_arr.append(self.arr[i][0])
        return new_arr
