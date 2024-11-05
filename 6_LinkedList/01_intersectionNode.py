
'''BRUTE FORCE NESTED LOOPS
def intersectionPresent(head1, head2):
    while head2 != None:
        temp = head1
        while temp != None:
            # if both nodes are same
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    # intersection is not present between the lists
    return None
'''

'''HASHING SOLUTION
def intersectionPresent(head1, head2):
    st = set()
    while head1 != None:
        st.add(head1)
        head1 = head1.next
    while head2 != None:
        if head2 in st:
            return head2
        head2 = head2.next
    return None
'''


'''We can also find the difference in the length and use
it to find the intersection point'''



'''  OPTIMAL SOLUTION
while learning this algo i got a foubt how does this exit
the loop when there is no intersection point, it exits the loop
because after traversing till the end ofeach linkedlist they
get redirected to the other one and after that they both reach null
at the same point because the sum of lengths are equal
the while condition temp1!=temp2 fails and it exits the loop

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        temp1=headA
        temp2=headB
        while temp1 != temp2:
            if temp1:
                temp1=temp1.next
            else:
                temp1=headB
            if temp2:
                temp2=temp2.next
            else:
                temp2=headA
            
        return temp1
'''  