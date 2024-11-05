'''Brute force : we have to use an additional data structure
like set and store the nodes in it. If while traversing you
find the node again then it means that there is a cycle'''



''' Optimal code
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next=head
        temp=dummy
        slow=dummy
        fast=dummy
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
        '''