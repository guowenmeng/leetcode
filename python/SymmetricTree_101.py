# Definition for a binary tree node.
from createtree import tree


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isequal(root.left,root.right)

    def isequal(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is not None and node2 is not None and node1.val==node2.val:
            return self.isequal(node1.left,node2.right) and self.isequal(node1.right,node2.left)
        else:
            return False


if __name__ == '__main__':
    s=Solution()
    l=[1,2,2,3,4,4,3]
    root=tree(l)
    print(s.isSymmetric(root))
