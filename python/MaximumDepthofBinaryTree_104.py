from createtree import tree

class Solution:
    def maxDepth(self, root):
        max_depth=0
        if root is None:
            return max_depth
        else:
            return self.search_max_depth(root,max_depth)

    def search_max_depth(self,tree,max_depth):
        if tree is None:
            return max_depth
        else:
            max_depth+=1
            return max(self.search_max_depth(tree.left,max_depth),self.search_max_depth(tree.right,max_depth))

    def maxDepth1(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth1(root.left),self.maxDepth1(root.right))+1
if __name__ == '__main__':
    s=Solution()
    l=[1,2,2,3,4,4,3]
    root=tree(l)
    print(s.maxDepth(root))