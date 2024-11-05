'''brute force calculate the length and the 
 that we want tp remove is the L-N+1 th element
 worst case 2 traversals
 '''
#optimal
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move the first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next

        # Now, second.next is the node to be removed
        second.next = second.next.next

        # Return the head of the modified list
        return dummy.next