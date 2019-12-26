# TODO 链表创建，树的创建，反转链表的迭代和递归实现
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generatelinklist(l):
    if len(l)==0:
        head=None
    else:
        cur=head=ListNode(l[0])
        for i in l[1:]:
            node=ListNode(i)
            cur.next=node
            cur=node
    return head

class Solution:
    def reverseList1(self, head):
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        head=stack.pop()
        new=head
        while stack:
            next_node=stack.pop()
            head.next=next_node
            head=next_node
        head.next=None
        return new

    # 迭代
    def reverseList2(self, head):
        pre=head
        if head:
            cur=head.next
        else:
            return pre
        while cur.next:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        return cur

    # 递归
    def reverseList3(self, head):
        pass

if __name__ == '__main__':
    l=[1,2,3]
    head=generatelinklist(l)
    s=Solution()
    reverse_head=s.reverseList2(head)
    while reverse_head:
        print(reverse_head.val)
        reverse_head=reverse_head.next
