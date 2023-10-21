class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        return f"{self.name} ({self.weight})"


a = Node("Abslau", 1)
b = Node("Abslau Júnior", 2)
c = Node("Abslau Senior", 3)
d = Node("d", 4)
a.add_child(b)
a.add_child(c)
b.add_child(d)
print(a.children[0].parent.name)
print(a.children[1].parent.name)