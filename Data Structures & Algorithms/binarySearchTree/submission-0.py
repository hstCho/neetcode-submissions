class TreeMap:
    
    def __init__(self):
        self.length = 0
        self.node = []

    def insert(self, key: int, val: int) -> None:
        # If the key is already present in the tree,
        # override with the new key-value pair
        if self.get(key) != -1:
            self.remove(key)

        # Add new key-value into the node list
        self.node.append((key, val))

        # Increment length by 1
        self.length += 1

    def get(self, key: int) -> int:
        for i in range(self.length):
            if self.node[i][0] == key:
                return self.node[i][1]
        # If key is not present in the tree
        return -1

    def getMin(self) -> int:
        if self.length == 0:
            return -1

        min_node_key = float('inf')
        min_node_value = 0
        for i in range(self.length):
            if self.node[i][0] < min_node_key:
                min_node_key = self.node[i][0]
                min_node_value = self.node[i][1]
        return min_node_value

    def getMax(self) -> int:
        if self.length == 0:
            return -1

        max_node_key = float('-inf')
        max_node_value = 0
        for i in range(self.length):
            if self.node[i][0] > max_node_key:
                max_node_key = self.node[i][0]
                max_node_value = self.node[i][1]
        return max_node_value

    def remove(self, key: int) -> None:
        print(self.node)
        for i in range(self.length):
            if self.node[i][0] == key:
                del self.node[i]
                break
        self.length -= 1

    def getInorderKeys(self) -> List[int]:
        new_arr = []
        for i in range(self.length):
            new_arr.append(self.node[i][0])
        new_arr.sort()
        return new_arr

