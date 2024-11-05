'''Brute force
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        temp=head
        while temp:
            if temp in s:
                return temp
            s.add(temp)
            temp=temp.next'''

'''Optimal solution
here first rendu slow and fast meet ayye point kosam search cheyali then 
initialize a 3rd pointer at the start and then move both pointers
at one step each then their meeting point is the starting point of the loop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
        '''