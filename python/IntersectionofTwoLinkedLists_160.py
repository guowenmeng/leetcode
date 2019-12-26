class Solution:
    def getIntersectionNode(self, headA, headB):
        pa,pb=headA,headB
        while pa!=pb:
            if pa is None:
                pa=headB
            else:
                pa=pa.next
            if pb is None:
                pb=headA
            else:
                pb=pb.next
        return pa
