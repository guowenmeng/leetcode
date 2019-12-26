from createtree import tree

class Solution:
    def invertTree(self, root):
        if root is None:
            return
        else:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

    def invertTree1(self,root):
        if root is not None:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root



if __name__ == '__main__':
    s=Solution()
    l=[4,2,7,1,3]
    root=tree(l)
    print(s.invertTree(root))