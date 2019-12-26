# TODO 寻找更优的解法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self,root,sum):
        path_nums_sum=[0]
        if root:
            self.recurvenode(root,sum,path_nums_sum)
        return path_nums_sum[0]

    def recurvenode(self,node,sum,path_nums_sum):
        if node is None:
            return
        elif node.val==sum:
            path_nums_sum[0] += 1
        self.findpath(node.left,node.val,sum,path_nums_sum)
        self.findpath(node.right,node.val,sum,path_nums_sum)
        self.recurvenode(node.left,sum,path_nums_sum)
        self.recurvenode(node.right,sum,path_nums_sum)
    def findpath(self,node,val,sum,path_nums_sum):
        if node is None:
            return
        elif node.val+val==sum:
            path_nums_sum[0]+=1
        self.findpath(node.left,node.val+val,sum,path_nums_sum)
        self.findpath(node.right,node.val+val,sum,path_nums_sum)