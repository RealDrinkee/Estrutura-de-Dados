class BinaryTree():

    def __init__(self):
        self.root = None
        pass

    def insertNode(self, node):
        pass

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def pos_order(self):
        pass

    def preorder(self):

        if root == None:
            return []
        else:
            return [root] + preorder(root.left) + preorder(root.right)
