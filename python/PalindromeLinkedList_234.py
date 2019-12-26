class Solution:
    def isPalindrome(self, head):
        to_list=[]
        while head is not None:
            to_list.append(head.val)
            head=head.next
        i,j=0,len(to_list)-1
        while i<j:
            if to_list[i]!=to_list[j]:
                return False
            else:
                i+=1
                j-=1
        return True

    def isPalindrome1(self, head):
        fast=slow=ListNode(0)
        fast=slow=head
        stack=[]

        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next

        if fast:
            slow=slow.next
        while slow:
            top=stack.pop()
            if top!=slow.val:
                return False
            slow=slow.next
        return True