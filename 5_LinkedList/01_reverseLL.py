# brute force using extra memory(stack)
from typing import Lists
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        temp=head
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            temp.val=stack.pop()
            temp=temp.next
        return head
    
#OPTIMAL
def reverse(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev