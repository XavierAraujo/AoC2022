from __future__ import annotations


class TreeNode:
    def __init__(self, name: str, parent: TreeNode, data: object):
        self.name = name
        self.children = list[TreeNode]()
        self.parent = parent
        self.data = data

    def append_child(self, name: str, data: object):
        child = TreeNode(name, self, data)
        self.children.append(child)
        return child
