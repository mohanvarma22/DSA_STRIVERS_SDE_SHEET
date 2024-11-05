#Brute force
'''class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        temp = head
        while temp:
            if temp.val != arr.pop():
                return False
            temp=temp.next
        return True'''

'''# Definition for singly-linked list.

Optimal approach slow fast pointers vadi slow ni middle element
varaku techi slow.next value reverse function nunchi return ayye value
assign cheste reversed linked list attach aypoyiddi then
slow ni second half first element loki pampinchi head deggara oka pointer assign 
chesi slow null ayye varaku compare cheyali


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next.next and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=self.reverse(slow.next)
        slow=slow.next
        temp=head
        while slow:
            if slow.val!=temp.val:
                return False
            slow=slow.next
            temp=temp.next
        return True

    def reverse(self,head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
'''