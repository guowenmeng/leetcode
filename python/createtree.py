class TreeNode:
    def __init__(self,x=None):
        self.val=x
        self.left=None
        self.right=None

#方法一，递归
def listcreatetree(root,llist,i):
    if i<len(llist):
        if llist[i]=='#':
            return None
        else:
            root=TreeNode(llist[i])
            root.left=listcreatetree(root.left,llist,2*i+1)
            root.right=listcreatetree(root.right,llist,2*i+2)
            return root
        return root

#方法二,递归
def tree(l):
    # 创建根节点
    if len(l)==0:
        node=TreeNode()
        return node
    else:
        return createtree(l,0)


def createtree(l,i):
    if i >len(l)-1:
        return None
    node=TreeNode(l[i])
    # print(node.val)
    node.left=createtree(l,2*i+1)
    node.right=createtree(l,2*i+2)
    return node


if __name__ == '__main__':
    # root=TreeNode()
    l=[1,2,2,3,4,4,3]
    # root=listcreatetree(root,l,0)
    root=tree(l)
