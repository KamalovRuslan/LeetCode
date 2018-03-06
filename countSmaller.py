class Node(object):

    def __init__(self, val):

        self.val = val
        self.left = left
        self.right = right
        self.counter = 0


class BinTree(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(root, val)

    def _insert(self, node, val):
        if node is None:
            node = Node(val)
            return
        elif node.val < val:
            self._insert(node.right, val)
        else:
            node.counter += 1
            self._insert(node.left, val)
        return

    def search(self, val):
        if self.root is None:
            raise ValueError("Tree is Empty!")
        elif root.val == val:
            return root.counter
        elif root.val > val:
            return self._search(root.left, val)
        else:
            return self._search(root.right, val)

    def _search(self, node, val):
        if node.val is None:
            raise ValueError("{} not contained in nums!".format(val))
        if node.val == val:
            return node.counter
        elif node.val > val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)


class CounterSmaller(object):

    def __init__(self, nums):
        self.nums = nums
        self.tree = BinTree()
        for num in nums:
            self.tree.insert(num)

    def __getitem__(self, idx):
        val = self.nums[idx]
        return self.tree.search(val)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    tree = BinTree()
    for num in nums:
        tree.insert(num)
    counter_smaller = CounterSmaller(nums)
    print([counter_smaller[i] for i in range(len(nums))])
