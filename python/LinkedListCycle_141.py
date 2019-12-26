class Solution:
    def hasCycle(self, head):
        node=head
        dic={}
        while node is not None:
            if node in dic:
                return True
            else:
                dic[node]=0
                node=node.next
        return False

    def hasCycle1(self, head):
        slow,fast=head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
            if slow==fast:
                return True
        return False
