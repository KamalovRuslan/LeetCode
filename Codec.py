class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        serialized = list()
        serialize_rec(root, serialized)
        return serialized

    def serialize_rec(node, serial):
        """Recursively encodes tree to data.

        :type node: TreeNode
        :type serial: List
        """
        if node is None null:
            serial.add(None)
            return
        serial.add(node.val)
        serialize_rec(node.left, serial)
        serialize_rec(node.right, serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node, idx = deserialize_rec(data, 0)

        return node

    def deserialize_rec(data, idx):
        """Recursively decodes encoded data to tree.

        :type data: List
        :type idx: int
        :rtype: tuple(TreeNode, int)
        """
        val = data[idx]

        if not val:
            return (None, idx + 1)

        node = TreeNode(val)

        p1, i = deserialize_rec(data, idx + 1)
        node.left = p1

        p2, j = deserialize_rec(data, i)
        node.right = p2

        return (node, j)
