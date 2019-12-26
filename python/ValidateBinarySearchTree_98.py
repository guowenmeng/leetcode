# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        # if root is None:
        #     return True
        # if root.left is not None and root.right is None:
        #     if root.left.val>=root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left)
        # if root.right is not None and root.left is None:
        #     if root.right.val <=root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.right)
        # if root.right is None and root.right is None:
        #     return True
        # if root.left is not None and root.right is not None:
        #     if root.left.val>=root.val or root.right.val <=root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left) and self.isValidBST(root.right)
        pass
    def isValidBST(self, root):
        return self.valid(root,float('-inf'),float('inf'))

    def valid(self,root,min,max):
        if not root:
            return True
        if root.val>=max or root.val<=min:
            return False
        return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)

if __name__ == '__main__':
    s=Solution()
    t1=TreeNode(2)
    t2=TreeNode(1)
    t3=TreeNode(3)
    t1.left=t2
    t1.right=t3
    print(s.isValidBST(t1))