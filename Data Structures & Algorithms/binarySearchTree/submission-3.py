class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)

        if not self.root:
            self.root = newNode
            return

        curr = self.root

        while curr:
            if curr.key < key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            elif curr.key > key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1
    
    def findMin(self, curr: TreeNode) -> TreeNode:
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        curr = self.findMax(self.root)
        return curr.val if curr else -1
    
    def findMax(self, curr: TreeNode) -> TreeNode:
        while curr and curr.right:
            curr = curr.right
        return curr

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
